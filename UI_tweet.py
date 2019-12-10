#!~/Desktop/school/pyBot/UI_tweet.py
import tweepy

#twitter credentials
consumer_key = 'kHmRMNXitDdegE7Yp36XFzFmk'
consumer_secret = '7SCYvOKeiMVKlV05mFqrEjckafaWzcbkCn3J1DL10m7kHLVPhJ'
access_token = '1198538245941932033-y1OWbyK5XaHlSeUs955s6zd8jkyH7W'
access_token_secret = '8ybkqq7zgnifYzoH8AVA5tgaygvuNgHvfVzWG1TpqqNWU'

#twitter oAuth2; API access
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

admin_info = {'id': None, 'values': None}
UI_dict = []
UI_values = []
print("Welcome to a twitter bot by Owen Bernsee")
name = input("\nPlease enter your name: ")
admin_info['id'] = name
def collector():
	"""Collects words & phrases from user input & adds them to UI_values"""
	print("Welcome to Owen's twitter bot.\nFollow @bot_by_owen for posts & updates.")
	live = True
	jane_doe = True
	u_usr = name.strip()
	while live == True:
		print(f"\n\nHello, {name.title()}!\n")
		print("\nThis bot will compile words and phrases. If you would like to submit single words please do so one at a time.\n")
		UI_in = input("\tEnter words or phrases for me to tweet: ")
		UI_values.append(UI_in)
		if UI_in == 'q':
			UI_values.remove('q')
			print(f"Thanks for contributing, {name.title()}. See you online! =D ")
			print("Follow @bot_by_owen for posts & updates.")
			break
		else:
			live = True
			admin_info['values'] = UI_values
			continue

	return UI_dict, UI_values 
collector()



print(f"{name.title()}'s contributions:")
for i in UI_values:
		print(f"\t{i}")
#shows the user their contributions


#pickle the data out to access in bot_admin.py
import pickle
with open("user_library.txt", "wb") as library:
		pickle.dump(UI_values, library)
with open("usernames.txt", 'wb') as name_file:
	pickle.dump(admin_info['id'], name_file)




	

