import yfinance as yf

data = yf.download("AARTIDRUGS.NS RELIANCE.NS", start="2020-08-15", end="2020-08-23")
data = data.transpose()
print(data)