import tweepy
from decouple import config


auth = tweepy.OAuthHandler(config('CONSUMER_KEY'), config('CONSUMER_SECRET'))
auth.set_access_token(config('ACCESS_TOKEN'), config('ACCESS_TOKEN_SECRET'))
twitter_api = tweepy.API(auth)
