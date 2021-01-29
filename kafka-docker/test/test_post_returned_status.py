import sys
import pytest
import subprocess

@pytest.mark.parametrize('X, Y', [[0,1],[0,2],[1,2],[1,3],[1,4],[2,3],[2,4],[2,6],[2,7],[3,8],[3,5],[3,6],[4,6],[4,7],[4,8]])
def test_me(X, Y):
	assert "200" == subprocess.run("curl -i -XPOST localhost:5000/dimensional_analysis -d odim=" + str(X) + " -d sdim=" + str(Y) + " -d General=Submit", capture_output=True, shell=True, encoding="utf8").stdout.split()[1]

'''
py.test --tb=short test_post_returned_status.py
'''
