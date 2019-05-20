import os

path_to_dir = os.path.abspath(".")

saves = os.walk(path_to_dir + "/saveData")

for x in saves:
	for file in x[2]:
		print(file)