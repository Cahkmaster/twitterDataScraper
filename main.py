import tweepy
import pandas as pd
import configparser
# Ismaeel Hashimi

#reads config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# change keywords to whatever you want to search twitter for
keywords = '2021'
limit = 300

# used limit to bypass tweet per command limit
tweets = tweepy.Cursor(api.search_tweets, q=keywords, count = 100, tweet_mode = 'extended').items(limit)

# setting up dataframe
columns = ['Time', 'User', 'Tweet']
data = []

# for loop that appends tweets to data list
for tweet in tweets:
    data.append([tweet.created_at,tweet.user.screen_name, tweet.full_text])

# dataframe that uses data list
df = pd.DataFrame(data, columns = columns)

# creates a csv file with dataframe info
df.to_csv('tweets.csv')





