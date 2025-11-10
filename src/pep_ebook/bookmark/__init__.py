"""Bookmark data for various textbooks"""

from typing import Dict, List, NamedTuple


class Bookmark(NamedTuple):
    """PDF bookmark structure"""
    title: str
    page: int
    children: List['Bookmark'] = []


# Placeholder bookmark data - in the original project this is extensive
# For now, we'll create the structure and add data as needed
BOOKMARKS: Dict[str, List[Bookmark]] = {
    "初中/七年级/数学/上册": [],
    "初中/七年级/数学/下册": [],
    "初中/八年级/数学/上册": [],
    "初中/八年级/数学/下册": [],
    "初中/九年级/数学/上册": [],
    "初中/九年级/数学/下册": [],
    "高中/必修/数学/第一册/B版": [],
    "高中/必修/数学/第一册/A版": [],
    "高中/必修/数学/第二册/B版": [],
    "高中/必修/数学/第二册/A版": [],
    "高中/必修/数学/第三册/B版": [],
    "高中/必修/数学/第四册/B版": [],
    "高中/选择性必修/数学/第一册/B版": [],
    "高中/选择性必修/数学/第一册/A版": [],
    "高中/选择性必修/数学/第二册/B版": [],
    "高中/选择性必修/数学/第二册/A版": [],
    "高中/选择性必修/数学/第三册/B版": [],
    "高中/选择性必修/数学/第三册/A版": [],
}
