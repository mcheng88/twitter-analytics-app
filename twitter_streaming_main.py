import tweepy
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
import config
import json


"""
This is the listener class, will update with statistics and such
"""
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

"""
What if I set it up so that you could change the country code or the streaming search?
"""
class TwitterMain():
	def __init__(self, num_tweets, retweet_count):
		self.auth = OAuthHandler(config.consumer_key, config.consumer_secret)
		self.auth.set_access_token(config.access_token, config.access_secret)

		self.api = tweepy.API(self.auth)

		self.num_tweets = num_tweets
		self.retweet_count = retweet_count

	def get_streaming_data(self):
		myStream = Stream(auth = api.auth, listener=MyStreamListener(num_tweets=1000,
		retweet_count = self.retweet_count))
		try:
		#	myStream.sample()
			myStream.filter(track=['trump'])
		except Exception as e:
			print(e.__doc__)

	def get_trends(self):
		"""
		With trends you need to use the stupidly set up 
		Yahoo! Where (the fuck) On Earth (am I and why does Yahoo own this) ID
		Here are some common WOEIDs:
		1: Global
		23424977: USA 
		2459115: NYC
		"""
		trends = self.api.trends_place(23424977)
		trend_data = []

		for trend in trends[0]["trends"]:
			print(trend['name'])
			trend_tweets=[]
			trend_tweets.append(trend['name'])
			tt = tweepy.Cursor(self.api.search, q = trend['name']).items(3)
			for t in tt:
				trend_tweets.append(t.text)
                #print(tweet_html)
			trend_data.append(tuple(trend_tweets))
		print(trend_data)
