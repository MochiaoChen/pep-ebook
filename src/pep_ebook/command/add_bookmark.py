"""Add bookmarks to PDF handler"""

import pikepdf

from ..command.chain import Chain
from ..bookmark import BOOKMARKS


class AddBookmark(Chain):
    """Add bookmarks handler in the chain"""
    
    def can_handle(self, context, downloader) -> bool:
        """Check if bookmark addition can proceed"""
        return downloader.error is None and len(downloader.pdf_bookmark) > 0
    
    def handle_request(self, context, downloader):
        """Add bookmarks to PDF files"""
        if not self.can_handle(context, downloader):
            if self._next_handler:
                self._next_handler.handle_request(context, downloader)
            return
        
        for key, pdf_path in downloader.pdf_bookmark.items():
            # Build the bookmark key
            bookmark_key = downloader.path_key
            if key:
                bookmark_key = f"{downloader.path_key}/{key}"
            
            # Check if we have bookmarks for this PDF
            if bookmark_key not in BOOKMARKS:
                print(f"没有找到书签数据: {bookmark_key}")
                downloader.fail[key] = pdf_path
                continue
            
            bookmarks = BOOKMARKS[bookmark_key]
            
            if not bookmarks:
                print(f"书签数据为空: {bookmark_key}")
                downloader.fail[key] = pdf_path
                continue
            
            try:
                # Open PDF with pikepdf
                pdf = pikepdf.open(pdf_path)
                
                # Add bookmarks (outline)
                # Note: This is a simplified version
                # The full implementation would recursively add nested bookmarks
                with pdf.open_outline() as outline:
                    for bookmark in bookmarks:
                        outline.root.append(
                            pikepdf.OutlineItem(
                                bookmark.title,
                                bookmark.page - 1  # pikepdf uses 0-based indexing
                            )
                        )
                
                # Save PDF with bookmarks
                pdf.save(pdf_path)
                pdf.close()
                
                print(f"书签添加完成: {pdf_path}")
                downloader.success[key] = pdf_path
                
            except Exception as e:
                print(f"添加书签失败: {str(e)}")
                downloader.fail[key] = pdf_path
        
        # Call next handler
        if self._next_handler:
            self._next_handler.handle_request(context, downloader)
