"""Create PDF handler"""

import os
from PIL import Image

from ..command.chain import Chain
from ..constant import SAVE_PDF_DIR


class CreatePdf(Chain):
    """Create PDF handler in the chain"""
    
    def can_handle(self, context, downloader) -> bool:
        """Check if PDF creation can proceed"""
        return downloader.error is None and len(downloader.images) > 0
    
    def handle_request(self, context, downloader):
        """Create PDF from sorted images"""
        if not self.can_handle(context, downloader):
            if self._next_handler:
                self._next_handler.handle_request(context, downloader)
            return
        
        # Create PDF directory
        pdf_dir = os.path.join(SAVE_PDF_DIR, downloader.path_key)
        os.makedirs(pdf_dir, exist_ok=True)
        
        for key, images in downloader.images.items():
            if not images:
                continue
            
            # Prepare PDF filename
            if key:
                pdf_filename = os.path.join(pdf_dir, f"{key}.pdf")
            else:
                pdf_filename = os.path.join(pdf_dir, f"{downloader.subject}.pdf")
            
            try:
                # Open all images
                image_list = []
                first_image = None
                
                for img_path in images:
                    img = Image.open(img_path)
                    # Convert to RGB if necessary
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    if first_image is None:
                        first_image = img
                    else:
                        image_list.append(img)
                
                # Save as PDF
                if first_image:
                    if image_list:
                        first_image.save(
                            pdf_filename,
                            save_all=True,
                            append_images=image_list,
                            resolution=100.0,
                            quality=95,
                            optimize=False
                        )
                    else:
                        first_image.save(pdf_filename)
                    
                    print(f"PDF创建完成: {pdf_filename}")
                    downloader.pdf_bookmark[key] = pdf_filename
                
            except Exception as e:
                downloader.error = f"创建PDF失败: {str(e)}"
                return
        
        # Call next handler
        if self._next_handler:
            self._next_handler.handle_request(context, downloader)
