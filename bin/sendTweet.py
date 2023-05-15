import argparse
import json
import sys
import time
import random
from datetime import datetime
from confluent_kafka import Producer
import socket


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg.value()), str(err)))
    else:
        print("Message produced: %s" % (str(msg.value())))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('topic', type=str,
                        help='Name of the Kafka topic to stream.')
    parser.add_argument('--speed', type=float, default=1, required=False,
                        help='Speed up time series by a given multiplicative factor.')
    args = parser.parse_args()

    topic = args.topic
    p_key = "key"

    conf = {'bootstrap.servers': "localhost:9092",
            'client.id': socket.gethostname()}
    producer = Producer(conf)

    while True:
        tweet = {
            "text": "This is a sample tweet!",
            "user": {
                "name": "John Doe",
                "screen_name": "johndoe",
                "location": "San Francisco, CA"
            },
            "created_at": datetime.now().strftime("%a %b %d %H:%M:%S +0000 %Y"),
            "retweet_count": random.randint(0, 100),
            "favorite_count": random.randint(0, 100),
            "hashtags": ["sample", "tweet", "python"],
            "urls": [],
            "mentions": []
        }

        jresult = json.dumps(tweet)
        producer.produce(topic, key=p_key, value=jresult, callback=acked)
        producer.flush()

        time.sleep(2)

if __name__ == "__main__":
    main()
