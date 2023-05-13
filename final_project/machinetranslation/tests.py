import unittest
from translator import Translator


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(Translator().english_to_french('Hello'), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(Translator().french_to_english('Bonjour'), 'Hello')
        self.assertEqual(Translator().french_to_english('Bonjour le monde'), 'Hello World')


unittest.main()
