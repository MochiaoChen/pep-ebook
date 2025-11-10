# pep-ebook — 自动下载带书签(人民教育出版社)的电子书

这是 [maogou/pep-ebook](https://github.com/maogou/pep-ebook) 项目的 Python 重写版本。

## 项目介绍

这是一个用于自动下载人民教育出版社电子教材并添加书签的命令行工具。

### 为什么写这个项目
  
- 如果你的孩子正在上初中,那么你就不可避免给孩子辅导作业,但是你每天辛苦工作根本没有时间拿着孩子的教材先看一遍老师今天讲的课本内容,所有只能抽取零碎的时间(例如上厕所,坐公交)去看对应的教材,我本来在网上已经找到了对应的对应教材的pdf文件,但是所有的pdf文件都没有书签,导致每次找东西都要把pdf文件从头翻一遍,所以就有了这个项目
- 如果你或者你的孩子不是自媒体短视频的从业者,那么建议你或者你的孩子远离短视频软件,它的危害真的很大

## 功能特性

- ✅ 自动下载人民教育出版社电子教材
- ✅ 自动为PDF添加书签
- ✅ 支持小学、初中、高中多个学段
- ✅ 支持数学等多个学科
- ✅ 交互式命令行界面
- ✅ 使用责任链设计模式

## 安装

### 从源码安装

```bash
# 克隆仓库
git clone https://github.com/MochiaoChen/pep-ebook.git
cd pep-ebook

# 安装依赖
pip install -r requirements.txt

# 安装包
pip install -e .
```

### 使用 pip 安装 (待发布)

```bash
pip install pep-ebook
```

## 使用方法

### 查看帮助

```bash
pep-ebook --help
```

### 下载电子教材

```bash
pep-ebook download
```

按照提示选择学段、年级、学科等信息，然后输入认证请求即可开始下载。

### 升级到最新版本

```bash
pep-ebook upgrade
```

## 如何获取认证请求

1. 访问电子教材主页 
   进入[人民教育出版社电子教材平台](https://jc.pep.com.cn/)，按顺序选择：学段 → 学科 → 年级 → 点击具体教材封面进入电子版页面

2. 捕获认证请求
   - 按 F12 打开浏览器开发者工具
   - 切换到「Network」选项卡 → 在筛选框输入「jpg」
   - 多次点击下一页，直到出现携带认证的图片请求
   - 在出现的图片请求上右键 → 「Copy」→ 「Copy as cURL」

## 配置文件

你可以在 `config/pep-ebook.yaml` 中保存认证请求，以避免每次都要输入：

```yaml
# 开启调试日志（可选）
debug: true

# 保存的认证请求（可选）
authenticated_curl: "curl 'https://...' -H '...'"
```

## 项目结构

```
pep-ebook/
├── src/
│   └── pep_ebook/
│       ├── __init__.py
│       ├── cli.py              # CLI入口
│       ├── constant.py         # 常量定义
│       ├── classification.py   # 教材分类数据
│       ├── bookmark/           # 书签数据
│       │   └── __init__.py
│       └── command/            # 命令实现
│           ├── chain.py        # 责任链基类
│           ├── download.py     # 下载处理器
│           ├── sort_image.py   # 排序处理器
│           ├── create_pdf.py   # PDF创建处理器
│           ├── add_bookmark.py # 书签添加处理器
│           ├── print_finish_tips.py
│           ├── success_print.py
│           ├── downloader.py   # 下载命令
│           └── upgrade.py      # 升级命令
├── main.py                     # 主入口
├── setup.py                    # 安装配置
├── requirements.txt            # 依赖列表
├── README.md                   # 项目说明
└── LICENSE                     # 许可证
```

## 技术栈

- **Python 3.8+**: 主要编程语言
- **Click**: 命令行界面框架
- **Questionary**: 交互式命令行提示
- **Requests**: HTTP 请求库
- **Pillow**: 图像处理库
- **pikepdf**: PDF 操作库
- **PyYAML**: YAML 配置文件解析

## 设计模式

本项目使用了**责任链设计模式**（Chain of Responsibility Pattern）来处理下载、排序、PDF生成、书签添加等一系列操作。

## TODO LIST

- [x] 重写 Go 项目为 Python
- [x] 实现基本的下载功能
- [x] 实现 PDF 生成功能
- [x] 实现书签添加功能
- [ ] 完善所有学科的书签数据
- [ ] 并发下载支持
- [ ] 自动更新书签算法
- [ ] 各学科访问URL自动维护
- [ ] 重复下载检测

## 贡献

如果您发现任何问题或有任何改进意见，请随时提出 issue 或提交 pull request。我非常欢迎您的贡献！

## 许可证

本项目根据 MIT 许可证发布。详见 [LICENSE](LICENSE) 文件。

## 免责声明

本代码仅用于学习，下载后请勿用于商业用途。如果对出版社造成任何影响，与本人无关！

## 致谢

本项目是基于 [maogou/pep-ebook](https://github.com/maogou/pep-ebook) 的 Python 重写版本，感谢原作者的贡献。
