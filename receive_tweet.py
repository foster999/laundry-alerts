from collections import namedtuple

Location = namedtuple('Location', ['city','country'])

def get_city_and_country(tweet):
	tweet_arr = tweet.split(',')
	if len(tweet_arr) > 1:
		country = tweet_arr[-1].strip() 
		city = (',').join(tweet_arr[:-1])
	else: 
		city = tweet
		country =""
	return Location(city, country)