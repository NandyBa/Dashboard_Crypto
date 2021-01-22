from unittest import TestCase, mock
import os
import BinanceExchange
import importlib
importlib.reload(BinanceExchange)



class TestBinanceExchange(TestCase):

    @mock.patch('binance.client.Client.get_account', return_value = {'makerCommission': 10, 'takerCommission': 10, 'buyerCommission': 0, 
        'sellerCommission': 0, 'canTrade': True, 'canWithdraw': True, 'canDeposit': True,
         'updateTime': 1610525165262, 'accountType': 'MARGIN', 
         'balances': [
             {'asset': 'BTC', 'free': '0.00000856', 'locked': '0.00000013'},
             {'asset': 'LTC', 'free': '0.00000000', 'locked': '0.17000000'},
             {'asset': 'ETH', 'free': '0.56000000', 'locked': '0.00000000'},
             {'asset': 'NEO', 'free': '0.00000000', 'locked': '0.00000000'},
             {'asset': 'BNB', 'free': '0.00000000', 'locked': '0.00000000'},
             {'asset': 'QTUM', 'free': '0.00000000', 'locked': '0.00000000'},
             {'asset': 'EOS', 'free': '3.00000000', 'locked': '0.00000000'},
             {'asset': 'SNT', 'free': '0.00000000', 'locked': '0.00000000'},
             {'asset': 'BNT', 'free': '0.00000000', 'locked': '0.00000000'},
             {'asset': 'GAS', 'free': '0.00000000', 'locked': '0.00000000'}
            ]
        })
    def test_get_balances(self, mock_get_account):
        b = BinanceExchange.BinanceExchange()
        self.assertEqual(b.get_balances(), [
             {'asset': 'BTC', 'free': 0.00000856, 'locked': 0.00000013},
             {'asset': 'LTC', 'free': 0.00000000, 'locked': 0.17000000},
             {'asset': 'ETH', 'free': 0.56000000, 'locked': 0.00000000},
             {'asset': 'EOS', 'free': 3.00000000, 'locked': 0.00000000}
            ])
        

if __name__ == '__main__':
    unittest.main()
