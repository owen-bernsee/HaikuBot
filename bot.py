#!~/Desktop/school/pyBot/bot.py
import requests #http
import json
import tweepy
import random
from word_libraries import americana, billboard, words1, words2

#twitter credentials
consumer_key = 'kHmRMNXitDdegE7Yp36XFzFmk'
consumer_secret = '7SCYvOKeiMVKlV05mFqrEjckafaWzcbkCn3J1DL10m7kHLVPhJ'
access_token = '1198538245941932033-y1OWbyK5XaHlSeUs955s6zd8jkyH7W'
access_token_secret = '8ybkqq7zgnifYzoH8AVA5tgaygvuNgHvfVzWG1TpqqNWU'

#twitter oAuth2; API access
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Hello World Tweet
#api.update_status('Hello world.')

#x = random.choice(x)
#print(x)


def titler():
	"""Titles poem"""
	title = random.choice(list(billboard.keys()))
	#print(title.title())
	poet = random.choice(list(billboard.values()))
	#print(poet)
	msg = f"{title.title()} -- by {poet.title()}"
	#print(msg)
	return msg 
#titler()


def haiku():
	"""writes a haiku"""
	i1 = [] #5 syllables (5 x 1 syl words)
	i2 = [] #7 syllables (3 x 2 syl words + 1 syl word)
	#i3 = [] #5 syllables (2syl + 1 syl + 2syl)

	#line 1 
	for i in range(0,5):
		i = random.choice(words1)
		i1.append(i)
		line1 = ' '.join(i1)
	#print(str1)

	#line 2
	for t in range(0,3):
		t = random.choice(words2) 
		i2.append(t)
		str2 = ' '.join(i2)
	x2 = random.choice(words1) # makes second line = 7 syl
	line2 = str2 + ' ' +x2
	#print(line2)

	#line 3 
	r12 = random.choice(words2)
	r1 = random.choice(words1)
	r2 = random.choice(words2)
	line3 = r12 + " " + r1 + " " + r2
	#print(line3)
	head = titler()
	poem = f"\n{line1.title()}\n{line2.title()}\n{line3.title()}"
	out = head + "\n" + poem
	#return line1, line2, line3
	#return poem
	print(out)
	return out
haiku()


#print(x)

def tweet():
	#twitter credentials
	consumer_key = 'kHmRMNXitDdegE7Yp36XFzFmk'
	consumer_secret = '7SCYvOKeiMVKlV05mFqrEjckafaWzcbkCn3J1DL10m7kHLVPhJ'
	access_token = '1198538245941932033-y1OWbyK5XaHlSeUs955s6zd8jkyH7W'
	access_token_secret = '8ybkqq7zgnifYzoH8AVA5tgaygvuNgHvfVzWG1TpqqNWU'

	#twitter oAuth2; API access
	auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	
	api.update_status(haiku())
tweet()







