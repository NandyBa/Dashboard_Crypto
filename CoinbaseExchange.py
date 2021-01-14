import os
import sys
sys.path.append("ENV")
import config

from coinbase.wallet.client import Client

class CoinbaseExchange():

	def __init__(self):
		self.CLIENT = Client(os.environ["Coinbase_API_Key"], os.environ["Coinbase_API_Secret"])

	def get_balances(self):
		balances = []
		info = self.CLIENT.get_accounts()
		for asset in info['data']:
			if float(asset['balance']['amount']) != 0:
				balance = {
					"amount": float(asset['balance']['amount']),
					"currency":asset['balance']['currency']
				}
				balances.append(balance)
		return balances
