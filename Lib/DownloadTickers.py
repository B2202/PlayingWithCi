import yfinance as yf
import datetime


class TickerUpdater:
    def __init__(self):
        self.globalStart = "2000-01-01"
        self.tickerList = ['MRK']

    def DownloadTickers(self):
        newData = yf.download(self.tickerList, start=self.globalStart,
                              stop=datetime.datetime.today(),
                              group_by='Ticker')
        return newData
