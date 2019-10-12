import tweepy
from googletrans import Translator
consumer_key='key'
consumer_secret='key'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
access_token='key'
access_token_secret='key'
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
translator = Translator()
trends = api.trends_place(1)
for t in trends[0]['trends']:
    #print((t['name'],translator.translate(t['name']).text))
    print(t)