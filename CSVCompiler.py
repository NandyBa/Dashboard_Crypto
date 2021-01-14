import pandas as pd
import CoinbaseExchange

class CSVCompiler():
    def compilecsv(self, exchanges = [], file = "summary_crypto.csv"):
        Coinbase = pd.Series(dtype='int', name="Coinbase")
        if("Coinbase" in exchanges):
            c = CoinbaseExchange.CoinbaseExchange()
            CoinbaseBalances  = c.get_balances()
            
            for balance in CoinbaseBalances:
                Coinbase[balance["currency"]] = balance["amount"]
        
        
        df = pd.DataFrame({ "Coinbase": Coinbase})
        df.to_csv(file,sep=';',index=True)