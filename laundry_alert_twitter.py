import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("pezoJMfy7ciq3ZKSzeuYXNOEJ", "IBJyPVu23T4CrhhzK8R9YxTPma5xKbWYlfQ1kANvieWN4D01QT")
auth.set_access_token("1168592646991949825-CIqcDG10n3OHAXkcK3Tmk4HJy2Q5Is", "tONZl9PsdyVgGUjp3bS4ao8g9Y3xRTS0aSJn4n1fKcNU0")

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


