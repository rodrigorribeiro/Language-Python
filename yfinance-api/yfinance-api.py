#!/usr/bin/env python2.7

__author__ = "Rodrigo Ribeiro"
__version__ = "1.0.0"

import yfinance as yf
import sys
import argparse

banner  = "------------------------------------------------\n"
banner += "|    YFINANCE-API - Get a lot of stocks!        |\n"
banner += "------------------------------------------------\n"
print banner

if len(sys.argv) == 6:

    parser = argparse.ArgumentParser()
    parser.add_argument("--period", help="specify the period 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max", type=str)
    parser.add_argument("--interval", help="specify the interval 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo", type=str)
    parser.add_argument("--start", help="specify the start date yyyy-mm-dd", type=str)
    parser.add_argument("--end", help="specify the end date yyyy-mm-dd", type=str)
    parser.add_argument("--ticker", help="specify the ticker MSFT", type=str)

    args = parser.parse_args()
    
    arg_period = args.period
    arg_interval = args.interval
    arg_start = args.start
    arg_end = args.end
    arg_ticker = args.ticker

    # get data on this ticker
    tickerData = yf.Ticker(arg_ticker + ".SA")

    # get the historical prices for this ticker
    tickerDf = tickerData.history(period=arg_period, interval=arg_interval, start=arg_start, end=arg_end)

    # save CSV file
    tickerDf.to_csv(arg_ticker + '.csv', index = True, header=True)

    print("[*] Downloaded and saved CSV file: " + arg_ticker + '.csv')

else:

    print "[!] You need to specify a search stocks query!"
    print "[-] Usage: # yfinance-api.py --period=1d --interval=1m --start=2020-04-23 --end=2020-04-24 --ticker=MSFT\n"
    print "[-] --period - specify the period 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max"
    print "[-] --interval - specify the interval 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo"
    print "[-] --start - specify the start date yyyy-mm-dd"
    print "[-] --end - specify the end date yyyy-mm-dd"
    print "[-] --ticker - specify the ticker ITUB4"