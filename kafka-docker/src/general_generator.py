#!/usr/bin/python
import sys
import pandas as pd
from sympy import symbols, Matrix
import io

# This class is too long and not tested. We need to write down in sentences what this class does and translate the  words into
# unit tests so that we can refactor this class.

def determinant(matrix):
	dimension = len(matrix)
	if (dimension == 1):
		return matrix[0][0]
	output = ""
	for k in range(0, dimension):
		fill_x = 0
		fill_y = 0
		new_matrix = [0] * (dimension - 1)
		for i in range(0, dimension - 1):
			new_matrix[i] = [0] * (dimension - 1)
		for i in range(1, dimension):
			for j in range(0, dimension):
				if (j != k):
					new_matrix[fill_x % dimension][fill_y] = matrix[i][j];
					fill_y = fill_y + 1
					if (fill_y % dimension == dimension - 1):
						fill_y = 0;
						fill_x = fill_x + 1
		if (k != 0):
			if (k % 2 == 0):
				output += " + "
			else:
				output += " - "
		output += "(" + matrix[0][k] + ")[" + determinant(new_matrix) + "]\n"
	return output


class Model():
	def generate(self, dimension_x, dimension_y):
		matrix = [0] * (dimension_x + 1)
		for i in range(0, dimension_x + 1):
			matrix[i] = [0] * dimension_y

		for i in range(0, dimension_y):
		    matrix[0][i] = "A_{" + str(i) + "} - \\alpha_{0," + str(i) + "}"
		    for j in range(1, dimension_x + 1):
		        matrix[j][i] = "\\alpha_{" + str(j) + "," + str(i) + "} - \\alpha_{0," + str(i) + "}"

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
			output = output + "\\[" + determinant(matrix) + "= 0\\]\n</p>\n</body>\n</html>"

		else:
			output = output + "Equation 1 to be satisfied:\n"
			new_matrix = [0] * (dimension_x + 1)
			for i in range(0, dimension_x + 1):
				new_matrix[i] = [0] * (dimension_x + 1)
			for i in range(0, dimension_x + 1):
				for j in range(0, dimension_x + 1):
					new_matrix[i][j] = matrix[i][j]
			output = output + "\\[" + determinant(matrix) + "= 0\\]\n"
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
				output = output + "\\[" + determinant(matrix) + "= 0\\]\n"
		output = output + "</p>\n</body>\n</html>"
		return output


