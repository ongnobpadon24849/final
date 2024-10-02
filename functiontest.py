import unittest
import json
from flask import Flask
from api_code.api_app import api_app

print("Testing the API...")
class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.tester = api_app.test_client()

    def test_x_is_1(self):
        response = self.tester.get('/mul5/1')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', data)
        self.assertEqual(data.get('result'), '5')
        print(f"Test(/mul5/1) ==> Response: {data}")

    def test_x_is_neg10(self):
        response = self.tester.get('/mul5/-10') 
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', data)
        self.assertEqual(data.get('result'), '-50')
        print(f"Test(/mul5/-10) ==> Response: {data}")

    def test_x_is_1dot5(self):
        response = self.tester.get('/mul5/1.5')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', data)
        self.assertEqual(data.get('result'), '7.5')
        print(f"Test(/mul5/1.5) ==> Response: {data}")

if __name__ == '__main__':
    unittest.main()
