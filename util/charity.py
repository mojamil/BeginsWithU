import tweepy # getting twitter trends and tweets
from googletrans import Translator # translate tweets from worlwide trends
import emoji
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
s=set(stopwords.words('english'))

translator = Translator()
consumer_key="qnPdxzRBALjDJ99XuAw9O4qK5"
consumer_secret="7ZYQSrFHC45Sdag4nZdLWxvmKUvC1RqBynW7ws6UqK8uxWoJPy"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
access_token="799410017145339905-BV5PBq4XsBnTd0rNKgUJbaVp2Wjv4MU"
access_token_secret="51iVHaZhJWfRjWJvGcruYLmmV3KmGBI9omjltzMA13y9D"
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def deEmojify(inputString):
    return emoji.get_emoji_regexp().sub(u'', inputString) # remove regular emojis using emoji package in string
    
f=open("trending_relevant.txt",'r')
lines=f.read().split("\n")
i=1
curr=lines[0]
test=lines[0]
linkdict={}
linkdict[curr]=[]
while i<len(lines):
    if i%11==0:
        curr=lines[i]
        linkdict[curr]=[]
    else:
        linkdict[curr].append(lines[i])
    i+=1
tweets=[]
for tweet in linkdict[test]:
    tweets.append(translator.translate(deEmojify(api.get_status(tweet).text)).text)
wordcount={}
common=set()
for tweet in tweets:
    for word in tweet.split():
        word=re.sub(r'\W+', '', word)
        word=word.lower()
        if word not in s and not word.isnumeric():
            if word in wordcount.keys():
                wordcount[word]+=1
            else:
                wordcount[word]=1
            if wordcount[word]>5:
                common.add(word)
phrase=" ".join(common)
print(phrase)

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query =phrase+"charity navigator"
  
for j in search(query, tld="com", num=10, stop=4, pause=2): 
    print(j) 
