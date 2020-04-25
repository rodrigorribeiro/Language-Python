#!/usr/bin/env python2.7

__author__ = "Rodrigo Ribeiro"
__version__ = "1.0.0"

import os
import sys
import jsonpickle
import tweepy
from tweepy import OAuthHandler
from datetime import datetime

def init_api():
    API_KEY = '<API_KEY>'
    API_SECRET = '<API_SECRET>'
    ACCESS_TOKEN = '<ACCESS_TOKEN>'
    ACCESS_TOKEN_SECRET = '<ACCESS_TOKEN_SECRET>'

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def set_global_id(id):
    # define glb_id var global
    global glb_id
    # check the biggest id
    if id > glb_id:
        glb_id = id

def save_offset(glb_id, filename):
    file = open(filename,"w+")
    file.write(str(glb_id))
    file.close()

def persist_offset(twitter_offset_file):
    if not os.path.exists(twitter_offset_file):
        file = open(twitter_offset_file,"w+")
        file.write(str("0"))
        sinceId = 0
        file.close()
    else:
        file = open(twitter_offset_file,"r")
        sinceId = int(file.read())
        file.close()
    return sinceId

def verify_offset(fName):
    if os.path.exists(fName):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not
    return append_write

banner  = "------------------------------------------------\n"
banner += "|    TWITTER-API - Get a lot of tweets!         |\n"
banner += "------------------------------------------------\n"
print banner

# set global var id
glb_id = 0

if len(sys.argv) > 1:

    twitter_search = sys.argv[1]

    twitter_offset_file = twitter_search + ".offset"

    # persist offset into a file
    sinceId = persist_offset(twitter_offset_file)

    # initialize api
    api = init_api()

    # define some vars
    searchQuery = twitter_search  # this is what we're searching for
    maxTweets = 10000000 # Some arbitrary large number
    tweetsPerQry = 100  # this is the max the API permits
    fName = twitter_search + ".json" # We'll store the tweets in a json file.

    # verify if offset file exists
    append_write = verify_offset(fName)

    # If results only below a specific ID are, set max_id to that ID.
    # else default to no upper limit, start from the most recent tweet matching the search query.
    max_id = -1L

    tweetCount = 0
    print("[-] Downloading max {0} tweets".format(maxTweets))
    with open(fName, append_write) as f:
        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                    else:
                        new_tweets = api.search(q=searchQuery, count=tweetsPerQry, since_id=sinceId)
                else:
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id - 1))
                    else:
                        new_tweets = api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id - 1), since_id=sinceId)
                if not new_tweets:
                    print("[!] No more tweets found")
                    break
                for tweet in new_tweets:
                    dict = tweet._json
                    id = dict["id"]
                    set_global_id(id)
                    save_offset(glb_id, twitter_offset_file)
                    f.write(jsonpickle.encode(tweet._json, unpicklable=False) + "\n")
                tweetCount += len(new_tweets)
                print("[+] Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("[!] some error : " + str(e))
                break

    print ("[*] Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))

else:

    print "[!] You need to specify a search query!"
    print "[-] Usage: # twitter-api.py something"
