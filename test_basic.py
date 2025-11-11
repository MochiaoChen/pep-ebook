#!/usr/bin/env python3
"""Test script for pep-ebook functionality"""

import sys
sys.path.insert(0, 'src')

from pep_ebook.command.download import parse_curl, make_book_url
from pep_ebook.classification import PATHS, PERIODS

def test_curl_parsing():
    """Test curl parsing functionality"""
    test_curl = """curl 'https://book.pep.com.cn/1321001101121/files/mobile/1.jpg' -H 'User-Agent: Mozilla/5.0' -H 'Referer: https://book.pep.com.cn/1321001101121/'"""
    
    try:
        data = parse_curl(test_curl)
        print('✅ Curl parsing works')
        print(f'  Page URL format: {data.page_url_format}')
        print(f'  Headers count: {len(data.headers)}')
        return True
    except Exception as e:
        print(f'❌ Curl parsing error: {e}')
        return False

def test_book_url():
    """Test book URL generation"""
    book_id = "1321001101121"
    url = make_book_url(book_id)
    expected = f"https://book.pep.com.cn/{book_id}/mobile/index.html"
    
    if url == expected:
        print('✅ Book URL generation works')
        print(f'  URL: {url}')
        return True
    else:
        print(f'❌ Book URL generation failed')
        print(f'  Expected: {expected}')
        print(f'  Got: {url}')
        return False

def test_classification():
    """Test classification data"""
    print('✅ Classification data loaded')
    print(f'  Periods: {PERIODS}')
    print(f'  Total paths: {len(PATHS)}')
    print(f'  Sample path keys: {list(PATHS.keys())[:3]}')
    return True

def main():
    """Run all tests"""
    print("Running pep-ebook tests...\n")
    
    tests = [
        test_classification,
        test_book_url,
        test_curl_parsing,
    ]
    
    results = [test() for test in tests]
    
    print("\n" + "="*50)
    passed = sum(results)
    total = len(results)
    print(f"Tests: {passed}/{total} passed")
    print("="*50)
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
