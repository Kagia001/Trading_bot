import backtrader
import core


class myStrategy(backtrader.Strategy):
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(f"{dt.isoformat()}, {txt}")

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.order = None

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status == order.Completed:
            if order.isbuy():
                self.log(
                    f"BUY EXECUTED, PRICE: {order.executed.price}, COST: {order.executed.value}, COMM: {round(order.executed.comm, 2)}"
                )
            if order.issell():
                self.log(
                    f"SELL EXECUTED, PRICE: {order.executed.price}, COST: {order.executed.value}, COMM: {round(order.executed.comm, 2)}"
                )

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log("Order Canceled/Margin/Rejected")

        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log(
            f"OPERATION PROFIT, GROSS {round(trade.pnl, 2)}, NET: {round(trade.pnlcomm, 2)}"
        )

    def next(self):
        self.log(f"Close: {self.dataclose[0]}")
        if self.order:
            return

        if not self.position:
            if self.dataclose[-2] > self.dataclose[-1] > self.dataclose[0]:
                self.log(f"BUY CREATE, {self.dataclose[0]}")
                self.order = self.buy()

        else:
            if len(self) >= self.bar_executed + 5:
                self.log("SELL CREATE, %.2f" % self.dataclose[0])
                self.order = self.sell()


if __name__ == "__main__":
    core.run()
