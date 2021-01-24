import os
try:
	load_dotenv('.env')
	Coinbas_api_key = os.environ["Coinbase_API_Key"]
except Exception as e:
	raise e
print("test passed")