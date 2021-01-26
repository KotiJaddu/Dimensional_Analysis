import sys
import io
import pandas as pd
sys.path.append('../../src')
import specific_generator, general_generator, specific_satisfier

general_generator_parameters = [[1,0,1],[2,0,2],[3,1,2],[4,1,3],[5,1,4],[6,2,3],[7,2,4],[8,2,6],[9,2,7],[10,3,8],[11,3,5],[12,3,6],[13,4,6],[14,4,7],[15,4,8]]
specific_generator_parameters = [[1,"0"],[2,"1,2"],[3,"1,2;3,4"],[4,"1,3,4,5;3,2,1,8"],[5,"0,9,3;-1,2,4;-3,6,-7"],[6,"0,9,-3,3;0,-1,2,4;-10,-3,6,-7"],[7,"0,9,-3,3,5,6;6,5,0,-1,2,4;-10,-3,6,-10,5,-7"],
	[8,"0,9,-3,3,5,6,10;6,5,0,-20,-1,2,4;-10,-3,6,12,-10,5,-7"],[9,"1,2,3,4,5,6,7,8;2,3,4,5,6,7,8,9;3,4,5,6,7,8,9,10;1,5,6,7,8,9,10,11"],[10,"-1,-2,-3,4,-5;6,5,-4,3,-2;4,3,2,6,4;6,7,8,5,-3"],[11,"3,2,1;5,6,7"],[12,"9,50,32,24,25,26;-32,24,25,12,24,10;32,41,54,34,67,12;10,23,24,11,10,-10"],[13,"0,1,2;-1,100,12;13,1,14"],[14,"0,1,2,3,4,5,3,2,2,5,4,3"],[15,"0,0,4,3,2;1,2,3,4,5"]]
specific_satisfier_parameters = [[1,"0;9"],[2,"1,2;1,2"],[3,"1,2;3,4"],[4,"1,3,4,5;3,2,1,8"],[5,"0,9,3;-1,2,4;-3,6,-7"],[6,"0,9,-3,3;0,-1,2,4;-10,-3,6,-7"],[7,"0,9,-3,3,5,6;6,5,0,-1,2,4;-10,-3,6,-10,5,-7"],
	[8,"0,9,-3,3,5,6,10;6,5,0,-20,-1,2,4;-10,-3,6,12,-10,5,-7"],[9,"1,2,3,4,5,6,7,8;2,3,4,5,6,7,8,9;3,4,5,6,7,8,9,10;1,5,6,7,8,9,10,11"],[10,"-1,-2,-3,4,-5;6,5,-4,3,-2;4,3,2,6,4;6,7,8,5,-3"],[11,"3,2,1;5,6,7"],[12,"9,50,32,24,25,26;-32,24,25,12,24,10;32,41,54,34,67,12;10,23,24,11,10,-10"],[13,"0,1,2;-1,100,12;13,1,14"],[14,"0,1,2,3,4,5,3,2,2,5,4,3;1,1,2,3,4,5,3,2,3,5,4,3"],[15,"0,0,4,3,2;1,2,3,4,5"]]


def write_to_file(file, type, obj1, obj2):
	test_file = open(file, "w")
	if type == 0:
		test_file.write(general_generator.Model().generate(obj1, obj2))
	elif type == 1:
		test_file.write(specific_generator.Model().generate(obj1))
	elif type == 2:
		test_file.write(specific_satisfier.Model().generate(obj1))
	test_file.close()

for i in range(len(general_generator_parameters)):	
	write_to_file("general_generator/general_generator_test" + str(i + 1) + ".html", 0, general_generator_parameters[i][1], general_generator_parameters[i][2])
	specific_generator_df = pd.read_csv(io.StringIO("""""" + specific_generator_parameters[i][1].replace(";", "\n") + """"""), sep=",", header=None)
	specific_satisfier_df = pd.read_csv(io.StringIO("""""" + specific_satisfier_parameters[i][1].replace(";", "\n") + """"""), sep=",", header=None)
	write_to_file("specific_generator/specific_generator_test" + str(i + 1) + ".html", 1, specific_generator_df, None)
	write_to_file("specific_satisfier/specific_satisfier_test" + str(i + 1) + ".html", 2, specific_satisfier_df, None)
