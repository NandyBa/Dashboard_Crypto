import os
import sys
sys.path.append("ENV")
import config
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
