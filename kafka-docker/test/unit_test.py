import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"src"
)
sys.path.append(SOURCE_PATH)
sys.path.append("../src")
import helper_functions
import unittest
from sympy import symbols

class TestHelperFunctions(unittest.TestCase):

	def test_generate_html_header_should_get_correct_header(self):
		assert helper_functions.generate_html_header() == "<!DOCTYPE html>\n<html>\n<head>\n<meta charset=""utf-8"">\n<meta name=""viewport"" content=""width=device-width"">\n<title>Dimensional Analysis</title>\n<script src=""https://polyfill.io/v3/polyfill.min.js?features=es6""></script>\n<script id=""MathJax-script"" async\nsrc=""https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"">\n</script>\n</head>\n<body>\n<p>\n"

	def test_generate_html_header_should_get_incorrect_header(self):
		self.assertNotEqual("", helper_functions.generate_html_header())
		
	def test_generate_null_matrix_should_get_correct_size(self):
		matrix = helper_functions.generate_null_matrix(1, 3)
		assert(len(matrix)) == 1
		assert(len(matrix[0])) == 3

	def test_generate_null_matrix_should_contain_zeroes(self):
		matrix = helper_functions.generate_null_matrix(1, 4)
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				assert matrix[i][j] == 0

	def test_initialise_matrix_general_generator_should_return_correct_matrix(self):
		matrix = helper_functions.generate_null_matrix(2, 2)
		matrix = helper_functions.initialise_matrix_general_generator(matrix, 1, 2)
		assert matrix == [['A_{0} - \\alpha_{0,0}', 'A_{1} - \\alpha_{0,1}'], ['\\alpha_{1,0} - \\alpha_{0,0}', '\\alpha_{1,1} - \\alpha_{0,1}']]

	def test_initialise_matrix_general_generator_should_return_incorrect_matrix(self):
		matrix = helper_functions.generate_null_matrix(2, 2)
		matrix = helper_functions.initialise_matrix_general_generator(matrix, 1, 2)
		self.assertNotEqual(matrix, [['', ''], ['', '']])

	def test_initialise_matrix_specific_generator_should_return_correct_matrix(self):
		matrix = helper_functions.generate_null_matrix(2, 2)
		matrix = helper_functions.initialise_matrix_specific_generator(matrix, [[1,2],[3,4]], 1, 2)
		assert str(matrix) == "[[A_0 - 1.0, A_1 - 3.0], [1.0, 1.0]]"

	def test_initialise_matrix_specific_generator_should_return_incorrect_matrix(self):
		matrix = helper_functions.generate_null_matrix(2, 2)
		matrix = helper_functions.initialise_matrix_specific_generator(matrix, [[1,2],[3,4]], 1, 2)
		self.assertNotEqual(matrix, [[1, 2], [3, 4]])

	def test_initialise_matrix_specific_satisfier_should_return_correct_matrix(self):
		matrix = helper_functions.generate_null_matrix(1, 1)
		matrix = helper_functions.initialise_matrix_specific_satisfier(matrix, [[1,2],[3,4]], 0, 1)
		assert str(matrix) == "[[1.0]]"

	def test_initialise_matrix_specific_satisfier_should_return_incorrect_matrix(self):
		matrix = helper_functions.generate_null_matrix(1, 1)
		matrix = helper_functions.initialise_matrix_specific_satisfier(matrix, [[1,2],[3,4]], 0, 1)
		self.assertNotEqual(matrix, [[0]])

	def test_generate_spacial_definition_should_get_correct_string_based_on_dimensions(self):
		assert helper_functions.generate_spacial_definition("", 1, 2) == "To represent a 1D object in 2D space, there is only one equation that needs to be satisfied in order to check whether the point\n\\[("

	def test_generate_spacial_definition_should_not_get_correct_string_based_on_dimensions(self):
		self.assertNotEqual("", helper_functions.generate_spacial_definition("", 1, 2) == "To represent a 1D object in 2D space, there is only one equation that needs to be satisfied in order to check whether the point\n\\[(")
			
	def test_generate_spacial_variables_should_get_correct_description_based_on_dimensions(self):
		assert helper_functions.generate_spacial_variables("", 1, 2) == "A_{0}, A_{1}"

	def test_generate_spacial_variables_should_not_get_correct_description_based_on_dimensions(self):
		self.assertNotEqual("", helper_functions.generate_spacial_variables("", 2, 4))

	def test_generate_object_definition_should_get_correct_string_based_on_dimensions(self):
		assert helper_functions.generate_object_definition("", 1, 2) == ")\\]\nin 2D space lies on the 1D object defined by the point(s)\n"

	def test_generate_object_definition_should_not_get_correct_string_based_on_dimensions(self):
		self.assertNotEqual("", helper_functions.generate_object_definition("", 1, 4))
	
	def test_generate_object_variables_should_get_correct_description_based_on_dimensions(self):
		assert helper_functions.generate_object_variables("", 1, 2) == "\\[(\\alpha_{0,0}, \\alpha_{0,1}), (\\alpha_{1,0}, \\alpha_{1,1})\\] which all lie on that 1D object.<br><br>\n"

	def test_generate_object_variables_should_not_get_correct_description_based_on_dimensions(self):
		self.assertNotEqual("", helper_functions.generate_object_variables("", 2, 3))

	def test_generate_definitions_and_variables_should_get_correct_description_based_on_dimensions(self):
		assert helper_functions.generate_definitions_and_variables("", 3, 5) == "To represent a 3D object in 5D space, there are 2 equations that need to be satisfied in order to check whether the point\n\\[(A_0, ..., A_{4})\\]\nin 5D space lies on the 3D object defined by the point(s)\n \\[(\\alpha_{0,0},...,\\alpha_{0,4}), ..., (\\alpha_{3,0},...,\\alpha_{3,4})\\] which all lie on that 3D object.<br><br>\n"

	def test_generate_definitions_and_variables_should_get_incorrect_description_based_on_dimensions(self):
		self.assertNotEqual("", helper_functions.generate_definitions_and_variables("", 3, 4))

	def test_generate_determinant_as_string_should_get_correct_determinant(self):
		matrix = helper_functions.generate_null_matrix(2, 2)
		matrix = helper_functions.initialise_matrix_specific_generator(matrix, [[1,2],[3,4]], 1, 2)
		assert helper_functions.generate_determinant_as_string(matrix) == '1.0*A_0 - 1.0*A_1 + 2.0\n'

	def test_generate_determinant_as_string_should_get_incorrect_determinant(self):
		matrix = helper_functions.generate_null_matrix(2, 2)
		matrix = helper_functions.initialise_matrix_specific_generator(matrix, [[1,2],[3,4]], 1, 2)
		self.assertNotEqual("", helper_functions.generate_determinant_as_string(matrix))

	def test_generate_determinant_should_get_correct_determinant(self):
		matrix = helper_functions.generate_null_matrix(2, 2)
		matrix = helper_functions.initialise_matrix_general_generator(matrix, 1, 2)
		assert helper_functions.generate_determinant(matrix) == '(A_{0} - \\alpha_{0,0})[\\alpha_{1,1} - \\alpha_{0,1}]\n - (A_{1} - \\alpha_{0,1})[\\alpha_{1,0} - \\alpha_{0,0}]\n'

	def test_generate_determinant_should_get_incorrect_determinant(self):
		matrix = helper_functions.generate_null_matrix(2, 2)
		matrix = helper_functions.initialise_matrix_general_generator(matrix, 1, 2)
		self.assertNotEqual("", helper_functions.generate_determinant(matrix))

	def test_generate_equation_output_case_1_should_get_correct_equations_for_general_generator(self):
		matrix = helper_functions.generate_null_matrix(2, 2)
		matrix = helper_functions.initialise_matrix_general_generator(matrix, 1, 2)
		assert helper_functions.generate_equation_output_case_1("", helper_functions.generate_determinant(matrix)) == "Equation 1 to be satisfied:\n\\[(A_{0} - \\alpha_{0,0})[\\alpha_{1,1} - \\alpha_{0,1}]\n - (A_{1} - \\alpha_{0,1})[\\alpha_{1,0} - \\alpha_{0,0}]\n= 0\\]\n</p>\n</body>\n</html>"
	
	def test_generate_equation_output_case_1_should_get_incorrect_equations_for_general_generator(self):
		matrix = helper_functions.generate_null_matrix(2, 2)
		matrix = helper_functions.initialise_matrix_general_generator(matrix, 1, 2)
		self.assertNotEqual("", helper_functions.generate_equation_output_case_1("", helper_functions.generate_determinant(matrix)))

	def test_generate_equation_output_case_1_should_get_correct_equations_for_specific_generator(self):
		matrix = helper_functions.generate_null_matrix(2, 2)
		matrix = helper_functions.initialise_matrix_specific_generator(matrix, [[1,2], [3,4]], 1, 2)
		assert helper_functions.generate_equation_output_case_1("", helper_functions.generate_determinant_as_string(matrix)) == "Equation 1 to be satisfied:\n\\[1.0*A_0 - 1.0*A_1 + 2.0\n= 0\\]\n</p>\n</body>\n</html>"
	
	def test_generate_equation_output_case_1_should_get_incorrect_equations_for_specific_generator(self):
		matrix = helper_functions.generate_null_matrix(2, 2)
		matrix = helper_functions.initialise_matrix_specific_generator(matrix, [[1,2], [3,4]], 1, 2)
		self.assertNotEqual("", helper_functions.generate_equation_output_case_1("", helper_functions.generate_determinant_as_string(matrix)))
	
	def test_generate_equation_output_case_1_should_get_correct_equations_for_specific_satisfier(self):
		matrix = helper_functions.generate_null_matrix(1, 1)
		matrix = helper_functions.initialise_matrix_specific_satisfier(matrix, [[1,2], [3,4]], 0, 1)
		assert helper_functions.generate_equation_output_case_1("", helper_functions.generate_determinant_as_string(matrix)) == "Equation 1 to be satisfied:\n\\[1.00000000000000\n= 0\\]\n</p>\n</body>\n</html>"
	
	def test_generate_equation_output_case_1_should_get_incorrect_equations_for_specific_satisfier(self):
		matrix = helper_functions.generate_null_matrix(1, 1)
		matrix = helper_functions.initialise_matrix_specific_satisfier(matrix, [[1,2], [3,4]], 0, 1)
		self.assertNotEqual("", helper_functions.generate_equation_output_case_1("", helper_functions.generate_determinant_as_string(matrix)))

	def test_generate_equation_output_case_2_should_get_correct_equations_for_general_generator(self):
		matrix = helper_functions.generate_null_matrix(1, 2)
		matrix = helper_functions.initialise_matrix_general_generator(matrix, 0, 2)
		assert helper_functions.generate_equation_output_case_2("", matrix, True, helper_functions.generate_determinant, 0, 2) == "Equation 1 to be satisfied:\n\\[A_{0} - \\alpha_{0,0}= 0\\]\n<br>Equation 2 to be satisfied:\n\\[A_{0} - \\alpha_{0,0}= 0\\]\n"
	
	def test_generate_equation_output_case_2_should_get_incorrect_equations_for_general_generator(self):
		matrix = helper_functions.generate_null_matrix(1, 2)
		matrix = helper_functions.initialise_matrix_general_generator(matrix, 0, 2)
		self.assertNotEqual("", helper_functions.generate_equation_output_case_2("", matrix, True, helper_functions.generate_determinant, 0, 2))

	def test_generate_equation_output_case_2_should_get_correct_equations_for_specific_generator(self):
		matrix = helper_functions.generate_null_matrix(1, 2)
		matrix = helper_functions.initialise_matrix_specific_generator(matrix, [[1],[2]], 0, 2)
		assert helper_functions.generate_equation_output_case_2("", matrix, False, helper_functions.generate_determinant_as_string, 0, 2) == "Equation 1 to be satisfied:\n\\[A_0 - 1.0\n= 0\\]\n<br>Equation 2 to be satisfied:\n\\[A_1 - 2.0\n= 0\\]\n"
	
	def test_generate_equation_output_case_2_should_get_incorrect_equations_for_specific_generator(self):
		matrix = helper_functions.generate_null_matrix(1, 2)
		matrix = helper_functions.initialise_matrix_specific_generator(matrix, [[1],[2]], 0, 2)
		self.assertNotEqual("", helper_functions.generate_equation_output_case_2("", matrix, False, helper_functions.generate_determinant_as_string, 0, 2))

	def test_generate_equation_output_case_2_should_get_correct_equations_for_specific_satisfier(self):
		matrix = helper_functions.generate_null_matrix(1, 2)
		matrix = helper_functions.initialise_matrix_specific_satisfier(matrix, [[1,2], [1,3]], 0, 2)
		assert helper_functions.generate_equation_output_case_2("", matrix, False, helper_functions.generate_determinant_as_string, 0, 2) == "Equation 1 to be satisfied:\n\\[1.00000000000000\n= 0\\]\n<br>Equation 2 to be satisfied:\n\\[2.00000000000000\n= 0\\]\n"
	
	def test_generate_equation_output_case_2_should_get_incorrect_equations_for_specific_satisfier(self):
		matrix = helper_functions.generate_null_matrix(1, 2)
		matrix = helper_functions.initialise_matrix_specific_satisfier(matrix, [[1,2], [1,3]], 0, 2)
		self.assertNotEqual("", helper_functions.generate_equation_output_case_2("", matrix, False, helper_functions.generate_determinant_as_string, 0, 2))

	def test_generate_html_footer_should_get_correct_header(self):
		assert helper_functions.generate_html_footer("") == "</p>\n</body>\n</html>"

	def test_generate_html_footer_should_get_incorrect_header(self):
		self.assertNotEqual("", helper_functions.generate_html_footer(""))

if __name__ == '__main__':
  unittest.main()
