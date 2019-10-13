import tweepy # getting twitter trends and tweets
from googletrans import Translator # translate tweets from worlwide trends
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer # Analyze tweet sentiments to find out which require help
import emoji # tweets contains emojis and the translate package does not take it into account
analyser = SentimentIntensityAnalyzer()


# Keys need to be acquired before running
consumer_key=""
consumer_secret=""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
access_token=""
access_token_secret=""
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
translator = Translator()
trends = api.trends_place(1)
t10trends=[]
i=0
for t in trends[0]['trends']:
    if i<10:
        t10trends.append(t['name'])
    i+=1
print(t10trends)
def deEmojify(inputString):
    return emoji.get_emoji_regexp().sub(u'', inputString) # remove regular emojis using emoji package in string

def rating(tweets):
    tobea=[] # to be analyzed
    for tweet in tweets:
        if tweet.lang!='en':
            try:
                tobea.append(translator.translate(deEmojify(tweet.text)).text)
            except:
                print("This tweet was excluded from analysis due to unicode characters that could not be translated "+tweet.text) # some special characters still persist after attempted removal
        else:
            tobea.append(tweet.text) 
    totalscore=0
    count=0
    for article in tobea:
        ti=article
        # the compound gives us an idea on the positiveness or negativeness of a tweet
        totalscore+=analyser.polarity_scores(ti)['compound']
        count+=1
    if count==0:
        # the compound analysis returns negative values and we require something that is  more negative to hold as an incorrect return
        return -10
    return totalscore/count
f=open("trending_relevant.txt","w")
for t in t10trends:
    tweets=api.search(q=t,count=10,result_type='popular')
    rat=rating(tweets)
    print(rat)
    if rat!=-10:
        if rat<-0.2:
            f.write(t+"\n")
            for tweet in tweets:
                # try:
                f.write("".join(tweet.id_str+"\n") )# this writes the links to a text file to be processed by another script to make the code modular
                # except:
                #     ""
    #f.write("\n")

