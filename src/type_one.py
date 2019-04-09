from src import type_zero

def compare_files(filename_one, filename_two):
	return type_zero.compare_files(filename_one, filename_two, True)

#Only for the unit tests
def get_check_file_handler():
	return type_zero.get_check_file_handler()

#Only for the unit tests
def get_extract_files_handler():
	return type_zero.extract_files

#Only for the unit tests
def get_plagiarism_percentage_handler():
	return type_zero.plagiarism_percentage
