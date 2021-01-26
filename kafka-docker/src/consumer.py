import KafkaComponents
import sys
import pandas as pd
import specific_generator, general_generator, specific_generator
import io
import webbrowser
import os

topic = sys.argv[1]
consumer = KafkaComponents.generate_consumer(topic)
for msg in consumer:
	msg_string = msg.value.decode('utf-8')
	manipulated_msg_string = msg_string.replace(";", "\n")
	df = pd.read_csv(io.StringIO("""""" + manipulated_msg_string + """"""), sep=",", header=None)
	f = open("generator.html", "w")
	if (topic == "general_generator"):
		split_msg = msg_string.split(',')
		f.write(general_generator.Model().generate(int(split_msg[0]), int(split_msg[1])))
	elif (topic == "specific_generator"):
		f.write(specific_generator.Model().generate(df))
	elif (topic == "specific_satisfier"):
		f.write(specific_satisfier.Model().generate(df))
	f.close()
	webbrowser.open(os.path.abspath("generator.html"), new=2)
