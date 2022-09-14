import unittest
from Hangman import guess_next_letter


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #    self.assertEqual(True, False)  # add assertion here

    def test_function_should_return_something(self):

        pattern = '____t'
        used_letters = list("ces")
        word_list = ['about', 'abound', 'abundant', 'python', 'hangman']

        assert guess_next_letter(pattern, used_letters, word_list) is not None


if __name__ == '__main__':
    unittest.main()
