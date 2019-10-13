import tweepy # getting twitter trends and tweets
from googletrans import Translator # translate tweets from worlwide trends
import emoji
import re
import nltk
from nltk.corpus import stopwords
import requests

nltk.download('stopwords')
s=set(stopwords.words('english'))
# We use this list to give weight to topics of relevance in identifying topics
weightwords="enivironment,typhoon,forest fire,amzazon,fire,drought,dry,dessert,flood,crisis,monsoon,tree,animal,death,violence,pain,homicide,pray,world,mass,drug,meth,coc,endangered,save,help,killed,earth,quake,ground,farm,grow,destroy,fung,mold,disease,infect,attack,victim,genocide,cide,plastic,micro,pollut,air,ozone,breath,smell,erad,destr,stop,happen,dea,forest,wood,effect,impact,hurricane,tornadoe,asteroid,war,poverty,sick"
keywords=set(weightwords.split())
translator = Translator()
consumer_key=""
consumer_secret=""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
access_token=""
access_token_secret=""
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
        if word not in s and not word.isnumeric() and len(word)>0:
            if word in wordcount.keys():
                wordcount[word]+=1
            else:
                wordcount[word]=1
            if wordcount[word]>5:
                common.add(word)
def isPlace(word):
    response=requests.get("https://restcountries.eu/rest/v2/name/"+word)
    if 'status' in response.json():
        return False
    return True
common=list(common)
weights=[]
i=0
for w in common:
    weights.append(wordcount[w])
    # these weights are to better the results, as this is using a naive way to find resources
    if w in keywords:
        weights[i]+=5
    if isPlace(w):
        weights[i]+=5
    i+=1
common=[i for _,i in sorted(zip(weights,common))]

phrase=" ".join(common[len(common)-2:len(common)])
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query =phrase+"charity"
f=open("urls.txt","w")
for j in search(query, tld="com", num=10, stop=2, pause=2): 
    f.write(j+"\n")
