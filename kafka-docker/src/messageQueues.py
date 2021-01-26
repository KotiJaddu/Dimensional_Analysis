from kafka import KafkaProducer, KafkaConsumer
import subprocess

# messageQueue might not be the best mame. Another suggestion: 'KafkaComponents'

# Every module should have taks which are related. Here we create Kafka components (producer, consumere)
# The configuration of Kafka could b done by another module which will be imported into kafka.
# you created a file called setup.py -> does get_port fit to this module?

def get_PORT():
  return str(subprocess.check_output(['docker-compose', 'ps'], shell=True)).split(':')[1].split('-')[0]

def generate_producer():
  producer = KafkaProducer(bootstrap_servers='localhost:' + get_PORT())
  return producer

def generate_consumer(topic):
  consumer = KafkaConsumer(topic, bootstrap_servers='localhost:' + get_PORT(), auto_offset_reset='earliest')
  return consumer