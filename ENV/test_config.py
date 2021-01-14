import unittest
import os
import config
from binance.client import Client

class TestConfig(unittest.TestCase):

    def test_check_presence_of_Binance_API_Key(self):
        key = os.getenv('Binance_API_Key')
        self.assertIsNotNone(key)
        self.assertIsNot(key, "")

    def test_check_presence_of_Binance_API_Secret(self):
        key = os.getenv('Binance_API_Secret')
        self.assertIsNotNone(key)
        self.assertIsNot(key, "")

    def test_check_Binance_valid_credentials(self):
        error_raised = False

        api_key = os.getenv('Binance_API_Key')
        api_secret = os.getenv('Binance_API_Secret')

        try:
            client = Client(api_key, api_secret, {"verify": True, "timeout": 20})
            client.get_all_orders(symbol='BNBBTC', limit=1)
        except:
            error_raised = True
        self.assertFalse(error_raised, "Invalid Bianance credentials")

    def test_check_presence_of_Coinbase_API_Key(self):
        key = os.getenv('Coinbase_API_Key')
        self.assertIsNotNone(key)
        self.assertIsNot(key, "")

    def test_check_presence_of_Coinbase_API_Secret(self):
        key = os.getenv('Coinbase_API_Secret')
        self.assertIsNotNone(key)
        self.assertIsNot(key, "")

if __name__ == '__main__':
    unittest.main()