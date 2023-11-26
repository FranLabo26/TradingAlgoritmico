import math
import backtrader as bt

class GoldenCross(bt.Strategy):
    params = (('fast', 10),('slow',25),('order_porcentage', 0.95),('ticker', 'AAPL'))
    def __init__(self):
        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period= self.params.fast,plotname='10 day moving average'
        )

        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period= self.params.slow,plotname='20 day moving average'
        )

        self.crossover = bt.indicators.CrossOver(self.fast_moving_average, self.slow_moving_average)

    def next(self):
        if self.position.size == 0: 
            if self.crossover > 0:
                amount_to_invest = (self.params.order_porcentage * self.broker.cash)
                self.size = math.floor(amount_to_invest / self.data.close)
                print("Buy {} shares of {} at {}".format(self.size, self.params.ticker, self.data.close[0]))
                self.buy(size=self.size)

        if self.position.size > 0:
            if self.crossover < 0:
                print ("Sell {} shares of {} at {}".format(self.size, self.params.ticker, self.data.close[0]))
                self.close()
