# to query the api
import tweepy
# to hide sensitive information
import configparser
# to convert data to csv
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('config.ini')
# sensitive data is stored in config.ini

# reading all sensitive data
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# creating api instance
api = tweepy.API(auth, wait_on_rate_limit=True)

# which keywords to search for
keywords = '#StopHindiImposition'
# number of tweets to search
limit = 10000

# querying api
tweets = tweepy.Cursor(api.search, q=keywords,
                       count=100, tweet_mode='extended').items(limit)

# create DataFrame
columns = ['Username', 'Tweet', 'Place', 'ID',
           'Created', 'User', 'Entities']
data = []
# will hold data

# filtering through returned JSON
for tweet in tweets:
    if tweet.place:
        data.append([tweet.user.screen_name, tweet.full_text, tweet.place,
                    tweet.id, tweet.created_at, tweet.user, tweet.entities])
    else:
        data.append([tweet.user.screen_name, tweet.full_text, ' ', tweet.id,
                    tweet.created_at, tweet.user, tweet.entities])

# converting to csv
df = pd.DataFrame(data, columns=columns)
filename = '10000tweets.csv'
df.to_csv(filename)
