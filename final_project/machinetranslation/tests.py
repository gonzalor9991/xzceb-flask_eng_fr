import unittest
from translator import Translator


class TestTranslator(unittest.TestCase):
    def test_english_to_french_equal(self):
        self.assertEqual(Translator().english_to_french('Hello'), 'Bonjour')

    def test_english_to_french_not_equal(self):
        self.assertNotEqual(Translator().english_to_french('Hello'), 'bonjour')

    def test_french_to_english_equal(self):
        self.assertEqual(Translator().french_to_english('Bonjour'), 'Hello')

    def test_french_to_english_not_equal(self):
        self.assertNotEqual(Translator().french_to_english('Bonjour'), 'hello')


unittest.main()
