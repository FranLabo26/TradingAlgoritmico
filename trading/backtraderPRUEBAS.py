import os, sys, argparse
import pandas as pd
import backtrader as bt
from strategies.GoldenCross import GoldenCross

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

spy_prices = pd.read_csv ('oracle.csv', index_col = 'Date', parse_dates = True)

feed = bt.feeds.PandasData(dataname =spy_prices)
cerebro.adddata(feed)

cerebro.addstrategy(GoldenCross)

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())


cerebro.plot()

