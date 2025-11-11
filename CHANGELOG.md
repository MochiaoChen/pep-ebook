# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2025-11-10

### Added
- Complete Python rewrite of the original Go project (maogou/pep-ebook)
- Chain of Responsibility design pattern implementation
- Interactive CLI using Questionary library
- PDF generation from downloaded images using Pillow
- Bookmark support structure using pikepdf
- YAML configuration file support
- Download command with curl parsing
- Upgrade command
- Comprehensive README and documentation
- Development guide (DEVELOPMENT.md)
- Basic test suite
- Example configuration file

### Features
- Download textbooks from People's Education Press (人民教育出版社)
- Support for multiple education levels: Elementary, Middle, and High School
- Support for multiple subjects: Math, Chinese, English, etc.
- Automatic PDF creation from downloaded images
- Bookmark addition to PDF files (structure ready, bookmark data to be populated)
- Interactive selection of period, grade, and subject
- Configuration file support for storing authenticated curl requests

### Technical Details
- Python 3.8+ support
- Click for CLI framework
- Requests for HTTP operations
- Pillow for image processing
- pikepdf for PDF manipulation
- PyYAML for configuration parsing
- Questionary for interactive prompts

### Documentation
- Comprehensive README.md with installation and usage instructions
- DEVELOPMENT.md with architecture details and contribution guide
- Example configuration file
- Inline code documentation and docstrings
- Basic test coverage

### Migration from Go
- Maintained the same design patterns and architecture
- Kept the same command structure (download, upgrade)
- Preserved the catalog data structure
- Implemented the same chain of responsibility pattern
- Compatible with the same workflow and user experience

[1.0.0]: https://github.com/MochiaoChen/pep-ebook/releases/tag/v1.0.0
