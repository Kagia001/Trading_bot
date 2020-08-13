import config
import requests
import datetime
from core import dt, stringDt
import math
import progressbar


def tiingoRequest(url):  # simplified request function
    return requests.get("https://api.tiingo.com/" + url + "&token=" + config.tiingoKey).text


def minuteOHLC(ticker, fromDate, toDate):
    """return ohlc data in 1min steps in csv string form."""
    return tiingoRequest(
        (
            "iex/{}"
            "/prices"
            "?startDate={}"
            "&endDate={}"
            "&format=csv"
            "&resampleFreq=1min"
            "&columns=open,high,low,close,volume"
            "&forceFill=false"
        ).format(ticker, stringDt(fromDate), stringDt(toDate))
    )


def dailyOHLC(ticker, fromDate, toDate):
    """return ohlc data in daily steps in csv string form."""
    return tiingoRequest(
        (
            "tiingo/daily/"
            "{}"
            "/prices"
            "?startDate={}"
            "&endDate={}"
            "&format=csv"
            "&resampleFreq=daily"
            "&columns=open,high,low,close,volume"
        ).format(ticker, stringDt(fromDate), stringDt(toDate))
    )


def makeMinuteDataFile(ticker, fromDate, toDate):
    """make a file with csv stock data on a minute by minute level."""
    fromDate = fromDate
    toDate = toDate
    dateJump = datetime.timedelta(days=36)
    numberOfRequests = math.ceil((toDate - fromDate).days / 36)
    with open(f"data/{ticker}_Minute.txt", "w") as f:
        f.write("date,open,high,low,close\n")

    tempFrom = fromDate
    tempTo = fromDate + datetime.timedelta(days=35)
    dataRetrievalProgressBar = progressbar.progressbar(50, numberOfRequests - 1)

    with open(f"data/{ticker}_Minute.txt", "a") as f:
        for i in range(numberOfRequests):
            dataRetrievalProgressBar.update(i)
            f.write(minuteOHLC(ticker, tempFrom, tempTo).split("\n", 1)[1])

            tempFrom += dateJump
            tempTo = min(tempTo + dateJump, toDate)


def makeDailyDataFile(ticker, fromDate, toDate):
    """make a file with csv stock data on a daily level."""
    with open(f"data/{ticker}_Daily.txt", "w") as f:
        f.write(dailyOHLC(ticker, fromDate, toDate))


def makeMinuteAndDailyDataFile(ticker, fromDate, toDate):
    makeDailyDataFile(ticker, fromDate, toDate)
    makeMinuteDataFile(ticker, fromDate, toDate)


if __name__ == "__main__":
    makeMinuteAndDailyDataFile(
        config.ticker, datetime.date(2017, 1, 1), datetime.date(2020, 1, 1)
    )
