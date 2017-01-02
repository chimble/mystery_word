import unittest
from mystery_word import *


class TestMysteryWordMethods(unittest.TestCase):
    def test_fake_function(self):
        self.assertTrue(fake_function('boy') == 'boy')


    def test_three_lists(self):
        easy_word_list = three_lists('easy')
        self.assertTrue('berry' in easy_word_list)
        self.assertTrue('fish' in easy_word_list)
        self.assertTrue('dogs' in easy_word_list)


    def test_draw_word(self):
        word = 'abc'
        print(draw_word(word))
        self.assertTrue(draw_word(word) == "_ _ _ ")

if __name__ == '__main__':
    unittest.main()
