# -*- coding: utf-8 -*-
import unittest
import json
import requests
from app import app


class GenerateTextTestCase(unittest.TestCase):
    """
    Test cases for the generate_text endpoint.
    """
    def setUp(self):
        """
        Setup the test environment.
        """
        self.app = app.test_client()

    def test_generate_text_success(self):
        """
        Test that the endpoint returns a 200 status code and generates text successfully.
        """
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "emotion": "funny",
            "prompt": "This is a test prompt."
        }
        response = self.app.post("/gpt3", headers=headers, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) > 0)

    def test_generate_text_failure(self):
        """
        Test that the endpoint returns a 500 status code when an error occurs.
        """
        headers = {
            "Content-Type": "application/json"
        }
        response = self.app.post("/gpt3", headers=headers)
        self.assertEqual(response.status_code, 500)

if __name__ == "__main__":
    unittest.main()
