"""Download handler for the chain of responsibility"""

import os
import re
import time
import random
from typing import Dict
from urllib.parse import urlparse

import requests

from ..command.chain import Chain
from ..constant import IMAGE_CACHE_DIR


class CurlData:
    """Data extracted from curl command"""
    
    def __init__(self):
        self.page_url_format: str = ""
        self.refer_format: str = ""
        self.headers: Dict[str, str] = {}


def make_book_url(book_id: str) -> str:
    """Generate book URL from book ID"""
    return f"https://book.pep.com.cn/{book_id}/mobile/index.html"


def parse_curl(curl: str) -> CurlData:
    """Parse curl command to extract URL and headers"""
    data = CurlData()
    
    # Extract URL
    curl_regex = re.compile(r"curl '([^']+)'")
    url_match = curl_regex.search(curl)
    if not url_match:
        raise ValueError("Invalid URL format")
    
    original_url = url_match.group(1)
    
    # Extract book_id
    book_id = ""
    book_id_regex = re.compile(r"book\.pep\.com\.cn/(\d+)")
    book_id_match = book_id_regex.search(original_url)
    if book_id_match:
        book_id = book_id_match.group(1)
    
    # Generate PageURLFormat
    url_format_regex = re.compile(r"(\d+)/files/mobile/(\d+)\.jpg")
    data.page_url_format = url_format_regex.sub(r"{}/files/mobile/{}.jpg", original_url)
    
    # Parse Headers
    header_regex = re.compile(r"-H '([^:]+):\s*([^']+)'")
    header_matches = header_regex.findall(curl)
    
    for key, value in header_matches:
        key = key.strip()
        value = value.strip().strip('"')
        data.headers[key] = value
    
    # Parse Cookie parameter
    cookie_regex = re.compile(r"-(?:-cookie|b) '([^']+)'")
    cookie_matches = cookie_regex.findall(curl)
    
    cookies = []
    if "Cookie" in data.headers:
        cookies.append(data.headers["Cookie"])
    
    for cookie_str in cookie_matches:
        cookies.append(cookie_str.strip())
    
    if cookies:
        data.headers["Cookie"] = "; ".join(cookies)
    
    # Replace Referer
    if "Referer" in data.headers:
        data.headers["Referer"] = data.headers["Referer"].replace(book_id, "{}")
    
    data.refer_format = data.headers.get("Referer", "")
    
    return data


def new_request_via_curl(curl_data: CurlData, book_id: str, page: int) -> requests.Request:
    """Create HTTP request from curl data"""
    book_url = curl_data.page_url_format.format(book_id, page)
    
    headers = curl_data.headers.copy()
    if curl_data.refer_format:
        headers["Referer"] = curl_data.refer_format.format(book_id)
    
    return requests.Request('GET', book_url, headers=headers)


class Download(Chain):
    """Download handler in the chain"""
    
    def can_handle(self, context, downloader) -> bool:
        """Check if download can proceed"""
        return downloader.error is None
    
    def handle_request(self, context, downloader):
        """Download all images for the selected textbooks"""
        if not self.can_handle(context, downloader):
            if self._next_handler:
                self._next_handler.handle_request(context, downloader)
            return
        
        print("🚨🚨🚨正在生成中请稍等.....🚨🚨🚨")
        
        curl = downloader.authenticated_curl
        try:
            curl_data = parse_curl(curl.strip())
        except Exception as e:
            downloader.error = f"解析认证请求失败: {str(e)}"
            return
        
        for item in downloader.paths:
            images = []
            path = os.path.join(
                IMAGE_CACHE_DIR,
                downloader.path_key,
                item.remark if item.remark else ""
            )
            
            os.makedirs(path, exist_ok=True)
            
            for i in range(1, item.pages + 1):
                book_id = item.book_id
                filename = os.path.join(path, f"{i}.jpg")
                
                # Check if file already exists
                if os.path.exists(filename):
                    images.append(filename)
                    continue
                
                # Create request
                req = new_request_via_curl(curl_data, book_id, i)
                
                try:
                    session = requests.Session()
                    prepared = session.prepare_request(req)
                    resp = session.send(prepared, timeout=30)
                    
                    # Check if response is an image
                    content_type = resp.headers.get('Content-Type', '')
                    if 'image' not in content_type:
                        downloader.error = f"电子书url返回{prepared.url}非图片,认证请求已过期"
                        return
                    
                    # Save image
                    with open(filename, 'wb') as f:
                        f.write(resp.content)
                    
                    images.append(filename)
                    
                    print(f"下载完成: 第 {i}/{item.pages} 页")
                    
                    # Random delay to avoid rate limiting
                    time.sleep(1 + random.randint(0, 2))
                    
                except Exception as e:
                    downloader.error = f"下载失败: {str(e)}"
                    return
            
            if images:
                key = item.remark if item.remark else downloader.subject
                downloader.images[key] = images
        
        # Call next handler
        if self._next_handler:
            self._next_handler.handle_request(context, downloader)
