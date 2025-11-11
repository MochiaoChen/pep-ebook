"""Upgrade command implementation"""

import subprocess
import sys


def upgrade():
    """Upgrade pep-ebook to the latest version"""
    print("正在升级 pep-ebook...")
    
    try:
        # Upgrade using pip
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "--upgrade", "pep-ebook"
        ])
        print("✅ 升级成功!")
    except subprocess.CalledProcessError as e:
        print(f"❌ 升级失败: {str(e)}")
        return False
    
    return True
