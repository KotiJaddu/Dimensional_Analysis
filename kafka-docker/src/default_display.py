import helper_functions
import sys

def generate_default_matrices_general_generator(max_dimension_x, max_dimension_y):
	default_matrices = []
	for dimension_x in range(max_dimension_x + 1):
		for dimension_y in range(dimension_x + 1, max_dimension_y + 1):
			matrix = helper_functions.generate_null_matrix(dimension_x + 1, dimension_y)
			matrix = helper_functions.initialise_matrix_general_generator(matrix, dimension_x, dimension_y)
			default_matrices.append(matrix)
	return default_matrices

