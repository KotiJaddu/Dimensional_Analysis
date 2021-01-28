import helper_functions
import sys

def generate_default_matrices_general_generator(max_dimension_x, max_dimension_y):
	for dimension_x in range(max_dimension_x + 1):
		for dimension_y in range(dimension_x + 1, max_dimension_y + 1):
			matrix = helper_functions.generate_null_matrix(dimension_x + 1, dimension_y)
			matrix = helper_functions.initialise_matrix_general_generator(matrix, dimension_x, dimension_y)
			with open('storage/' + str(dimension_x) + '_' + str(dimension_y) + '.txt', 'w') as f:
				print(matrix, file=f)
			f.close()


if __name__ == "__main__":
	generate_default_matrices_general_generator(int(sys.argv[1]), int(sys.argv[2]))
