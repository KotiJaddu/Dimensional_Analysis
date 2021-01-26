import subprocess

def get_PORT():
	return str(subprocess.check_output(['docker-compose', 'ps'], shell=True)).split(':')[1].split('-')[0]

IP_ADDRESS = str(subprocess.check_output(['ipconfig'], shell=True)).split(':')[3].split('\\')[0].split(' ')[1]
reading_file = open("../docker-compose.yml", "r")

new_file_content = ""
for line in reading_file:
	if (line.find("KAFKA_ADVERTISED_HOST_NAME:") != -1):
		new_file_content += "      KAFKA_ADVERTISED_HOST_NAME: " + IP_ADDRESS + "\n"
	else:
		new_file_content += line
reading_file.close()

writing_file = open("../docker-compose.yml", "w")
writing_file.write(new_file_content)
writing_file.close()

subprocess.run(['docker-compose', 'down'], shell=True)
subprocess.run(['docker-compose', 'up', '-d'], shell=True)

