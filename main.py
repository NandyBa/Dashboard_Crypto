import os
import env
from CSVCompiler import CSVCompiler

compiler = CSVCompiler()
exchanges = []

if os.getenv("using_Binance") == "True":
	exchanges.append("Binance")

if os.getenv("using_Coinbase") == "True":
	exchanges.append("Coinbase")


if len(exchanges) > 0:
	compiler.compilecsv(exchanges)
	compiler.compile_financial_statement()
