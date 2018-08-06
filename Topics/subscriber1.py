import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='person11', exchange_type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

person_types = sys.argv[1:]
if not person_types:
    sys.stderr.write("Usage: %s [person type]  \n" % sys.argv[0])
    sys.exit(1)

for person_type in person_types:
    channel.queue_bind(exchange='person11', queue=queue_name, routing_key=person_type)
    print("registered for topic %r" % person_type)

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print( " [x] %r: %r" % (method.routing_key, body))

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()