import subprocess
subprocess.run(['py.test', '--tb=short', 'test_general_generator.py', 'test_specific_generator.py', 'test_specific_satisfier.py'], shell=True)
