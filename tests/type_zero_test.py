import unittest
from src import type_zero
import config

def error_msg(actual_result, expected_result):
    return 'Expected ' + str(expected_result) + ' but found ' + str(actual_result)

class TestTypeZero(unittest.TestCase):

    test_file = [
        '#include<stdio.h>\n',
        '\n',
        'void func() {\n',
        '\tprintf("Hello world!");\n',
        '}\n',
        '\n',
        'int main() {\n',
        '\tint a, c;\n',
        '\tfunc();\n',
        '\tprintf("This is just a test code")\n',
        '}'
    ]

    test_filename = "type_zero_test_file.c"

    def test_get_percentage(self):
        method_to_be_tested = type_zero.plagiarism_percentage

        #Test instance one
        total_copied_lines_per_file = 0
        file_one_len = 100
        file_two_len = 100
        expected_result = 0
        actual_result = method_to_be_tested(total_copied_lines_per_file, file_one_len, file_two_len)
        self.assertEqual(actual_result, expected_result, msg = error_msg(actual_result, expected_result))

        #Test instance two
        total_copied_lines_per_file = 100
        file_one_len = 100
        file_two_len = 100
        expected_result = 100
        actual_result = method_to_be_tested(total_copied_lines_per_file, file_one_len, file_two_len)
        self.assertEqual(actual_result, expected_result, msg = error_msg(actual_result, expected_result))

        #Test instance three
        total_copied_lines_per_file = 58
        file_one_len = 100
        file_two_len = 100
        expected_result = (total_copied_lines_per_file * 2 * 100) / (file_one_len + file_two_len)
        actual_result = method_to_be_tested(total_copied_lines_per_file, file_one_len, file_two_len)
        self.assertEqual(actual_result, expected_result, msg = error_msg(actual_result, expected_result))
        
    def test_extract_files(self):
        
        method_to_be_tested = type_zero.extract_files

        #Test instance one
        expected_result = (self.test_file, self.test_file)
        actual_result = method_to_be_tested(self.test_filename, self.test_filename, False)
        self.assertEqual(actual_result, expected_result, msg = error_msg(actual_result, expected_result))

    def test_check_file(self):
        method_to_be_tested = type_zero.get_check_file_handler()
        
        #Test instance one
        expected_result = False
        actual_result = method_to_be_tested("randon_file_name.c")
        self.assertEqual(actual_result, expected_result, msg = error_msg(actual_result, expected_result))

        #Test instance two
        expected_result = False
        actual_result = method_to_be_tested("file_name.randon_extension")
        self.assertEqual(actual_result, expected_result, msg = error_msg(actual_result, expected_result))

        #Test instance three
        expected_result = False
        actual_result = method_to_be_tested("file_name_with_no_extension")
        self.assertEqual(actual_result, expected_result, msg = error_msg(actual_result, expected_result))

        #Test instance four
        expected_result = True
        actual_result = method_to_be_tested(config.SOURCE_CODE_FILEPATH + self.test_filename)
        self.assertEqual(actual_result, expected_result, msg = error_msg(actual_result, expected_result))


    def test_compare_files(self):

        method_to_be_tested = type_zero.compare_files

        #Test instance one
        expected_result = (100.0, 100.0)
        actual_result = method_to_be_tested(self.test_filename, self.test_filename)
        self.assertEqual(actual_result, expected_result, msg = error_msg(actual_result, expected_result))

def main():
    unittest.main()