### INF601 - Advanced Programming in Python
### Jim Pinto
### Mini Project 1
import pprint
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt

mytickers = ["MSFT", "AAPL", "GOOG", "NVDA", "AMC"]


mytickers.sort()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    # get historical market data
    hist = result.history(period="10d")
    last10days = []
    for date in hist['Close']:
        last10days.append(date)
    myarray = np.array(last10days)
    plt.plot(myarray)
    plt.show()









