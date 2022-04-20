import json
import pytest
import unittest

import src.app as tested_app
from src.task1 import URLConverter


@pytest.mark.parametrize(
    "url, keyword, result_url",
    [
        ("http://looooong.com/somepath",
         "MY-NEW-WS",
         "http://short.com/MY-NEW-WS"),
    ]
)
def test_addUrl_and_getUrl_success(url, keyword, result_url):
    converter = URLConverter()
    result = converter.addUrl(url, keyword)
    assert result == result_url
    source_url = converter.getUrl(result)
    assert source_url == url


class FlaskAppTEst(unittest.TestCase):
    def setUp(self) -> None:
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_hello_endpoint(self):
        r = self.app.get('/')
        self.assertEqual(r.data, b'Hello world')

    def test_post_hello_endpoint(self):
        r = self.app.post('/')
        self.assertEqual(r.status_code, 405)


"""
1. Shorten URL "SEO"
Given as input a URL and a SEO keyword with a max length of 20 characters,
chosen by the user, generate a SEO URL.

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
