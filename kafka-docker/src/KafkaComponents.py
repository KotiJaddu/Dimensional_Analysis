from kafka import KafkaProducer, KafkaConsumer
import setup
import subprocess

# messageQueue might not be the best mame. Another suggestion: 'KafkaComponents' -- CHANGED

# Every module should have taks which are related. Here we create Kafka components (producer, consumer) -- UNDERSTOOD
# The configuration of Kafka could b done by another module which will be imported into kafka. -- ?
# you created a file called setup.py -> does get_port fit to this module? -- MOVED

def generate_producer():
  producer = KafkaProducer(bootstrap_servers='localhost:' + setup.get_PORT())
  return producer

def generate_consumer(topic):
  consumer = KafkaConsumer(topic, bootstrap_servers='localhost:' + setup.get_PORT(), auto_offset_reset='earliest')
  return consumer