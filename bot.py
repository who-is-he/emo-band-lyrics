import tweepy, time, sys
import credentials
from creative_process import compose

INTERVAL = 60 * 60 * 8 # 8 hours

auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_KEY, credentials.ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    api.update_status(compose())
    time.sleep(INTERVAL)