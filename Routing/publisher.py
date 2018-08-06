import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='person1', exchange_type='direct')

person_type = sys.argv[1] if len(sys.argv) > 2 else 'researcher'
message = ''.join(sys.argv[1:]) or "ss4878"
channel.basic_publish(exchange='person1', routing_key=person_type, body=message)

print(" [x] sent %r" % message)

connection.close()