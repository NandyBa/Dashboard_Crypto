import os
try:
	_ = os.environ["travis_test"] # check if we are in Travis test environment
except:
	## env import
	from dotenv import load_dotenv
	load_dotenv('.env')
	