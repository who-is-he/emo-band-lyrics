import tweepy, time, sys
from creative_process import compose
from credentials import *

INTERVAL = 60 * 60 * 8 # 8 hours

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    print("making emo lyrics...")
    api.update_status(compose())
    print("sleeping :)")
    time.sleep(INTERVAL)
