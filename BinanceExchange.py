import os
import env
from binance.client import Client

class BinanceExchange():

	def __init__(self):
		self.CLIENT = Client(os.getenv('Binance_API_Key'), os.getenv('Binance_API_Secret'), {"verify": True, "timeout": 20})

	def get_balances(self):
		balances = []
		info = self.CLIENT.get_account()
		for asset in info['balances']:
			if float(asset['free']) != 0 or float(asset['locked']) != 0:
				balances.append({'asset': asset['asset'], 'free': float(asset['free']), 'locked': float(asset['locked'])})
		return balances

	def get_Price(self, asset, currency = 'USDT'):
		if asset == "BETH":
			asset = "ETH" #to return price of ETH for ETH(2.0) stacking
		try:
			price = float( self.CLIENT.get_avg_price(symbol=asset+currency)['price'] )
		except:
			try:
				if(asset == "USDT"):
					price = 1
				else:
					price = float( self.CLIENT.get_avg_price(symbol=asset+'USDT')['price'] )
			except:
				raise Exception()
			else:
			    price = price / float( self.CLIENT.get_avg_price(symbol=currency+'USDT')['price'] )
		return price
