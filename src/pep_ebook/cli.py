"""Main CLI entry point for pep-ebook"""

import click

from .constant import LOGO, VERSION
from .command.downloader import Downloader
from .command.upgrade import upgrade


@click.group()
@click.version_option(version=VERSION, prog_name="pep-ebook")
def cli():
    """pep-ebook — 自动下载带书签(人民教育出版社)的电子书"""
    click.echo(LOGO)


@cli.command()
def download():
    """自动下载具体学科带书签的电子书"""
    downloader = Downloader()
    downloader.execute()


@cli.command()
def upgrade_cmd():
    """升级 pep-ebook 到最新版本"""
    upgrade()


if __name__ == "__main__":
    cli()
