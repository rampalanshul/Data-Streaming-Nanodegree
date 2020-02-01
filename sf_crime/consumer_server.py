from kafka import KafkaConsumer
import time

def consume(topic_list):
    consumer = KafkaConsumer(topic_list, bootstrap_servers="localhost:8082" )
    while(true):
        messages = consumer.poll()
        print(messages)
        time.sleep(10)


if __name__ == "__main__":
    topic_list = ['org.police.calls.v1']
    consume(topic_list)