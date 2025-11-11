"""Success print handler"""

from ..command.chain import Chain


class SuccessPrint(Chain):
    """Success print handler in the chain"""
    
    def can_handle(self, context, downloader) -> bool:
        """Always can handle"""
        return True
    
    def handle_request(self, context, downloader):
        """Print success message"""
        if downloader.error:
            print(f"\n❌ 错误: {downloader.error}")
        else:
            print("\n✅ 所有任务完成!")
        
        # This is the last handler, no next handler to call
