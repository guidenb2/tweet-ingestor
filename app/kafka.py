import socket
from confluent_kafka import Producer

def init_producer():
    conf = {'bootstrap.servers': 'localhost:9093',
            'client.id': socket.gethostname()}
    return Producer(conf)

def acked(err, _):
    if err is not None:
        print("Failed to add tweet to topic: %s" % (str(err)))
    else:
        print("Tweet added to topic successfully")