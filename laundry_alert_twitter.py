import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

try:
    launderers
except NameError:
    launderers = {}

# Get users from tweets, store with location
for mention in api.mentions():
    user = mention["user"]["name"]
    location = mention["text"]
    launderers[user] = [location, 0]

# Check weather for each user
for user in launderers:
    if is_rainy(launderers[user][0], country="UK"):
	    api.update_status("@", user, "Get the washing in, it's gonna rain!")
	launderers[user][1] +=1
	if launderers[user][1] >= 10:
	    del launderers[user]

