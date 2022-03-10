
import yfinance as yf
import pandas as pd
from datetime import datetime

#https://finance.yahoo.com/cryptocurrencies?guccounter=1
#https://www.youtube.com/watch?v=x58MJUVNKMg <- fuente
#moedas disponibles

start = datetime(2013,1,1)
end = datetime.now().date().isoformat()
symbol = 'BTC-USD'

df = yf.download(symbol, start=start, end = end)

print(df.head(20))
print(len(df), 'holaaaaaaaaaa')
