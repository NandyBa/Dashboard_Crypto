import BinanceExchange
import CoinbaseExchange
import numpy as np

class Exchanges(object):

	def __init__(self):
		self.Coinbase = CoinbaseExchange.CoinbaseExchange()
		self.Binance = BinanceExchange.BinanceExchange()

	def get_Price(self, asset, currency):
		prices = []
		try:
			prices.append(self.Coinbase.get_Price(asset, currency))
		except:
			pass
		
		try:
			prices.append(self.Binance.get_Price(asset, currency))
		except:
			pass

		if len(prices) >= 1:
			mean_price = np.mean(prices)
		else:
			raise Exception(f"No price found for {asset}-{currency}")
		return mean_price
		