from confluent_kafka import Producer

conf = {'bootstrap.servers': "pkc-419q3.us-east4.gcp.confluent.cloud:9092"}

topic = 'cheese'

producer = Producer(conf)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

producer.produce(topic, key='cheddar', value='good', on_delivery=acked)

producer.poll(1)


