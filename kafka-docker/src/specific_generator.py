#!/usr/bin/python
import sys
import pandas as pd
from sympy import symbols, Matrix
import io
import helper_functions

# This class is too long and not tested. We need to write down in sentences what this class does and translate the  words into
# unit tests so that we can refactor this class.

class Model():
	def generate(self, points):
		dimension_x = points.shape[0] - 1
		dimension_y = points.shape[1]
		matrix = helper_functions.Initialise_Matrix(dimension_x + 1, dimension_y)

		for i in range(0, dimension_y):
			matrix[0][i] = symbols('A_0:' + str(dimension_y))[i] - float(points[i][0])
			for j in range(1, dimension_x + 1):
				matrix[j][i] = float(points[i][j]) - float(points[i][0])

		output = helper_functions.Headers()
		output = helper_functions.Introduction(output, dimension_x, dimension_y)

		if (dimension_x + 1 == dimension_y):
			output = helper_functions.Equation_Output_Case1(output, helper_functions.Determinant_Read(matrix))
		else:
			output = helper_functions.Equation_Output_Case2(output, matrix, False, helper_functions.Determinant_Read, dimension_x, dimension_y)
		return output + "</p>\n</body>\n</html>"
