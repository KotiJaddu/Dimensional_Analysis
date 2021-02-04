import subprocess
subprocess.run(['py.test', '--tb=short', 'test_general_generator.py', 'test_specific_generator.py', 'test_specific_satisfier.py', 'test_post_returned_code.py', 'test_post_returned_status.py', 'test_post_returned_server_error.py'], shell=True)
