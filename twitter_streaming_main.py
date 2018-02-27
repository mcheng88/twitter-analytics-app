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
	def __init__(self, num_tweets_to_grab, retweet_count):
		self.counter = 0
		self.num_tweets_to_grab = num_tweets_to_grab
		self.retweet_count = retweet_count

	# on data, prints tweet 
	def on_data(self, data):
		try:
			json_data = json.loads(data)
			# print(json_data["text"])
			self.counter += 1
			retweet_count = json_data["retweeted_status"]["retweet_count"]

			if retweet_count >= self.retweet_count:
				# print(json_data["text"], retweet_count)
				self.stats.add_top_tweets(self.get_tweet_html(json_data['id']))

			if self.counter >= self.num_tweets_to_grab:
				return False

			return True
		except:
			# @TODO: need to edit this later.
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
	def __init__(self, num_tweets_to_grab, retweet_count):
		self.auth = OAuthHandler(config.consumer_key, config.consumer_secret)
		self.auth.set_access_token(config.access_token, config.access_secret)

		self.api = tweepy.API(self.auth)
		self.num_tweets_to_grab = num_tweets_to_grab
		self.retweet_count = retweet_count
		self.stats = stats()

	def get_streaming_data(self):
		myStream = Stream(auth = self.api.auth, listener=MyStreamListener(num_tweets_to_grab=self.num_tweets_to_grab, retweet_count=self.retweet_count))
		try:
			myStream.sample()
		#	myStream.filter(track=['trump'])
		except Exception as e:
			print(e.__doc__)

		top_tweets = self.stats.get_stats()
		print(top_tweets)

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
			# print(trend['name'])
			trend_tweets=[]
			trend_tweets.append(trend['name'])
			tt = tweepy.Cursor(self.api.search, q = trend['name']).items(3)
			for t in tt:
				trend_tweets.append(self.get_tweet_html(t.id))
                #print(tweet_html)
			trend_data.append(tuple(trend_tweets))
		print(trend_data)

	def get_tweet_html(self,id):
		oembed = self.api.get_oembed(id=id, hide_media = True, hide_thread = True)
		tweet_html = oembed['html'].strip("\n")
		return tweet_html


"""
Class for storing statistics of a tweet
"""
class stats():
	def __init__(self):
		self.top_tweets = []

	def add_top_tweets(self, tweet_html):
		self.top_tweets.append(tweet_html)

	def get_stats(self):
		return self.top_tweets


if __name__ == "__main__":
	num_tweets_to_grab = 10
	retweet_count = 10000
	twitMain = TwitterMain(num_tweets_to_grab,retweet_count)
	twitMain.get_streaming_data()
	twitMain.get_trends()