import pika

credentials = pika.PlainCredentials('user', 'password')

connection = pika.BlockingConnection(pika.ConnectionParameters(
    '127.0.0.1', 5672, '/', credentials))
channel = connection.channel()



channel.queue_declare(queue='hello')

for i in range(500000):
    channel.basic_publish(exchange='', routing_key='hello', body='message {}'.format(i))
    print(" [{}]  message'".format(i))   
connection.close()