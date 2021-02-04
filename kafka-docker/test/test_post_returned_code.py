import sys
import pytest
import subprocess

#sys.path.append('../src')
sys.path.append('src')
import general_generator

@pytest.mark.parametrize('index, X, Y', [[1,0,1],[2,0,2],[3,1,2],[4,1,3],[5,1,4],[6,2,3],[7,2,4],[8,2,6],[9,2,7],[10,3,8],[11,3,5],[12,3,6],[13,4,6],[14,4,7],[15,4,8]])
def test_if_HTML_code_returned_is_correct(index, X, Y):
	test_file = open("test/test_data/general_generator/general_generator_test" + str(index) + ".html", "r")
	assert test_file.read() == subprocess.run("curl -XPOST localhost:5000/dimensional_analysis -d odim=" + str(X) + " -d sdim=" + str(Y) + " -d General=Submit", capture_output=True, shell=True, encoding="utf8").stdout
	test_file.close()


'''
py.test --tb=short test_post_returned_code.py
'''