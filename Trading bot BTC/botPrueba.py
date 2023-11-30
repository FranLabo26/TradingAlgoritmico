from __future__ import (absolute_import, division, print_function, unicode_literals)
import datetime
from GoldenCross import GoldenCross
import backtrader as bt 
from StochRSI import StochRSIStrategy

if __name__ == '__main__':
    cerebro = bt.Cerebro()


dataDAY = bt.feeds.YahooFinanceCSVData(
    dataname = 'BTC-USD-DAY.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(2018,11,1),
    #do not pass values after this date
    todate= datetime.datetime(2023,11,29),
    reverse = False
)

dataMONTH = bt.feeds.YahooFinanceCSVData(
    dataname = 'BTC-USD-MONTH.csv',
    #do not pass values before this date
    fromdate = datetime.datetime(2018,11,1),
    #do not pass values after this date
    todate= datetime.datetime(2023,11,29),
    reverse = False
)



def run():
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(10000.0)
    saldoInicial = cerebro.broker.getvalue()
    print('Saldo Inicial: %.2f' % saldoInicial)

    cerebro.adddata(dataDAY)
    cerebro.addstrategy(StochRSIStrategy)
    #cerebro.addstrategy(GoldenCross)



    cerebro.run()
    cerebro.plot()

    saldoFinal= cerebro.broker.getvalue()
    print('Saldo Final: %.2f' % saldoFinal)

    saldoFinal=  (saldoFinal*100/saldoInicial)-100
    print('Porcentaje de ganancias: %.2f' % saldoFinal)

run()