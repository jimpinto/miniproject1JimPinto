### INF601 - Advanced Programming in Python
### Jim Pinto
### Mini Project 1
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)


mytickers = ["MSFT", "AAPL", "GOOG", "NVDA", "AMC"]


mytickers.sort()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    # get historical market data
    hist = result.history(period="10d")
    last10days = []
    for date in hist['Close']:
        last10days.append(date)
    if len(last10days) == 10:
        myarray = np.array(last10days)
        max_price = myarray.max() + (myarray.max()*.05)
        min_price = myarray.min() - (myarray.min()*.05)
        plt.plot(myarray)
        plt.xlabel('Data Points')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price))
        plt.title(f"{ticker} last 10 closing price")
        plt.savefig(f"charts/{ticker}.png")
    else:
        print(f"Do not have 10 days of data. Only have {len(last10days)} days of data ")









