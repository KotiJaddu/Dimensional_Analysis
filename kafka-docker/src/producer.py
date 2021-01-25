import messageQueues
import sys

topic = sys.argv[1]
producer = messageQueues.generate_producer()
while True:
	if topic == "general_generator":
		msg = input("Input dimensions: ")
	else:
		msg = input("Input points: ")
	future = producer.send(topic, msg.encode("utf-8"))
	print(f"Sending msg: {msg}")
	result = future.get(timeout=10)

	metrics = producer.metrics()
	print(metrics)