from unittest import TestCase, mock
import CSVCompiler
import os
import openpyxl

class TestCSVCompiler(TestCase):

    def compilecsv(self, exchanges, file = "summary_crypto.xlsx"):
        return CSVCompiler.CSVCompiler().compilecsv(exchanges, file)

    @mock.patch('CoinbaseExchange.CoinbaseExchange.get_balances', return_value = [
        {"amount":3, "currency":"BTC"},
        {"amount":2.45553, "currency":"ETH"}
    ])
    def test_Coinbase_compile(self, mock_get_balances):
        file = "testcompiler.xlsx"
        self.compilecsv(["Coinbase"], file)

        wb_obj = openpyxl.load_workbook(file)
        sheet = wb_obj['Balances']
        i = 0
        count = 0
        for row in sheet.iter_rows():
            if i == 0:
                finded = False
                for j in range(len(row)):
                    if row[j].value == "Coinbase":
                        iCoinbaseAmount = j
                        count += 1
                if count != 1:
                    raise ValueError("Error in the Coinbase compiler output")
            else:
                if(row[0].value == "BTC"):
                    self.assertEqual(float(row[iCoinbaseAmount].value), 3)
                    count += 1
                elif(row[0].value == "ETH"):
                    self.assertEqual(float(row[iCoinbaseAmount].value), 2.45553)
                    count += 1
            i += 1
        self.assertEqual(count, 3)
        os.remove(file)

    @mock.patch('BinanceExchange.BinanceExchange.get_balances', return_value = [
        {'asset': 'BTC', 'free': 0.00000856, 'locked': 0.00000013},
        {'asset': 'LTC', 'free': 0.00000000, 'locked': 0.17000000},
        {'asset': 'LDETH', 'free': 0.56000000, 'locked': 0.00000000},
        {'asset': 'LDEOS', 'free': 3.00000000, 'locked': 0.00000000}
    ])
    def test_Binance_compile(self, mock_get_balances):
        file = "testcompiler2.xlsx"
        self.compilecsv(["Binance"], file)

        wb_obj = openpyxl.load_workbook(file)
        sheet = wb_obj['Balances']

        i = 0
        count = 0
        for row in sheet.iter_rows():
            if i == 0:
                for j in range(len(row)):
                    if row[j].value == "Binance":
                        iBinanceAmount = j
                        count += 1
                    elif row[j].value == "Binance Flexible Saving":
                        iBinanceAmountFlexibleSaving = j
                        count += 1
                if count != 2:
                    raise ValueError("Error in the Binance compiler output")
            else:
                if(row[0].value == "BTC"):
                    self.assertEqual(float(row[iBinanceAmount].value), 8.69e-06)
                    count += 1
                elif(row[0].value == "LTC"):
                    self.assertEqual(float(row[iBinanceAmount].value), 0.17)
                    count += 1
                elif(row[0].value == "ETH"):
                    self.assertEqual(float(row[iBinanceAmountFlexibleSaving].value), 0.56)
                    count += 1
                elif(row[0].value == "EOS"):
                    self.assertEqual(float(row[iBinanceAmountFlexibleSaving].value), 3)
                    count += 1
            i += 1
        self.assertEqual(count, 6)
        os.remove(file)


if __name__ == '__main__':
    unittest.main()