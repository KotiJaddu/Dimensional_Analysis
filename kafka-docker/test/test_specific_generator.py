import sys
import pytest
import io
import pandas as pd
sys.path.append('../src')
import specific_generator

@pytest.mark.parametrize('index, points', [[1,"0"],[2,"1,2"],[3,"1,2;3,4"],[4,"1,3,4,5;3,2,1,8"],[5,"0,9,3;-1,2,4;-3,6,-7"],[6,"0,9,-3,3;0,-1,2,4;-10,-3,6,-7"],[7,"0,9,-3,3,5,6;6,5,0,-1,2,4;-10,-3,6,-10,5,-7"],
	[8,"0,9,-3,3,5,6,10;6,5,0,-20,-1,2,4;-10,-3,6,12,-10,5,-7"],[9,"1,2,3,4,5,6,7,8;2,3,4,5,6,7,8,9;3,4,5,6,7,8,9,10;1,5,6,7,8,9,10,11"],[10,"-1,-2,-3,4,-5;6,5,-4,3,-2;4,3,2,6,4;6,7,8,5,-3"],[11,"3,2,1;5,6,7"],[12,"9,50,32,24,25,26;-32,24,25,12,24,10;32,41,54,34,67,12;10,23,24,11,10,-10"],[13,"0,1,2;-1,100,12;13,1,14"],[14,"0,1,2,3,4,5,3,2,2,5,4,3"],[15,"0,0,4,3,2;1,2,3,4,5"]])
def test_me(index, points):
	test_file = open("test_data/specific_generator/specific_generator_test" + str(index) + ".html", "r")
	df = pd.read_csv(io.StringIO("""""" + points.replace(";", "\n") + """"""), sep=",", header=None)
	assert test_file.read() == specific_generator.Model().generate_dimensional_analysis_html_script(df)
	test_file.close()


'''
py.test --tb=short test_specific_generator.py
'''
