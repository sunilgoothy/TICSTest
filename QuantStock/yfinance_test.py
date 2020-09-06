import yfinance as yf

data = yf.download("AARTIDRUGS.NS RELIANCE.NS", start="2019-09-04", end="2019-09-05")
data = data.transpose()
print(data)