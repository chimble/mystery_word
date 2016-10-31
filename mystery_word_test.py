from mystery_word import draw_word
import unittest

class Test_mystery_word(unittest.TestCase):
    def test_draw_word(self):
        self.assertEqual(draw_word(word))

if __name__ == '__main__':
    unittest.main(exit = False)
