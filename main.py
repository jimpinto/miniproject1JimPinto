### INF601 - Advanced Programming in Python
### Jim Pinto
### Mini Project 1
import pprint
import yfinance as yf

mytickers = ["MSFT", "AAPL", "GOOG", "NVDA", "AMC"]

mydata = {}


mytickers.sort()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    mydata[ticker] ={'ticker': ticker,
                     'dayHigh': result.info['dayHigh']
                     }

pprint.pprint(mydata)


#msft = yf.Ticker("MSFT")

# get all stock info
#pprint.pprint(msft.info)

# get historical market data
#hist = msft.history(period="10d")

#pprint.pprint(hist)