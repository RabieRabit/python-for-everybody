import unittest
from program import *

class TestMyProgram(unittest.TestCase):

    def test_hello_world(self):
        text = make_it_uppercase("Hello world")
        self.assertEqual(text, "HELLO WORLD")

    def test_first_word(self):
        result = return_first_word("Greetings is my first word")
        self.assertEqual(result, "Greetings")
    
    def test_list(self):
        result = return_list()
        self.assertListEqual(result,
        ["cats", "dogs", "birds"],
    "The list was wrong!")

if __name__ == "__main__":
    unittest.main()