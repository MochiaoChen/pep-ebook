"""Sort images handler"""

from ..command.chain import Chain


class SortImage(Chain):
    """Sort images handler in the chain"""
    
    def can_handle(self, context, downloader) -> bool:
        """Check if sorting can proceed"""
        return downloader.error is None and len(downloader.images) > 0
    
    def handle_request(self, context, downloader):
        """Sort images by filename"""
        if not self.can_handle(context, downloader):
            if self._next_handler:
                self._next_handler.handle_request(context, downloader)
            return
        
        # Images are already sorted by download order (1.jpg, 2.jpg, ...)
        # Just ensure they're in correct order
        for key, images in downloader.images.items():
            downloader.images[key] = sorted(images, key=lambda x: int(x.split('/')[-1].replace('.jpg', '')))
        
        print("图片排序完成")
        
        # Call next handler
        if self._next_handler:
            self._next_handler.handle_request(context, downloader)
