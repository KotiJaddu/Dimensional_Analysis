import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"src"
)
sys.path.append(SOURCE_PATH)
from app import app
import unittest
import specific_satisfier
import pandas as pd
import io

data = [[1,"0;9"],[2,"1,2;1,2"],[3,"1,2;3,4"],[4,"1,3,4,5;3,2,1,8"],[5,"0,9,3;-1,2,4;-3,6,-7"],[6,"0,9,-3,3;0,-1,2,4;-10,-3,6,-7"],[7,"0,9,-3,3,5,6;6,5,0,-1,2,4;-10,-3,6,-10,5,-7"], [8,"0,9,-3,3,5,6,10;6,5,0,-20,-1,2,4;-10,-3,6,12,-10,5,-7"],[9,"1,2,3,4,5,6,7,8;2,3,4,5,6,7,8,9;3,4,5,6,7,8,9,10;1,5,6,7,8,9,10,11"],[10,"-1,-2,-3,4,-5;6,5,-4,3,-2;4,3,2,6,4;6,7,8,5,-3"],[11,"3,2,1;5,6,7"],[12,"9,50,32,24,25,26;-32,24,25,12,24,10;32,41,54,34,67,12;10,23,24,11,10,-10"],[13,"0,1,2;-1,100,12;13,1,14"],[14,"0,1,2,3,4,5,3,2,2,5,4,3;1,1,2,3,4,5,3,2,3,5,4,3"],[15,"0,0,4,3,2;1,2,3,4,5"]]

class TestKafkaConsumerForSpecificSatisfier(unittest.TestCase):
	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_0(self):
		index = 0
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)
		
	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_1(self):
		index = 1
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)

	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_2(self):
		index = 2
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)

	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_3(self):
		index = 3
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)

	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_4(self):
		index = 4
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)

	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_5(self):
		index = 5
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)

	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_6(self):
		index = 6
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)

	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_7(self):
		index = 7
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)

	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_8(self):
		index = 8
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)

	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_9(self):
		index = 9
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)

	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_10(self):
		index = 10
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)

	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_11(self):
		index = 11
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)

	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_12(self):
		index = 12
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)

	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_13(self):
		index = 13
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)

	def test_if_HTML_code_returned_is_correct_specific_satisfier_with_parameters_index_14(self):
		index = 14
		test_file = open("test/test_data/specific_satisfier/specific_satisfier_test" + str(index + 1) + ".html", "r")
		test_html = test_file.read()
		df = pd.read_csv(io.StringIO("""""" + data[index][1].replace(";", "\n") + """"""), sep=",", header=None)
		test_file.close()
		self.assertEqual(specific_satisfier.Model().generate_dimensional_analysis_html_script(df), test_html)

if __name__ == '__main__':
	unittest.main()