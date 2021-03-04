from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': "pkc-419q3.us-east4.gcp.confluent.cloud:9092",
        'client.id': socket.gethostname()}

topic = 'cheese'

producer = Producer(conf)

producer.produce(topic, key='cheddar', value='good')

producer.poll(1)


