
import datetime  # For datetime objects
import backtrader as bt
from strategy import TestStrategy


cerebro = bt.Cerebro()

cerebro.broker.set_cash(1000000)

data = bt.feeds.YahooFinanceCSVData(
    dataname = 'oracle.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(2020,1,1),
    #do not pass values after this date
    todate= datetime.datetime(2023,12,31),
    reverse = False
)

cerebro.adddata(data)
cerebro.addstrategy(TestStrategy)
print('Starting portfolio value: %.2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final portfolio value: %.2f' % cerebro.broker.getvalue())