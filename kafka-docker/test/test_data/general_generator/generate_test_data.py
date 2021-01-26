import sys
sys.path.append('../../src')
import specific_generator, general_generator, specific_generator

general_generator_parameters = [[1,0,1],[2,0,2],[3,1,2],[4,1,3],[5,1,4],[6,2,3],[7,2,4],[8,2,6],[9,2,7],[10,3,8],[11,3,5],[12,3,6],[13,4,6],[14,4,7],[15,4,8]]

for parameters in general_generator_parameters:	
	test_file = open("general_generator_test" + str(parameters[0]) + ".html", "w")
	test_file.write(general_generator.Model().generate(parameters[1], parameters[2]))
	test_file.close()