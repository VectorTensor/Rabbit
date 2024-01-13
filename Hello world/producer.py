import json
import pika
import sys


class Producer:
    def __init__(self):

        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

        self.channel = self.connection.channel()

    def produce(self):
        self.channel.queue_declare(queue='hello')
        self.channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

        print("Sent hello world")



producer = Producer()

producer.produce()
