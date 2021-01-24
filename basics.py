import os
try:
	Coinbase_api_key = os.environ["Coinbase_API_Key"]
	if Coinbase_api_key == "":
		raise Exception()
except Exception as e:
	raise e
print("test passed")