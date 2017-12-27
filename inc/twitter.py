import os
from dotenv import load_dotenv
import tweepy

dotenv_path = os.path.join('.', '.env')
load_dotenv(dotenv_path)

env = {
    'twitter': {
        'key': os.getenv('TT_KEY'),
        'secret': os.getenv('TT_SECRET'),
        'access_token': os.getenv('TT_ACCESS_TOKEN'),
        'token_secret': os.getenv('TT_TOKEN_SECRET')
    }
}

def tweets():
    auth = tweepy.OAuthHandler(env['twitter']['key'], env['twitter']['secret'])
    auth.set_access_token(env['twitter']['access_token'], env['twitter']['token_secret'])
    return tweepy.API(auth)

def q(q, max_results):
    return tweets().search(q, count=max_results)

