#!/usr/bin/python
import sys
import pandas as pd
from sympy import symbols, Matrix
import io
import helper_functions

# This class is too long and not tested. We need to write down in sentences what this class does and translate the  words into
# unit tests so that we can refactor this class.


class Model():
	def generate_dimensional_analysis_html_script(self, dimension_x, dimension_y, default_matrices, MAX_DEFAULT_MATRIX_LENGTH):
		matrix = helper_functions.generate_null_matrix(dimension_x + 1, dimension_y)
		matrix = helper_functions.check_default_matrices(matrix, default_matrices, dimension_x, dimension_y, MAX_DEFAULT_MATRIX_LENGTH)

		output = helper_functions.generate_html_header() 
		output = helper_functions.generate_definitions_and_variables(output, dimension_x, dimension_y)

		if (dimension_x + 1 == dimension_y):
			output = helper_functions.generate_equation_output_case_1(output, helper_functions.generate_determinant(matrix))
			return helper_functions.generate_html_footer(output)
		output = helper_functions.generate_equation_output_case_2(output, matrix, True, helper_functions.generate_determinant, dimension_x, dimension_y)
		return helper_functions.generate_html_footer(output)


