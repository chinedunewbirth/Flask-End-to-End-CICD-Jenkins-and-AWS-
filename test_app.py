# test_app.py
import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        # Set up test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.app.get('/')
        self.assertIn(b'Hello from Flask CI/CD!', response.data)

if __name__ == '__main__':
    unittest.main()
