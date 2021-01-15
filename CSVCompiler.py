import pandas as pd
import CoinbaseExchange
import BinanceExchange
import xlsxwriter

class CSVCompiler():
    def compilecsv(self, exchanges = [], file = "summary_crypto.xlsx"):
        Coinbase = pd.Series(dtype='int', name="Coinbase")
        Binance = pd.Series(dtype='int', name="Binance")
        BinanceFlexibleSaving = pd.Series(dtype='int', name="BinanceEarn")
        if("Coinbase" in exchanges):
            c = CoinbaseExchange.CoinbaseExchange()
            CoinbaseBalances  = c.get_balances()
            
            for balance in CoinbaseBalances:
                Coinbase[balance["currency"]] = balance["amount"]
        if("Binance" in exchanges):
            c = BinanceExchange.BinanceExchange()
            BinanceBalances  = c.get_balances()
            
            for balance in BinanceBalances:
                if "LD" in balance["asset"][0:2]:
                    BinanceFlexibleSaving[balance["asset"].replace("LD","")] = balance["free"] + balance["locked"]
                else:
                    Binance[balance["asset"]] = balance["free"] + balance["locked"]
        
        
        df = pd.DataFrame({ "Coinbase": Coinbase,"Binance": Binance, "Binance Flexible Saving": BinanceFlexibleSaving})
        writer = pd.ExcelWriter(file, engine='xlsxwriter')
        df.to_excel(writer, sheet_name="Balances")
        writer.save()