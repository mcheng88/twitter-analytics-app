#!usr/bin/python3
import tweepy
from tweepy import OAuthHandler
import config

if __name__ == "__main__":
	auth = OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_secret)
	api = tweepy.API(auth)

	#Searching, where q is the search term. .items(5) restricts to only returning 5 results
	search_results = tweepy.Cursor(api.search, q="Python").items(5)
	for result in search_results:
		print(result.text)

	trends = api.trends_place(1)

	for trend in trends[0]["trends"]:
		print(trend['name'])
