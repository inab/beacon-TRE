#!/usr/bin/env python
import pika
import requests
import json
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def sendPost(jsonFile):
    # Always the same request for now
    jsonFile = str(jsonFile).replace('True', 'true').replace('False', 'false')
    jsonFile = str(jsonFile).replace("'", '"')
    jsonFile = json.loads(jsonFile)
    queryPost = jsonFile["queryPost"]
    urlEndpoint = jsonFile["url"]

    url = f'{mainUrl}/{urlEndpoint}'

    x = requests.post(url, json = queryPost)
    return x.text

def on_request(ch, method, props, body):
    response = sendPost(body.decode('utf-8'))

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

mainUrl = sys.argv[1]

print(" [x] Awaiting RPC requests")
channel.start_consuming()