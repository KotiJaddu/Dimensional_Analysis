#!/usr/bin/python
import sys
import pandas as pd
from kafka import KafkaConsumer
import webbrowser
from sympy import symbols, Matrix
import io

class Specific_Satisfier():
	def satisfy(self, points):
		dimension_x = points.shape[0] - 2
		dimension_y = points.shape[1]
		matrix = [0] * (dimension_x + 1)
		for i in range(0, dimension_x + 1):
			matrix[i] = [0] * dimension_y

		for i in range(0, dimension_y):
			matrix[0][i] = float(points[i][len(points) - 1]) - float(points[i][0])
			for j in range(1, dimension_x + 1):
				matrix[j][i] = float(points[i][j]) - float(points[i][0])

		dimension_xs = str(dimension_x)
		dimension_ys = str(dimension_y)
		output = "<!DOCTYPE html>\n<html>\n<head>\n<meta charset=""utf-8"">\n<meta name=""viewport"" content=""width=device-width"">\n<title>Dimensional Analysis</title>\n<script src=""https://polyfill.io/v3/polyfill.min.js?features=es6""></script>\n<script id=""MathJax-script"" async\nsrc=""https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"">\n</script>\n</head>\n<body>\n<p>\n"

		if (dimension_x + 1 == dimension_y):
			output = output + "To represent a " + dimension_xs + "D object in " + dimension_ys + "D space, there is only one equation that needs to be satisfied in order to check whether the point\n\\[("
		else:
			output = output + "To represent a " + dimension_xs + "D object in " + dimension_ys + "D space, there are " + str(dimension_y - dimension_x) + " equations that need to be satisfied in order to check whether the point\n\\[("
		if (dimension_y == 1):
			output = output + "A_{0}"
		else:
			if (dimension_y < 4):
				for i in range(0, dimension_y):
					if (i == 0):
						output = output + "A_{" + str(i) + "}"
					else:
						output = output + ", A_{" + str(i) + "}"    
			else:
				output = output + "A_0, ..., A_{" + str(dimension_y - 1) + "}"
		output = output + ")\\]\nin " + dimension_ys + "D space lies on the " + dimension_xs + "D object defined by the point(s)\n"
		
		if (dimension_y >= 4 and dimension_x == 1):
			output = output + "\\[(\\alpha_{0,0},...,\\alpha_{0," + str(dimension_y - 1) + "}), (\\alpha_{" + dimension_xs + ",0},...,\\alpha_{" + dimension_xs + "," + str(dimension_y - 1) + "}) "
		else:
			if (dimension_y < 4):
				output = output + "\\["
				for i in range(0, dimension_x + 1):
					if (i == 0):
						output = output + "("
					else:
						output = output + ", ("
					for j in range(0, dimension_y):
						if (j == 0):
							output = output + "\\alpha_{" + str(i) + "," + str(j) + "}"
						else:
							output = output + ", \\alpha_{" + str(i) + "," + str(j) + "}"
					output = output + ")"
			else:
				output = output + " \\[(\\alpha_{0,0},...,\\alpha_{0," + str(dimension_y - 1) + "}), ..., (\\alpha_{" + dimension_xs + ",0},...,\\alpha_{" + dimension_xs + "," + str(dimension_y - 1) + "})"
		output = output + "\\] which all lie on that " + dimension_xs + "D object.<br><br>\n"

		if (dimension_x + 1 == dimension_y):
			output = output + "Equation 1 to be satisfied:\n"
			with open('determinant.txt', 'w') as f:
				print(Matrix(matrix).det(), file=f)
			f = open("determinant.txt", "r")
			output = output + "\\[" + f.read() + "= 0\\]\n</p>\n</body>\n</html>"
			f.close()
		else:
			output = output + "Equation 1 to be satisfied:\n"
			new_matrix = [0] * (dimension_x + 1)
			for i in range(0, dimension_x + 1):
				new_matrix[i] = [0] * (dimension_x + 1)
			for i in range(0, dimension_x + 1):
				for j in range(0, dimension_x + 1):
					new_matrix[i][j] = matrix[i][j]
			with open('determinant.txt', 'w') as f:
				print(Matrix(new_matrix).det(), file=f)
			f = open("determinant.txt", "r")
			output = output + "\\[" + f.read() + "= 0\\]\n"
			f.close()
			for k in range(0, dimension_y - dimension_x - 1):
				new_matrix = [0] * (dimension_x + 1)
				for i in range(0, dimension_x + 1):
					new_matrix[i] = [0] * (dimension_x + 1)
				if (dimension_x > 0):
					for i in range(1, dimension_x + 1):
						for j in range(0, dimension_x + 1):
							new_matrix[j][i] = matrix[j][i]
				for j in range(0, dimension_x + 1):
					new_matrix[j][0] = matrix[j][dimension_y - k - 1]
				output = output + "<br>Equation " + str(k + 2) + " to be satisfied:\n"
				with open('determinant.txt', 'w') as f:
					print(Matrix(new_matrix).det(), file=f)
				f = open("determinant.txt", "r")
				output = output + "\\[" + f.read() + "= 0\\]\n"
				f.close()
		output = output + "</p>\n</body>\n</html>"
		return output

if __name__ == '__main__':
	specific_satisfier_consumer = KafkaConsumer('specific_satisfier', bootstrap_servers='localhost:55001', auto_offset_reset='earliest')
	for msg in specific_satisfier_consumer:
		msg_string = msg.value.decode('utf-8')
		manipulated_msg_string = msg_string.replace(";", "\n")
		data = io.StringIO("""""" + manipulated_msg_string + """""")
		df = pd.read_csv(data, sep=",", header=None)
		specific_satisfier = Specific_Satisfier()
		f = open("specific_satisfier.html", "w")
		f.write(specific_satisfier.satisfy(df))
		f.close()
		webbrowser.open("C:\\Users\\kjaddu001\\Desktop\\kafka-docker\\src\\specific_satisfier.html",new=2)
