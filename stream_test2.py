import tweepy
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
import config
import json

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

	# initializes the listener with a counter. 
	def __init__(self, num_tweets):
		self.counter = 0
		self.num_tweets = num_tweets


	# on data, prints tweet 
	def on_data(self, data):
		try:
			j = json.loads(data)
			print(j["text"])
			self.counter += 1
			if self.counter == self.num_tweets:
				return False

			return True
		except:
			pass

	# prints out tweet. 
#    def on_status(self, status):
#        print(status.text)
#        return True

	# on error, prints the error text.
	def on_error(self, status):
		print(status.text)
		return False

if __name__ == "__main__":
	# For authentication purposes
	auth = OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_secret)
	api = tweepy.API(auth)


	myStream = Stream(auth = api.auth, listener=MyStreamListener(num_tweets=10))
	try:
	#	myStream.sample()
		myStream.filter(track=['trump'])
	except Exception as e:
		print(e.__doc__)
