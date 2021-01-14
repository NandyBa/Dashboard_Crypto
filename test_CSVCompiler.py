from unittest import TestCase, mock
import CSVCompiler
import os

class TestCSVCompiler(TestCase):

    def compilecsv(self, exchanges, file = "summary_crypto.csv"):
        return CSVCompiler.CSVCompiler().compilecsv(exchanges, file)

    @mock.patch('CoinbaseExchange.CoinbaseExchange.get_balances', return_value = [
        {"amount":3, "currency":"BTC"},
        {"amount":2.45553, "currency":"ETH"}
    ])
    def test_Coinbase_compile(self, mock_get_balances):
        self.compilecsv(["Coinbase"], "testcompiler.csv")
        with open('testcompiler.csv', "r") as csvfile:
	        i = 0
	        for row in csvfile:
	            elems = row.replace("\n","").split(";")
	            if i == 0:
	                try:
	                    iCoinbaseAmount = elems.index("Coinbase")
	                except:
	                    raise ValueError("Error in the Coinbase compiler output")
	            else:
	                if(elems[0] == "BTC"):
	                	self.assertEqual(float(elems[iCoinbaseAmount]), 3)
	                elif(elems[0] == "ETH"):
	                	self.assertEqual(float(elems[iCoinbaseAmount]), 2.45553)
	            i += 1
        os.remove('testcompiler.csv')


if __name__ == '__main__':
    unittest.main()