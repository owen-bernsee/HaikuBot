#!/Desktop/school/pybot/helloWorld.py
"""Tweets 'Hello World' to timeline"""
import sys
import requests
import json
import tweepy

#twitter info
consumer_key = 'kHmRMNXitDdegE7Yp36XFzFmk'
consumer_secret = '7SCYvOKeiMVKlV05mFqrEjckafaWzcbkCn3J1DL10m7kHLVPhJ'
access_token = '1198538245941932033-y1OWbyK5XaHlSeUs955s6zd8jkyH7W'
access_token_secret = '8ybkqq7zgnifYzoH8AVA5tgaygvuNgHvfVzWG1TpqqNWU'

#twitter api
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#post hello world tweet
api.update_status('Hello world')

