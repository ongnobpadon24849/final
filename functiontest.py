import unittest
import json
from flask import Flask
from api_code.api_app import api_app

print("Testing the API...")
class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.tester = api_app.test_client()

    def test_x_is_3dot6(self):
        response = self.tester.get('/is1honor/3.6')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('is1honor', data)
        self.assertEqual(data.get('is1honor'), True)
        print(f"Test(/is1honor/3.6) ==> Response: {data}")

    def test_x_is_2dot0(self):
        response = self.tester.get('/is1honor/2.0')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('is1honor', data)
        self.assertEqual(data.get('is1honor'), False)
        print(f"Test(/is1honor/3.5) ==> Response: {data}")

    def test_x_is_5dot1(self):
        response = self.tester.get('/is1honor/5.1')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('ERROR', data)
        self.assertEqual(data.get('ERROR'), "Invalid input")
        print(f"Test(/is1honor/5.1) ==> Response: {data}")

if __name__ == '__main__':
    unittest.main()
