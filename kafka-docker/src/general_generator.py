#!/usr/bin/python
import sys
import pandas as pd
from sympy import symbols, Matrix
import io
import helper_functions

# This class is too long and not tested. We need to write down in sentences what this class does and translate the  words into
# unit tests so that we can refactor this class.


class Model():
	def generate(self, dimension_x, dimension_y):
		matrix = helper_functions.Initialise_Matrix(dimension_x + 1, dimension_y)

		for i in range(0, dimension_y):
		    matrix[0][i] = "A_{" + str(i) + "} - \\alpha_{0," + str(i) + "}"
		    for j in range(1, dimension_x + 1):
		        matrix[j][i] = "\\alpha_{" + str(j) + "," + str(i) + "} - \\alpha_{0," + str(i) + "}"

		output = helper_functions.Headers() 
		output = helper_functions.Introduction(output, dimension_x, dimension_y)

		if (dimension_x + 1 == dimension_y):
			output = helper_functions.Equation_Output_Case1(output, helper_functions.Calculate_Determinant(matrix))
		else:
			output = helper_functions.Equation_Output_Case2(output, matrix, True, helper_functions.Calculate_Determinant, dimension_x, dimension_y)
		return output + "</p>\n</body>\n</html>"


