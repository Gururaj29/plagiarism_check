import unittest
from src import type_zero


class TestTypeZero(unittest.TestCase):

    def test_upper(self):
        ''' Test case to verify the get_percentage function '''
        method_to_be_tested = type_zero.plagiarism_percentage

        #Test instance one
        total_copied_lines_per_file = 0
        file_one_len = 100
        file_two_len = 100
        expected_result = 0
        self.assertEqual(method_to_be_tested(total_copied_lines_per_file, file_one_len, file_two_len), expected_result)

        #Test instance two
        total_copied_lines_per_file = 100
        file_one_len = 100
        file_two_len = 100
        expected_result = 100
        self.assertEqual(method_to_be_tested(total_copied_lines_per_file, file_one_len, file_two_len), expected_result)

        #Test instance three
        total_copied_lines_per_file = 0
        file_one_len = 100
        file_two_len = 100
        expected_result = 0
        self.assertEqual(method_to_be_tested(total_copied_lines_per_file, file_one_len, file_two_len), expected_result)
        
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

def main():
    unittest.main()