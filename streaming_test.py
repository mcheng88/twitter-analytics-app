import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler
import config
import json

class twitter_listener(StreamListener):
	def on_data(self, data):
		j = json.loads(data)
		print(j["text"])
		return True

	def on_error(self, status):
		print(status)

if __name__ == "__main__":
	auth = OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_secret)
	api = tweepy.API(auth)
	twitter_stream = Stream(auth, twitter_listener())
	try:
		twitter_stream.sample()
	except Exception as e:
		print(e.__doc__)