import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.client.get('/')
        self.assertIn(b'Welcome to Flask Jenkins AWS App', response.data)
        self.assertIn(b'Flask Jenkins AWS App', response.data)

if __name__ == '__main__':
    unittest.main()
