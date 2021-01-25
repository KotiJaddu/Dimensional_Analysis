from kafka import KafkaProducer, KafkaConsumer
import subprocess


def get_PORT():
	return str(subprocess.check_output(['docker-compose', 'ps'], shell=True)).split(':')[1].split('-')[0]


def generate_producer():
	producer = KafkaProducer(bootstrap_servers='localhost:' + get_PORT())
	return producer

def generate_consumer(topic):
	consumer = KafkaConsumer(topic, bootstrap_servers='localhost:' + get_PORT(), auto_offset_reset='earliest')
	return consumer