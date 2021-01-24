import BinanceExchange
import CoinbaseExchange
import numpy as np

import os
import env
class Exchanges(object):

	def __init__(self):
		if os.getenv("using_Coinbase") == "True":
			self.Coinbase = CoinbaseExchange.CoinbaseExchange()
		if os.getenv("using_Binance") == "True":
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
		