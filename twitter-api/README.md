# TWITTER-API - Get a lot of tweets!
> Connecting to twitter api and save json file output.

This code in python connect through twitter api and search what you want, this code can control the download and search the content again, avoiding the duplicate increment of new tweets.

## Requirements

There are some libraries requirements:

os, sys, jsonpickle, tweepy, datetime

```sh
pip install tweepy
pip install jsonpickle
```

## Installation

There are no installation.

## Usage example

You need to specify only on argument, example:

```sh
------------------------------------------------
|    TWITTER-API - Get a lot of tweets!         |
------------------------------------------------

[!] You need to specify a search query!
[-] Usage: # twitter-api.py something
```

The result example:

```sh
------------------------------------------------
|    TWITTER-API - Get a lot of tweets!         |
------------------------------------------------

[-] Downloading max 10000000 tweets
[!] No more tweets found
[*] Downloaded 0 tweets, Saved to something.json
```

The new file will be created:
```sh
something.json
```

## Development setup

There are no development setup.

## Release History

* 1.0.0
    * The first proper release

## Meta

Rodrigo Ribeiro – [@silvarribeiros](https://twitter.com/silvarribeiros) – silva.rrs@gmail.com

[https://github.com/rodrigorribeiro/](https://github.com/rodrigorribeiro/)

## Credits
This code was adapted from an original project:

How to use Twitter’s Search REST API most effectively.
https://bhaskarvk.github.io/2015/01/how-to-use-twitters-search-rest-api-most-effectively./

## Contributing

1. Fork it (<https://github.com/rodrigorribeiro/Language-Python/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
