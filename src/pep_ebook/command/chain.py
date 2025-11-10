"""Base chain handler for command pattern"""

from abc import ABC, abstractmethod
from typing import Optional


class Chain(ABC):
    """Base class for chain of responsibility pattern"""
    
    def __init__(self):
        self._next_handler: Optional['Chain'] = None
    
    def set_next(self, handler: 'Chain') -> 'Chain':
        """Set the next handler in the chain"""
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle_request(self, context, downloader):
        """Handle the request"""
        pass
    
    @abstractmethod
    def can_handle(self, context, downloader) -> bool:
        """Check if this handler can process the request"""
        pass
