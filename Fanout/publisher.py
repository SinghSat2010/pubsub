import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='person', exchange_type='fanout')

message = ''.join(sys.argv[1:]) or "ss4878"
channel.basic_publish(exchange='person', routing_key='', body=message)

print(" [x] sent %r" % message)

connection.close()