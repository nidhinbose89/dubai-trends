"""The configuration file for the application."""

from twitter import OAuth

# Twitter Keys
CONSUMER_KEY = "BMNlxPpMDW2b0eOfsmyfXZnkl"
CONSUMER_SECRET = "dx19BbKCifWC5shRc7Kbar6cqMpAPkEBk2JvNDup6jW2Ov6yuw"
ACESS_KEY = "149402539-mqB9xlUj6RTBFvcMLRwboQOUVbDMTGdHVJAUj70F"
ACCESS_SECRET = "ea8ug4tWgZk1Yg8n3kVRrcu7bPD981ZZ96uzIyBNJmtpw"

# http://woeid.rosselliot.co.nz/lookup/dubai
DUBAI_WOEID = 1940345

# The OAuth object for twitter.
TWITTER_AUTH = OAuth(ACESS_KEY,
                     ACCESS_SECRET,
                     CONSUMER_KEY,
                     CONSUMER_SECRET)
