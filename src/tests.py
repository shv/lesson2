import unittest
import app as tested_app
import json

class FlaskAppTest(unittest.TestCase):
    def setUp(self) -> None:
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_success(self):
        r = self.app.get('/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'')
