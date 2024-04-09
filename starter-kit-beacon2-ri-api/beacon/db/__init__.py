from pymongo.mongo_client import MongoClient
from beacon import conf

client = ""


#!/usr/bin/env python
import pika
import uuid
import sys


class BeaconRpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n))
        while self.response is None:
            self.connection.process_data_events(time_limit=None)
        return self.response


# beacon_rpc = BeaconRpcClient()


# # Take JSON file for post
# inputPost = sys.argv[1]

# with open(inputPost) as user_file:
#   parsed_json = user_file.read()

# print(" [x] Requesting beacon query")
# response = beacon_rpc.call(parsed_json)
# print(f" [.] Got response")
# print(response)