"""Setup configuration for pep-ebook"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pep-ebook",
    version="1.0.0",
    author="Mochiao Chen",
    author_email="",
    description="自动下载带书签(人民教育出版社)的电子书",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MochiaoChen/pep-ebook",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.1.0",
        "requests>=2.31.0",
        "PyPDF2>=3.0.0",
        "pikepdf>=8.0.0",
        "Pillow>=10.0.0",
        "pyyaml>=6.0",
        "questionary>=2.0.0",
    ],
    entry_points={
        "console_scripts": [
            "pep-ebook=pep_ebook.cli:cli",
        ],
    },
)
