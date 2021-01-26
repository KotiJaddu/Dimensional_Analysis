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

class unit_test(unittest.TestCase):

	def test_Headers(self):
		assert helper_functions.Headers() == "<!DOCTYPE html>\n<html>\n<head>\n<meta charset=""utf-8"">\n<meta name=""viewport"" content=""width=device-width"">\n<title>Dimensional Analysis</title>\n<script src=""https://polyfill.io/v3/polyfill.min.js?features=es6""></script>\n<script id=""MathJax-script"" async\nsrc=""https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"">\n</script>\n</head>\n<body>\n<p>\n"
	
	def test_Initialise_Matrix(self):
		matrix = helper_functions.Initialise_Matrix(1, 3)
		assert(len(matrix)) == 2
		assert(len(matrix[0])) == 3

	def test_Introduction_Spacial_Definition(self):
		assert helper_functions.Introduction_Spacial_Definition("", 1, 2) == "To represent a 1D object in 2D space, there is only one equation that needs to be satisfied in order to check whether the point\n\\[("
	
	def test_Introduction_Spacial_Variables(self):
		assert helper_functions.Introduction_Spacial_Variables("", 1, 2) == "A_{0}, A_{1}"

	def test_Introduction_Object_Definition(self):
		assert helper_functions.Introduction_Object_Definition("", 1, 2) == ")\\]\nin 2D space lies on the 1D object defined by the point(s)\n"

	def test_Introduction_Object_Variables(self):
		assert helper_functions.Introduction_Object_Variables("", 1, 2) == "\\[(\\alpha_{0,0}, \\alpha_{0,1}), (\\alpha_{1,0}, \\alpha_{1,1})\\] which all lie on that 1D object.<br><br>\n"

	def test_Introduction(self):
		assert helper_functions.Introduction("", 3, 5) == "To represent a 3D object in 5D space, there are 2 equations that need to be satisfied in order to check whether the point\n\\[(A_0, ..., A_{4})\\]\nin 5D space lies on the 3D object defined by the point(s)\n \\[(\\alpha_{0,0},...,\\alpha_{0,4}), ..., (\\alpha_{3,0},...,\\alpha_{3,4})\\] which all lie on that 3D object.<br><br>\n"

if __name__ == '__main__':
  unittest.main()