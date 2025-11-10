# 开发指南 (Development Guide)

## 项目架构 (Project Architecture)

本项目采用**责任链设计模式** (Chain of Responsibility Pattern) 来处理下载流程。

### 目录结构 (Directory Structure)

```
pep-ebook/
├── src/pep_ebook/          # 主要源代码
│   ├── __init__.py         # 包初始化
│   ├── cli.py              # CLI 入口点
│   ├── constant.py         # 常量定义
│   ├── classification.py   # 教材分类数据
│   ├── bookmark/           # 书签数据模块
│   │   └── __init__.py
│   └── command/            # 命令实现
│       ├── __init__.py
│       ├── chain.py        # 责任链基类
│       ├── download.py     # 下载处理器
│       ├── sort_image.py   # 图片排序处理器
│       ├── create_pdf.py   # PDF 创建处理器
│       ├── add_bookmark.py # 书签添加处理器
│       ├── print_finish_tips.py  # 完成提示
│       ├── success_print.py      # 成功打印
│       ├── downloader.py   # 下载命令
│       └── upgrade.py      # 升级命令
├── config/                 # 配置文件目录
├── main.py                 # 程序入口
├── setup.py                # 安装配置
├── requirements.txt        # 依赖列表
├── test_basic.py           # 基础测试
└── README.md               # 项目说明
```

## 责任链模式 (Chain of Responsibility Pattern)

下载流程通过一系列处理器链式处理：

```
Download → SortImage → CreatePdf → AddBookmark → PrintFinishTips → SuccessPrint
```

每个处理器：
1. 检查是否可以处理 (`can_handle`)
2. 执行自己的任务 (`handle_request`)
3. 调用下一个处理器

### 处理器说明

- **Download**: 下载图片文件
- **SortImage**: 排序图片
- **CreatePdf**: 从图片创建 PDF
- **AddBookmark**: 添加书签到 PDF
- **PrintFinishTips**: 打印完成提示
- **SuccessPrint**: 打印成功消息

## 开发环境设置 (Development Setup)

### 1. 克隆仓库

```bash
git clone https://github.com/MochiaoChen/pep-ebook.git
cd pep-ebook
```

### 2. 创建虚拟环境 (推荐)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 开发模式安装

```bash
pip install -e .
```

## 运行测试 (Running Tests)

```bash
python test_basic.py
```

## 添加新的教材 (Adding New Textbooks)

在 `src/pep_ebook/classification.py` 中添加新的路径：

```python
PATHS: Dict[str, List[UrlPath]] = {
    # ... existing paths ...
    "初中-七年级-新学科": [
        UrlPath(book_id="1234567890123", pages=100, remark="上册"),
        UrlPath(book_id="1234567890124", pages=120, remark="下册"),
    ],
}
```

## 添加书签数据 (Adding Bookmark Data)

在 `src/pep_ebook/bookmark/__init__.py` 中添加书签：

```python
from typing import List

# 定义书签
bookmarks_example: List[Bookmark] = [
    Bookmark(title="第一章", page=1, children=[
        Bookmark(title="1.1 节", page=2),
        Bookmark(title="1.2 节", page=5),
    ]),
    Bookmark(title="第二章", page=10),
]

# 添加到 BOOKMARKS 字典
BOOKMARKS["初中/七年级/新学科/上册"] = bookmarks_example
```

## 代码风格 (Code Style)

- 使用 4 个空格缩进
- 遵循 PEP 8 规范
- 添加类型注解 (type hints)
- 编写文档字符串 (docstrings)

## 调试 (Debugging)

启用调试模式，在 `config/pep-ebook.yaml` 中设置：

```yaml
debug: true
```

## 常见问题 (Common Issues)

### Q: 依赖安装失败

A: 尝试使用国内镜像源：

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

### Q: 如何获取认证请求？

A: 参考 README.md 中的"如何获取认证请求"部分

### Q: PDF 生成失败

A: 确保安装了所有图像依赖：

```bash
pip install Pillow pikepdf
```

## 贡献指南 (Contributing)

1. Fork 仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证 (License)

MIT License - 详见 LICENSE 文件
