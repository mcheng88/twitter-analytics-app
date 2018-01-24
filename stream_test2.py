import tweepy
from tweepy import OAuthHandler
from tweepy import StreamListener
from tweepy import Stream
import config
import json

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        return True
    def on_error(self, status):
    	print(status.text)
    	return False

if __name__ == "__main__":
	auth = OAuthHandler(config.consumer_key, config.consumer_secret)
	auth.set_access_token(config.access_token, config.access_secret)
	api = tweepy.API(auth)
	myStream = Stream(auth = api.auth, listener=MyStreamListener())
	myStream.filter(track=['trump'], async=True)
