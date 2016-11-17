#!/usr/bin/python

import sys
import pika

queue_name = 'task_queue'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue=queue_name)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='', 
        routing_key=queue_name,
        body=message,
        properties=pika.BasicProperties(
            delivery_mode = 2,
            )
        )

print(" [x] Sent %r" % message)
connection.close()
