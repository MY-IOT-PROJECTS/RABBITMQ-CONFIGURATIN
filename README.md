## For every thing start first of all I will try to test docker without installing

follow the docker.sh

#### hello world

python -m pip install pika --upgrade

we must run the reciver file i have run it with 2  process

and after that run send oucatinally
you will see that ervey time it recvi one of our thread

recive.py
```python
import pika

credentials = pika.PlainCredentials('user', 'password')

connection = pika.BlockingConnection(pika.ConnectionParameters(
    '127.0.0.1', 5672, '/', credentials))
channel = connection.channel()


channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

```

send.py
```python
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
```


![ ](/images/001.png)
![ ](/images/002.png)
![ ](/images/003.png)
![ ](/images/004.png)