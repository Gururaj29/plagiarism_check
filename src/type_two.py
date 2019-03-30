from src import utils
from tokenize import generate_tokens
from collections import Counter

def compare_files(filename_one, filename_two):
    """ Receives filenames as parameters, compares the list of lines received
		Returns the tuple containing the plagiarism percentage
    """
    file_one = open(utils.get_file_path(filename_one))
    file_two = open(utils.get_file_path(filename_two))

    file_one_tokens, file_two_tokens = [], []

    tok_one = generate_tokens(file_one.readline)
    for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tok_one:
        file_one_tokens.append(toktype)

    tok_two = generate_tokens(file_two.readline)
    for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tok_two:
        file_two_tokens.append(toktype)

    counter_one = Counter(file_one_tokens)
    counter_two = Counter(file_two_tokens)

    # print(counter_one, counter_two)
    plagiarism_counter = counter_one & counter_two
    number_of_lines_plagiarised = sum(plagiarism_counter.values())
    file_one_plagiarism_percentage = utils.get_plagiarism_percentage(number_of_lines_plagiarised * 2, sum(counter_one.values()) + sum(counter_two.values()))
    return file_one_plagiarism_percentage

if __name__ == '__main__':
    print(compare_files("../../Test_Folder/File_1.py","../../Test_Folder/File_1_copy.py"))
