from kafka import KafkaProducer

def generate_producer(topic):
	producer = KafkaProducer(bootstrap_servers='localhost:55003')
	return producer
