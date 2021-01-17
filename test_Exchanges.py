from unittest import TestCase, mock
import Exchanges
import importlib
importlib.reload(Exchanges)



class TestExchanges(TestCase):

    ###
    # Test asset available only at Conbaise
    #
    ###
    @mock.patch('coinbase.wallet.client.Client.get_buy_price', return_value = {
      "amount": "30318.06",
      "base": "BTC",
      "currency": "EUR"
    })
    @mock.patch('binance.client.Client.get_avg_price', return_value = [

        Exception(),
        Exception()
    ])
    def test_get_Price_asset_available_only_at_Coinbase(self, mock_coinbase_get_buy_price, mock_binance_get_buy_price):
        e = Exchanges.Exchanges()
        self.assertEqual(e.get_Price("BTC","EUR"), 30318.06)




    ###
    # Test asset available only at Binance and direct market between asset and the requested currency exist
    #
    ###
    @mock.patch('coinbase.wallet.client.Client.get_buy_price', return_value = Exception())
    @mock.patch('binance.client.Client.get_avg_price', return_value = {
          'mins': 5, 'price': 30096.12
    })
    def test_get_Price_asset_available_only_at_Binance_directly_market(self, mock_coinbase_get_buy_price, mock_binance_get_buy_price):
        e = Exchanges.Exchanges()
        self.assertEqual(e.get_Price("BTC","EUR"), 30096.12)



    ###
    # Test asset available only at Binance and direct market between asset and the requested currency not exist
    #
    ###
    @mock.patch('coinbase.wallet.client.Client.get_buy_price', return_value = Exception())
    @mock.patch('binance.client.Client.get_avg_price', side_effect=[

        Exception(),
        {
          'mins': 5, 'price': 9
        },
        {
          'mins': 5, 'price': 1.5
        }
    ])
    def test_get_Price_asset_available_only_at_Binance_undirectly_market(self, mock_coinbase_get_buy_price, mock_binance_get_buy_prices):
        e = Exchanges.Exchanges()
        self.assertEqual(e.get_Price("SNX","EUR"), 6)

    ###
    # Test asset available at Coinbase and Binance
    #
    ###
    @mock.patch('coinbase.wallet.client.Client.get_buy_price', return_value = {
      "amount": "30318.06",
      "base": "BTC",
      "currency": "EUR"
    })
    @mock.patch('binance.client.Client.get_avg_price', return_value = {
      'mins': 5, 'price': '30096.12'
    })
    def test_get_Price_asset_available_at_all(self, mock_coinbase_get_buy_price, mock_binance_get_buy_price):
        e = Exchanges.Exchanges()
        self.assertEqual(e.get_Price("BTC","EUR"), 30207.09)
        


if __name__ == '__main__':
    unittest.main()
