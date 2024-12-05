import csv
import itertools
import requests
import argparse

def send_request(payload):
    res = requests.post("http://tweet-analyzer.tweet-ingestor:8001", json=payload, headers={"Content-Type": "application/json"})
    print(res.json())

def read_csv(count):
    csv_data = []
    with open('election_day_tweets.csv', newline='') as csvFile:
        csv_reader = csv.DictReader(csvFile, delimiter=',')
        for row in itertools.islice(csv_reader, count):
            csv_data.append(row) 
    return csv_data

def get_or_none(value):
    if not value.strip(" "):
        return None
    else:
        return value


def create_tweet_payload(tweet_data):
    return {
        "created_at": tweet_data.get("created_at"),
        "id": tweet_data.get("id"),
        "full_text": tweet_data.get("text"),
        "user": {
            "id": tweet_data.get("user.id"),
            "name": tweet_data.get("user.name"),
            "screen_name": tweet_data.get("user.screen_name")
        },
        "retweet_count": tweet_data.get("retweet_count"),
        "favourite_count": tweet_data.get("user.favourites_count"),
        "lang": tweet_data.get("lang"),
        "is_retweet": tweet_data.get("retweeted"),
        "geo": get_or_none(tweet_data.get("geo")),
        "coordinates": get_or_none(tweet_data.get("coordinates")),
        "place": get_or_none(tweet_data.get("place"))
    }

def send_traffic(args):
    csv = read_csv(args.count)
    for tweet in csv:
        tweet_payload = create_tweet_payload(tweet)
        send_request(tweet_payload)
    print("true")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='TrafficSender',
        description='Script for sending traffic to the Tweet Ingestor component'
    )
    parser.add_argument('-c', '--count', type=int, help='Number of tweets to send', required=True)

    args = parser.parse_args()

    send_traffic(args)
