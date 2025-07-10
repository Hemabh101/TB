import yfinance as yf
import pandas as pd

# Download BTC-USD data with Adj Close included
btc = yf.download('BTC-USD', start='2023-01-01', end='2023-12-31', auto_adjust=False)

btc.reset_index(inplace=True)

# Reorder columns safely: check if 'Adj Close' exists before selection
columns_needed = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
btc = btc[[col for col in columns_needed if col in btc.columns]]

btc.to_csv('BTC_2023.csv', index=False)

print("BTC data downloaded and saved as BTC_2023.csv in desired format.")
print(btc.head())
