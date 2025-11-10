"""Classification and catalog data for educational materials"""

from typing import Dict, List, NamedTuple


class UrlPath(NamedTuple):
    """URL path information for a textbook"""
    book_id: str
    pages: int
    remark: str = ""


# Periods/Stages
PERIODS = ["小学", "初中", "高中"]

# Grades by period
GRADES = {
    "小学": ["一年级", "二年级", "三年级", "四年级", "五年级", "六年级"],
    "初中": ["七年级", "八年级", "九年级"],
    "高中": ["必修", "选择性必修"],
}

# Subjects by period
SUBJECTS = {
    "小学": ["语文", "数学", "英语", "科学", "道德与法治", "音乐", "美术", "体育与健康", "习近平新时代中国特色社会主义思想学生读本"],
    "初中": ["语文", "数学", "英语", "物理", "化学", "生物", "道德与法治", "历史", "地理", "习近平新时代中国特色社会主义思想学生读本"],
    "高中": ["语文", "数学", "英语", "物理", "化学", "生物", "思想政治", "历史", "地理", "习近平新时代中国特色社会主义思想学生读本"],
}

# High school must or not options
HIGH_MUST_OR_NOT = {
    "数学-必修": ["第一册", "第二册", "第三册", "第四册"],
    "数学-选择性必修": ["第一册", "第二册", "第三册"],
}

# Paths mapping
PATHS: Dict[str, List[UrlPath]] = {
    "小学-三年级-习近平新时代中国特色社会主义思想学生读本": [
        UrlPath(book_id="1291001103221", pages=2),
    ],
    "小学-五年级-习近平新时代中国特色社会主义思想学生读本": [
        UrlPath(book_id="1291001403221", pages=102),
    ],
    "小学-一年级-道德与法治": [
        UrlPath(book_id="1284001101161", pages=78, remark="上册"),
        UrlPath(book_id="1284001102161", pages=80, remark="下册"),
    ],
    "小学-一年级-语文": [
        UrlPath(book_id="1211001101161", pages=128, remark="上册"),
        UrlPath(book_id="1211001102161", pages=128, remark="下册"),
    ],
    "小学-一年级-数学": [
        UrlPath(book_id="1221001101121", pages=120, remark="上册"),
        UrlPath(book_id="1221001102121", pages=112, remark="下册"),
    ],
    "小学-一年级-英语": [
        UrlPath(book_id="1212001101123", pages=78, remark="上册"),
        UrlPath(book_id="1212001102123", pages=78, remark="下册"),
    ],
    "小学-三年级-英语": [
        UrlPath(book_id="1212001301244", pages=106, remark="上册"),
        UrlPath(book_id="1212001302244", pages=102, remark="下册"),
    ],
    "小学-一年级-科学": [
        UrlPath(book_id="1244001101171", pages=52, remark="一"),
        UrlPath(book_id="1244001102172", pages=20, remark="二"),
        UrlPath(book_id="1244001102171", pages=52, remark="三"),
    ],
    "小学-一年级-音乐": [
        UrlPath(book_id="1262001101122", pages=68, remark="一"),
        UrlPath(book_id="1262001101121", pages=68, remark="二"),
        UrlPath(book_id="1262001102122", pages=68, remark="三"),
        UrlPath(book_id="1262001102121", pages=68, remark="四"),
    ],
    "小学-一年级-体育与健康": [
        UrlPath(book_id="1272001103221", pages=344),
    ],
    "小学-一年级-美术": [
        UrlPath(book_id="1263001101121", pages=52, remark="上册"),
        UrlPath(book_id="1263001102121", pages=52, remark="下册"),
    ],
    "初中-七年级-数学": [
        UrlPath(book_id="1321001101121", pages=162, remark="上册"),
        UrlPath(book_id="1321001102121", pages=176, remark="下册"),
    ],
    "初中-八年级-数学": [
        UrlPath(book_id="1321001201131", pages=170, remark="上册"),
        UrlPath(book_id="1321001202131", pages=148, remark="下册"),
    ],
    "初中-九年级-数学": [
        UrlPath(book_id="1321001301141", pages=164, remark="上册"),
        UrlPath(book_id="1321001302141", pages=124, remark="下册"),
    ],
    "高中-必修-数学-第一册": [
        UrlPath(book_id="1421001121201", pages=152, remark="B版"),
        UrlPath(book_id="1421001121191", pages=270, remark="A版"),
    ],
    "高中-选择性必修-数学-第一册": [
        UrlPath(book_id="1421001127202", pages=192, remark="B版"),
        UrlPath(book_id="1421001127201", pages=156, remark="A版"),
    ],
    "高中-选择性必修-数学-第二册": [
        UrlPath(book_id="1421001128202", pages=140, remark="B版"),
        UrlPath(book_id="1421001128201", pages=114, remark="A版"),
    ],
    "高中-选择性必修-数学-第三册": [
        UrlPath(book_id="1421001129202", pages=126, remark="B版"),
        UrlPath(book_id="1421001129201", pages=156, remark="A版"),
    ],
    "高中-必修-数学-第二册": [
        UrlPath(book_id="1421001122201", pages=192, remark="B版"),
        UrlPath(book_id="1421001122191", pages=280, remark="A版"),
    ],
    "高中-必修-数学-第三册": [
        UrlPath(book_id="1421001123201", pages=126, remark="B版"),
    ],
    "高中-必修-数学-第四册": [
        UrlPath(book_id="1421001137201", pages=142, remark="B版"),
    ],
}
