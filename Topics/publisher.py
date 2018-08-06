import pika
import sys

# topics in the form of <University>.<department>.<person_type>
# example cu.journalism.faculty; cu.engineering.student; cu.IT.admin; cu.finance.admin
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='person11', exchange_type='topic')

topic_key = sys.argv[1] if len(sys.argv) > 2 else 'anybody.info'
message = ''.join(sys.argv[1:]) or "ss4878"
channel.basic_publish(exchange='person11', routing_key=topic_key, body=message)

print(" [x] sent %r" % message)

connection.close()