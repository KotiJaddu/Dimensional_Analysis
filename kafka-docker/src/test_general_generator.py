import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"src"
)
sys.path.append(SOURCE_PATH)
import unittest

class test_general_generator(unittest.TestCase):

  def testcase(self):
    x = 'koti'
    assert x=='koti'

if __name__ == '__main__':
  unittest.main()
