#!~/Desktop/school/pyBot/bot_admin.py
import requests #http
import json
import tweepy
import pickle

#twitter credentials
consumer_key = 'kHmRMNXitDdegE7Yp36XFzFmk'
consumer_secret = '7SCYvOKeiMVKlV05mFqrEjckafaWzcbkCn3J1DL10m7kHLVPhJ'
access_token = '1198538245941932033-y1OWbyK5XaHlSeUs955s6zd8jkyH7W'
access_token_secret = '8ybkqq7zgnifYzoH8AVA5tgaygvuNgHvfVzWG1TpqqNWU'

#twitter oAuth2; API access
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

name_in = 'usernames.txt'
unpickle_name = open(name_in, 'rb')
NP = pickle.load(unpickle_name)
print("Usernames:\n\t",NP)
data_in = 'user_library.txt'
unpickle_data = open(data_in, 'rb')
IP = pickle.load(unpickle_data)
print("User Input Library:\n\t", IP)

