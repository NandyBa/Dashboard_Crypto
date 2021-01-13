import unittest
import os
import config

class TestConfig(unittest.TestCase):

    def test_check_presence_of_Binance_API_Key(self):
        key = os.getenv('Binance_API_Key')
        self.assertIsNotNone(key)
        self.assertIsNot(key, "")

    def test_check_presence_of_Binance_API_Secret(self):
        key = os.getenv('Binance_API_Secret')
        self.assertIsNotNone(key)
        self.assertIsNot(key, "")

if __name__ == '__main__':
    unittest.main()