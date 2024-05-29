import unittest
import tempfile
import os
from test_task import word_count


class TestWordCount(unittest.TestCase):
    
    def create_temp_file(self, text):
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(text.encode('utf-8'))
        temp_file.close()
        return temp_file.name

    def test_simple_string(self):
        file_path = self.create_temp_file("i want to test this string")
        self.assertEqual(word_count(file_path), "1 i\n1 want\n1 to\n1 test\n1 this\n1 string")
        os.remove(file_path)

    def test_string_with_bad_chars(self):
        file_path = self.create_temp_file("i, want to: test this string!")
        self.assertEqual(word_count(file_path), "1 i\n1 want\n1 to\n1 test\n1 this\n1 string")
        os.remove(file_path)

    def test_repeated_word(self):
        file_path = self.create_temp_file("test Test TEST tEsT")
        self.assertEqual(word_count(file_path), "4 test")
        os.remove(file_path)

    def test_empty_file(self):
        file_path = self.create_temp_file("")
        self.assertEqual(word_count(file_path), "")
        os.remove(file_path)


if __name__ == '__main__':
    unittest.main()


# test a simple text without bad_chars
# test a simple text with bad_chars
# test a text with repeated word in different register
# test an empty file
