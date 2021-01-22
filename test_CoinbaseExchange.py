from unittest import TestCase, mock
import os
import CoinbaseExchange
import importlib
importlib.reload(CoinbaseExchange)



class TestConbaiseExchange(TestCase):

    @mock.patch('coinbase.wallet.client.Client.get_accounts', return_value = {"data": [
        {
          "allow_deposits": True,
          "allow_withdrawals": True,
          "balance": {
            "amount": "2.567235",
            "currency": "GRT"
          },
          "native_balance": {
            "amount": "6.25",
            "currency": "EUR"
          },
        },
        {
          "allow_deposits": True,
          "allow_withdrawals": True,
          "balance": {
            "amount": "0.00000000",
            "currency": "BAND"
          },
          "native_balance": {
            "amount": "0.00",
            "currency": "EUR"
          },
        },
        {
          "balance": {
            "amount": "0.175864",
            "currency": "ALGO"
          },
          "native_balance": {
            "amount": "0.85",
            "currency": "EUR"
          },
        }
    ]})
    def test_get_balances(self, mock_get_account):
        c = CoinbaseExchange.CoinbaseExchange()
        self.assertEqual(c.get_balances(), [
             {"amount":2.567235, "currency":"GRT"},
             {"amount":0.175864, "currency":"ALGO"}
            ])
        


if __name__ == '__main__':
    unittest.main()
