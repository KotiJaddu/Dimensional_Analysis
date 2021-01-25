from kafka import KafkaProducer

topic = "general_generator"
producer = KafkaProducer(bootstrap_servers='localhost:55001')
while True:
	msg = input("Input dimensions: ")
	future = producer.send(topic, msg.encode("utf-8"))
	print(f"Sending msg: {msg}")
	result = future.get(timeout=10)

	metrics = producer.metrics()
	print(metrics)