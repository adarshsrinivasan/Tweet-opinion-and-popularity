import tweepy
from tweepy import Cursor
from nltk.corpus import stopwords

consumer_key = 'uiuse24zdQbSE3UACrue88IUc';
consumer_secret = 'KvxLDJneLDVzQkEF4blnVO5KgABKZ7qOpnDxHNfIxj4p5LJeAs'
access_key = '589241485-alNBxMQvKze0cQsMm6hXehISOzGrASohNVvsR0ju'
access_secret = '3WzwKcMMM0kDpaKoPAhTNhG16iki3zZWhTwV1eAAyP0Ci'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
query='#' + raw_input()
data = Cursor(api.search, q=query, geocode='12.9715987,77.59456269999998,100km', lang='en').items(5)

stop = set(stopwords.words("english"))

word_list = []
text_tweet = ''

print 'HashTag: ' + query + '\n'
for tweet in data:
	cleaned_text = filter(lambda x: x not in stop, tweet.text.split(' '))
		
	print tweet.user.location + '\n' + tweet.user.screen_name + '\n' + tweet.text + '\n'
	print cleaned_text
	print '\n'
