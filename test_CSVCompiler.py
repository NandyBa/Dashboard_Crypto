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

    @mock.patch('BinanceExchange.BinanceExchange.get_balances', return_value = [
        {'asset': 'BTC', 'free': 0.00000856, 'locked': 0.00000013},
        {'asset': 'LTC', 'free': 0.00000000, 'locked': 0.17000000},
        {'asset': 'LDETH', 'free': 0.56000000, 'locked': 0.00000000},
        {'asset': 'LDEOS', 'free': 3.00000000, 'locked': 0.00000000}
    ])
    def test_Binance_compile(self, mock_get_balances):
        self.compilecsv(["Binance"], "testcompiler2.csv")
        with open('testcompiler2.csv', "r") as csvfile:
	        i = 0
	        for row in csvfile:
	            elems = row.replace("\n","").split(";")
	            if i == 0:
	                try:
	                    iBinanceAmount = elems.index("Binance")
	                    iBinanceAmountFlexibleSaving = elems.index("Binance Flexible Saving")
	                except:
	                    raise ValueError("Error in the Binance compiler output")
	            else:
	                if(elems[0] == "BTC"):
	                	self.assertEqual(float(elems[iBinanceAmount]), 8.69e-06)
	                elif(elems[0] == "LTC"):
	                	self.assertEqual(float(elems[iBinanceAmount]), 0.17)
	                elif(elems[0] == "ETH"):
	                	self.assertEqual(float(elems[iBinanceAmountFlexibleSaving]), 0.56)
	                elif(elems[0] == "EOS"):
	                	self.assertEqual(float(elems[iBinanceAmountFlexibleSaving]), 3)
	            i += 1
        os.remove('testcompiler2.csv')


if __name__ == '__main__':
    unittest.main()