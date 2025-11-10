"""Downloader command implementation"""

import os
from typing import Dict, List

import questionary
import yaml

from ..classification import PATHS, PERIODS, GRADES, SUBJECTS, HIGH_MUST_OR_NOT, UrlPath
from ..command.download import Download, make_book_url
from ..command.sort_image import SortImage
from ..command.create_pdf import CreatePdf
from ..command.add_bookmark import AddBookmark
from ..command.print_finish_tips import PrintFinishTips
from ..command.success_print import SuccessPrint
from ..constant import IMAGE_CACHE_DIR, SAVE_PDF_DIR, DEFAULT_CONFIG_PATH


class Downloader:
    """Main downloader class"""
    
    def __init__(self, enable_log: bool = False):
        self.enable_log = enable_log
        self.error = None
        
        # User selections
        self.period = ""
        self.grade = ""
        self.subject = ""
        self.authenticated_curl = ""
        
        # Path information
        self.paths: List[UrlPath] = []
        self.path_key = ""
        
        # Working data
        self.images: Dict[str, List[str]] = {}
        self.pdf_bookmark: Dict[str, str] = {}
        self.success: Dict[str, str] = {}
        self.fail: Dict[str, str] = {}
        
        # Directories
        self.images_tmp_dir = IMAGE_CACHE_DIR
        self.pdf_dir = SAVE_PDF_DIR
    
    def prepare_select(self) -> bool:
        """Prepare user selection through interactive prompts"""
        
        # Select period
        period = questionary.select(
            "请选择用书学段",
            choices=PERIODS
        ).ask()
        
        if not period:
            print("你中断了选择用书学段")
            return False
        
        # Select grade
        grade = questionary.select(
            "请选择学生年级",
            choices=GRADES[period]
        ).ask()
        
        if not grade:
            print("你中断了选择学生年级")
            return False
        
        # Select subject
        subject = questionary.select(
            "请选择学科",
            choices=SUBJECTS[period]
        ).ask()
        
        if not subject:
            print("你中断了选择学科")
            return False
        
        # Handle high school special case
        must_or_not_select = ""
        if period == "高中":
            high_key = f"{subject}-{grade}"
            
            if high_key in HIGH_MUST_OR_NOT:
                must_or_not_select = questionary.select(
                    "请选择必修项:",
                    choices=HIGH_MUST_OR_NOT[high_key]
                ).ask()
                
                if not must_or_not_select:
                    print("你中断了选择必修项")
                    return False
        
        # Build key
        key = f"{period}-{grade}-{subject}"
        if must_or_not_select:
            key = f"{period}-{grade}-{subject}-{must_or_not_select}"
        
        # Check if path exists
        if key not in PATHS or not PATHS[key]:
            print("你选择的学段+年级+学科不存在(维护人员正在努力更新中....),请重新选择")
            return False
        
        # Get authenticated curl
        curl = self._get_authenticated_curl()
        if not curl:
            book_url = make_book_url(PATHS[key][0].book_id)
            curl = questionary.text(
                f"请访问 {book_url} 按照 README 输入认证请求",
                multiline=True
            ).ask()
            
            if not curl:
                print("你中断了输入认证请求")
                return False
        
        # Save selections
        self.period = period
        self.grade = grade
        self.subject = subject
        self.authenticated_curl = curl
        self.paths = PATHS[key]
        self.path_key = key.replace("-", "/")
        
        return True
    
    def _get_authenticated_curl(self) -> str:
        """Get authenticated curl from config file if exists"""
        if os.path.exists(DEFAULT_CONFIG_PATH):
            try:
                with open(DEFAULT_CONFIG_PATH, 'r', encoding='utf-8') as f:
                    config = yaml.safe_load(f)
                    return config.get('authenticated_curl', '')
            except:
                pass
        return ''
    
    def execute(self):
        """Execute the download process"""
        if not self.prepare_select():
            return
        
        # Build chain of responsibility
        download_handler = Download()
        sort_image_handler = SortImage()
        create_pdf_handler = CreatePdf()
        add_bookmark_handler = AddBookmark()
        print_finish_tips_handler = PrintFinishTips()
        success_print_handler = SuccessPrint()
        
        # Link handlers
        download_handler.set_next(sort_image_handler)
        sort_image_handler.set_next(create_pdf_handler)
        create_pdf_handler.set_next(add_bookmark_handler)
        add_bookmark_handler.set_next(print_finish_tips_handler)
        print_finish_tips_handler.set_next(success_print_handler)
        
        # Start the chain
        download_handler.handle_request(None, self)
