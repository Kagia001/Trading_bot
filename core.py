import backtrader
import config
import datetime


def dt(date):
    """convert YYYY-MM-DD string to datetime object"""
    return date.strptime("%Y-%m-%d")


def stringDt(date):
    """convert datetime object to YYYY-MM-DD string"""
    return date.strftime("%Y-%m-%d")


def run():
    cerebro = backtrader.Cerebro()

    #broker setup
    cerebro.broker.setcash(config.startCash)
    cerebro.broker.setcommission(commission = config.broker_commision)

    if config.tradingFrequency == "minute":
        ohlc = backtrader.feeds.GenericCSVData(
            dataname="data/" + config.ticker + "_Minute.txt",
            openinterest=-1,
            name="historical {} price data".format(config.ticker),
            fromdate=config.fromDate,
            todate=config.toDate,
            timeframe=backtrader.TimeFrame.Minutes,
            dtformat="%Y-%m-%d %H:%M:%S%z",
        )
    else:
        ohlc = backtrader.feeds.GenericCSVData(
            dataname="data/" + config.ticker + "_Daily.txt",
            openinterest=-1,
            name="historical {} price data".format(config.ticker),
            fromdate=config.fromDate,
            todate=config.toDate,
            timeframe=backtrader.TimeFrame.Days,
            dtformat="%Y-%m-%d",
        )

    cerebro.adddata(ohlc)

    cerebro.addstrategy(config.strategy)

    print("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())
    cerebro.run()
    print("Final Portfolio Value: %.2f" % cerebro.broker.getvalue())

if __name__ == '__main__':
    run(3)
