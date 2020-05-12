# YFINANCE-API - Get a lot of stocks!
> Connecting to yahoo finance api and save csv file output.

This code in python connect through yahoo finance api and search what you want.

## Requirements

There are some libraries requirements:

yfinance, sys, argparse

```sh
pip install yfinance
pip install argparse
```

## Installation

There are no installation.

## Usage example

You need to specify only on argument, example:

```sh
------------------------------------------------
|    YFINANCE-API - Get a lot of stocks!       |
------------------------------------------------

[!] You need to specify a search stocks query!
[-] Usage: # yfinance-api.py --period=1d --interval=1m --start=2020-04-23 --end=2020-04-24 --ticker=MSFT
[-] --period - specify the period 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
[-] --interval - specify the interval 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
[-] --start - specify the start date yyyy-mm-dd
[-] --end - specify the end date yyyy-mm-dd
[-] --ticker - specify the ticker ITUB4
```

The result example:

```sh
------------------------------------------------
|    YFINANCE-API - Get a lot of stocks!       |
------------------------------------------------

[*] Downloaded and saved CSV file: " + ITUB4 + '.csv'
```

The new file will be created:
```sh
ITUB4.csv
```

## Development setup

There are no development setup.

## Release History

* 1.0.0
    * The first proper release

## Meta

Rodrigo Ribeiro – [@silvarribeiros](https://twitter.com/silvarribeiros) – silva.rrs@gmail.com

[https://github.com/rodrigorribeiro/](https://github.com/rodrigorribeiro/)

## Contributing

1. Fork it (<https://github.com/rodrigorribeiro/Language-Python/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
