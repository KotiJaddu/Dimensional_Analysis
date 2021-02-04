import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"src"
)
sys.path.append(SOURCE_PATH)
from app import app
import unittest

class TestKafkaConsumerForGeneralGenerator(unittest.TestCase):
	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_0_1(self):
		test_file = open("test/test_data/general_generator/general_generator_test1.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="0", sdim="1", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_0_2(self):
		test_file = open("test/test_data/general_generator/general_generator_test2.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="0", sdim="2", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_1_2(self):
		test_file = open("test/test_data/general_generator/general_generator_test3.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="1", sdim="2", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_1_3(self):
		test_file = open("test/test_data/general_generator/general_generator_test4.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="1", sdim="3", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_1_4(self):
		test_file = open("test/test_data/general_generator/general_generator_test5.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="1", sdim="4", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_2_3(self):
		test_file = open("test/test_data/general_generator/general_generator_test6.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="2", sdim="3", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_2_4(self):
		test_file = open("test/test_data/general_generator/general_generator_test7.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="2", sdim="4", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_2_6(self):
		test_file = open("test/test_data/general_generator/general_generator_test8.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="2", sdim="6", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_2_7(self):
		test_file = open("test/test_data/general_generator/general_generator_test9.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="2", sdim="7", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_3_8(self):
		test_file = open("test/test_data/general_generator/general_generator_test10.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="3", sdim="8", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_3_5(self):
		test_file = open("test/test_data/general_generator/general_generator_test11.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="3", sdim="5", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_3_6(self):
		test_file = open("test/test_data/general_generator/general_generator_test12.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="3", sdim="6", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_4_6(self):
		test_file = open("test/test_data/general_generator/general_generator_test13.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="4", sdim="6", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_4_7(self):
		test_file = open("test/test_data/general_generator/general_generator_test14.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="4", sdim="7", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

	def test_if_HTML_code_returned_is_correct_general_generator_with_parameters_4_8(self):
		test_file = open("test/test_data/general_generator/general_generator_test15.html", "r")
		test_html = test_file.read()
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="4", sdim="8", General="Submit"))
		test_file.close()
		self.assertEqual(response.data.decode('UTF-8'), test_html)

if __name__ == '__main__':
	unittest.main()