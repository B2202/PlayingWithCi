import pytest
from DownloadTickers import TickerUpdater
import pandas

def test_CorrectTypeOfTickerList():
    updateTickersInstance = TickerUpdater()
    assert isinstance(updateTickersInstance.tickerList, list)

#def test_CorrectTypeOfTickerReturn():
#    updateTickersInstance = TickerUpdater()
#    assert isinstance(updateTickersInstance.DownloadTickers(), pandas.DataFrame)