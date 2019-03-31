from src import utils
from tokenize import generate_tokens
from collections import Counter
from src import custom_tokenizer

def token_generator(file, tokens_list):
    tok_callback = generate_tokens(file.readline)
    for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tok_one:
        tokens_list.append(toktype)
    return 0


def simple(filepath):
    tok = custom_tokenizer.Tokenizer(filepath)
    results = tok.full_tokenize()
    return tokenizer.compress_tokens(results)


def compare_files(filename_one, filename_two):
    """ Receives filenames as parameters, compares the list of lines received
		Returns the tuple containing the plagiarism percentage
    """
    if utils.check_file(filename_one) and utils.check_file(filename_two):
        file_one = open(utils.get_file_path(filename_one))
        file_two = open(utils.get_file_path(filename_two))

        file_one_tokens, file_two_tokens = [], []

        if filename_one.split(".")[1] == "py":
            token_generator(file_one, file_one_tokens)
            token_generator(file_two, file_two_tokens)
        else:
            print(simple(filename_one))
            return 0
            
        counter_one = Counter(file_one_tokens)
        counter_two = Counter(file_two_tokens)

        plagiarism_counter = counter_one & counter_two
        number_of_lines_plagiarised = sum(plagiarism_counter.values())
        file_one_plagiarism_percentage = utils.get_plagiarism_percentage(number_of_lines_plagiarised * 2, sum(counter_one.values()) + sum(counter_two.values()))
        return file_one_plagiarism_percentage
    else:
        print("Error file format not supported")

if __name__ == '__main__':
    print(compare_files("../../Test_Folder/File_1.py","../../Test_Folder/File_1_copy.py"))
