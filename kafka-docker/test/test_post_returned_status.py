import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"src"
)
sys.path.append(SOURCE_PATH)
from app import app
import unittest


class TestDataSuccessStatusCode(unittest.TestCase):
	def test_post_data_valid_parameters_returns_200_with_parameters_0_1(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="0", sdim="1", General="Submit"))
		self.assertEqual(response.status_code, 200)

	def test_post_data_valid_parameters_returns_200_with_parameters_0_2(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="0", sdim="2", General="Submit"))
		self.assertEqual(response.status_code, 200)

	def test_post_data_valid_parameters_returns_200_with_parameters_1_2(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="1", sdim="2", General="Submit"))
		self.assertEqual(response.status_code, 200)

	def test_post_data_valid_parameters_returns_200_with_parameters_1_3(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="1", sdim="3", General="Submit"))
		self.assertEqual(response.status_code, 200)

	def test_post_data_valid_parameters_returns_200_with_parameters_1_4(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="1", sdim="4", General="Submit"))
		self.assertEqual(response.status_code, 200)

	def test_post_data_valid_parameters_returns_200_with_parameters_2_3(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="2", sdim="3", General="Submit"))
		self.assertEqual(response.status_code, 200)

	def test_post_data_valid_parameters_returns_200_with_parameters_2_4(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="2", sdim="4", General="Submit"))
		self.assertEqual(response.status_code, 200)

	def test_post_data_valid_parameters_returns_200_with_parameters_2_6(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="2", sdim="6", General="Submit"))
		self.assertEqual(response.status_code, 200)

	def test_post_data_valid_parameters_returns_200_with_parameters_2_7(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="2", sdim="7", General="Submit"))
		self.assertEqual(response.status_code, 200)

	def test_post_data_valid_parameters_returns_200_with_parameters_3_8(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="3", sdim="8", General="Submit"))
		self.assertEqual(response.status_code, 200)

	def test_post_data_valid_parameters_returns_200_with_parameters_3_5(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="3", sdim="5", General="Submit"))
		self.assertEqual(response.status_code, 200)

	def test_post_data_valid_parameters_returns_200_with_parameters_3_6(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="3", sdim="6", General="Submit"))
		self.assertEqual(response.status_code, 200)

	def test_post_data_valid_parameters_returns_200_with_parameters_4_6(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="4", sdim="6", General="Submit"))
		self.assertEqual(response.status_code, 200)

	def test_post_data_valid_parameters_returns_200_with_parameters_4_7(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="4", sdim="7", General="Submit"))
		self.assertEqual(response.status_code, 200)

	def test_post_data_valid_parameters_returns_200_with_parameters_4_8(self):
		response = app.test_client().post('/dimensional_analysis', data=dict(odim="4", sdim="8", General="Submit"))
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()