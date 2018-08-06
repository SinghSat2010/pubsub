import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='queue1', type='fanout')

channel.basic_publish(exchange='', routing_key='queue1', body='Hi there')

print(" [x] sent 'Hi there!'")

connection.close()