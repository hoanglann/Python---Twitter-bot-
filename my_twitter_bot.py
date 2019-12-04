import tweepy
import time

print('This is my Twitter bot')

CONSUMER_KEY = 'ov4bb9OQmcjOHtv5wgKvFy07N'
CONSUMER_SECRET = 'IecG6sGlh0qkG4WyoIiqE5sL1uJQRZNro0fQMiLtoO13sH6zVP'
ACCESS_KEY = '1863430238-IWxVxGjVF7msHrGXTzrlHu2L5rQrbpbkevV2x31'
ACCESS_SECRET = 'XhDt9apCU4iMiAdUrVNYUqVhJDuP9z6A0y2EgiSiHyTQ7'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...')
    #Devnote ID = 1200062725809942535
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + '#HelloWorld back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(2)
