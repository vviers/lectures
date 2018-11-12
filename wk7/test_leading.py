import leading
import unittest

class TestLeading(unittest.TestCase):
    '''Tests for leading.'''

    def test_empty(self):
        '''Test an empty string.'''
        input = ""
        output_expected = []
        output = leading.leading_substrings(input)
        self.assertEqual(output_expected, output, "Empty string.")
        
    def test_one_char(self):
        '''Test when one letter string'''
        input = "a"
        output_expected = ["a"]
        output = leading.leading_substrings(input)
        self.assertEqual(output_expected, output, "One letter case.")
        
    def test_two_char(self):
        '''Test when two letter string'''
        input = "ab"
        output_expected = ["a", "ab"]
        output = leading.leading_substrings(input)
        self.assertEqual(output_expected, output, "Two letter case.")
    
    def justspaces(self):
        '''Test when 4 spaces string'''
        input = "    "
        output_expected = [" ", "  ", "   ", "    "]
        output = leading.leading_substrings(input)
        self.assertEqual(output_expected, output, "Only spaces case.")
            

if __name__ == '__main__':
    unittest.main()