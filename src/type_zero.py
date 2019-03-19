import termcolor
import difflib
import json
import pprint

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
	
def compare_files(filename_one, filename_two):
	''' Receives filenames as parameters, compares the list of lines received
	Returns the list of results 
	'''
	file_one, file_two = extract_files(filename_one, filename_two)
	result = []
	print(file_one, file_two)
	for line in difflib.unified_diff(file_one, file_two):
		result.append(line)
		print(line)
	return result
