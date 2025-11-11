"""Print completion tips handler"""

from ..command.chain import Chain


class PrintFinishTips(Chain):
    """Print finish tips handler in the chain"""
    
    def can_handle(self, context, downloader) -> bool:
        """Always can handle"""
        return True
    
    def handle_request(self, context, downloader):
        """Print completion tips"""
        print("\n" + "="*50)
        print("处理完成!")
        print("="*50)
        
        if downloader.success:
            print("\n✅ 成功生成的PDF:")
            for key, path in downloader.success.items():
                print(f"  - {key}: {path}")
        
        if downloader.fail:
            print("\n❌ 失败的PDF (可能是缺少书签数据):")
            for key, path in downloader.fail.items():
                print(f"  - {key}: {path}")
        
        print("\n" + "="*50)
        
        # Call next handler
        if self._next_handler:
            self._next_handler.handle_request(context, downloader)
