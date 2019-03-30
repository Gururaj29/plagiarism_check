import config
import os
import termcolor

def check_file(filename):
	''' Checks if the file is written in allowed programming languages
	'''
	file_parts = filename.split('.')
	if len(file_parts) != 2:
		print(filename + ": File name is not correct")
		return False

	# Checks for extension
	if file_parts[1] not in config.get_extensions():
		print(filename + ": Programming language is not supported")
		return False

	if not os.path.exists(filename):
		print(filename + ": File does not exist")
		return False

	return True

def get_file_path(filename):
	return config.SOURCE_CODE_FILEPATH + filename 

def remove_comments(list_lines):
	return list_lines

def get_readlines(filepath, remove_comments_bool):
	if not check_file(filepath):
		return None
	with open(filepath) as file:
		lines = file.readlines()

	#Only for type one
	if remove_comments_bool:
		remove_comments(lines)

	return lines

def extract_files(filename_one, filename_two, remove_comments_bool):
	''' Receives the filenames as strings, returns list of lines
	'''
	filepath_one = get_file_path(filename_one)
	filepath_two = get_file_path(filename_two)
	return get_readlines(filepath_one, remove_comments_bool), get_readlines(filepath_two, remove_comments_bool)

def get_plagiarism_percentage(number_of_lines_copied, total_number_of_lines):
	return (number_of_lines_copied*100)/ total_number_of_lines

def print_diff(plagiarism_result, diff_symbol):
	for line in plagiarism_result:
		if line[0] == ' ':
			print(termcolor.colored(line, "red"), end="")
		elif line[0] == diff_symbol:
			print(termcolor.colored(line, "green"), end="")
