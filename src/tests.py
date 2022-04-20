import pytest
import unittest
from .task1 import URLConverter


@pytest.mark.parametrize(
    "url, keyword, result_url",
    [
        ("http://looooong.com/somepath", "MY-NEW-WS", "http://short.com/MY-NEW-WS"),
        # ("http://looooong.com/somepath", "MY-NEW-WS", "http://short.com/MY-NEW-WS"),
        # ("http://looooong.com/somepath", "MY-NEW-WS", "http://short.com/MY-NEW-WS"),
    ]
)
def test_addUrl_and_getUrl_success(url, keyword, result_url):
    converter = URLConverter()
    result = converter.addUrl(url, keyword)
    assert result == result_url
    source_url = converter.getUrl(result)
    assert source_url == url


"""
1. Shorten URL "SEO"
Given as input a URL and a SEO keyword with a max length of 20 characters, chosen by the user, generate a SEO URL.

Examples:


Input:
URL: http://looooong.com/somepath 
SEO keyword: MY-NEW-WS

Output: 
URL: http://short.com/MY-NEW-WS

Input:
URL: http://looooong.com/somepath 
SEO keyword: POTATO

Output: 
URL: http://short.com/POTATO

"""