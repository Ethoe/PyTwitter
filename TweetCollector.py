import tweepy as tp
import csv

consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_key = "your_access_key"
access_secret = "your_access_secret"


def get_tweets(username):

    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tp.API(auth)

    # set count to numb of tweets, max 3000
    number_of_tweets = 100

    # get tweets
    tweets_for_csv = []
    for tweet in tp.Cursor(api.user_timeline, screen_name=username).items(number_of_tweets):
        # create array of tweet information: username, tweet id, date/time, text
        tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])

    # write to a new csv file from the array of tweets
    outfile = username + "_tweets.csv"
    print("writing to " + outfile)
    with open(outfile, 'w+') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(tweets_for_csv)


users = ['LilyPichu']

for user in users:
    get_tweets(user)
