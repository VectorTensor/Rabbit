import json
import pika
import sys


class Consumer:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

        self.channel = self.connection.channel()

    def _init_queue(self):
        self.channel.queue_declare(queue='hello')

    def consume(self):
        self._init_queue()
        self.channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback_fnc)
        self.channel.start_consuming()


def callback_fnc(ch, method, properties, body):
    print("received " + body.decode('utf-8'))


consumer = Consumer()

consumer.consume()
