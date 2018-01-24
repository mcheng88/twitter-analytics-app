import tweepy
from tweepy import OAuthHandler
from tweepy import StreamListener
import config
import json

class twitter_listener(StreamListener):
	def __init__(self, num_tweets_to_grab):
		self.counter = 0
		self.num_tweets_to_grab = num_tweets_to_grab

    def on_data(self, data):
    	try:
    		json_data = json.loads(data)x
    		self.counter += 1
    		with open('python.json', 'a') as 

    #Catches errors and disconnects stream when error is found.		
    def on_error(self, status_code):
    	print(status_code)
		return False




class TwitterMain():
	def __init__(self, num_tweets_to_grab):
		self.num_tweets_to_grab = num_tweets_to_grab

	def get_streaming_data(self):
		twitter_stream = Stream(self.auth, twitter_listener(num_tweets_to_grab))
		try:
			twitter_stream.sample()
		except Exception as e:
			print(e.__doc__)

		print(top_tweets)

	def get_trends(self):
		trends = self.api.trends_place(1)
		trend_data = []

		for trend in trends[0]["trends"]
			print(trend['name'])
			trend_tweets = []
			trend_tweets.append(trend['name'])
			tt = tweepy.Cursor(self.api.search, q = trend['name']),items(3)
			for t in tt:
				trend_tweets.append(self.get)


if __name__ == "__main__":
	auth = OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_secret)
	api = tweepy.API(auth)