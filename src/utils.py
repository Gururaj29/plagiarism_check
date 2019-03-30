import config

def get_file_path(filename):
	return config.SOURCE_CODE_FILEPATH + filename 

def get_readlines(filepath):
	with open(filepath) as file:
		return file.readlines()

def extract_files(filename_one, filename_two):
	''' Receives the filenames as strings, returns list of lines
	'''
	filepath_one = get_file_path(filename_one)
	filepath_two = get_file_path(filename_two)
	return get_readlines(filepath_one), get_readlines(filepath_two)

def get_plagiarism_percentage(number_of_lines_copied, total_number_of_lines):
	return (number_of_lines_copied*100)/ total_number_of_lines

def print_diff(plagiarism_result, diff_symbol):
	for line in plagiarism_result:
		if line[0] == ' ':
			print(termcolor.colored(line, "red"), end="")
		elif line[0] == diff_symbol:
			print(termcolor.colored(line, "green"), end="")
