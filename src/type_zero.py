import termcolor
import difflib
import json
import pprint
import os

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

def get_file_path(filename):
	return config['source_code_filepath'] + filename 

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

def compare_files(filename_one, filename_two):
	''' Receives filenames as parameters, compares the list of lines received
		Returns the tuple containing the plagiarism percentage 
	'''
	file_one, file_two = extract_files(filename_one, filename_two)
	result = []
	for line in difflib.unified_diff(file_one, file_two):
		result.append(line)
		print(line)
	
	if not result:
		# If there is no result, then it's 100% same file
		return 100.0, 100.0

	# Exclude the initial three default lines
	result = result[3:]

	#prints the results for file one
	print("Source code one: ")
	print_diff(result, '-')
	print("-" * 40)

	#prints the results for file two
	print("Source code two: ")
	print_diff(result, '+')
	print("-" * 40)

	number_of_lines_plagiarised = len(list(filter(lambda x: x[0] == ' ', result)))
	file_one_plagiarism_percentage = get_plagiarism_percentage(number_of_lines_plagiarised, len(file_one) + len(file_two))
	file_two_plagiarism_percentage = get_plagiarism_percentage(number_of_lines_plagiarised, len(file_one) + len(file_two))

	return file_one_plagiarism_percentage, file_two_plagiarism_percentage, result