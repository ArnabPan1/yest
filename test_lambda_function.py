import unittest
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    def test_lambda_function(self):
        event = {}
        context = {}
        response = lambda_handler(event, context)
        self.assertEqual(response['statusCode'], 200)
        self.assertIn('Hello from Arnab Lambda', response['body'])

if __name__ == '__main__':
    "Run the tests"
    unittest.main()
