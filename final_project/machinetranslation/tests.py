import unittest
from translator import Translator


class TestTranslator(unittest.TestCase):
    def test(self):
        self.assertEqual(Translator().english_to_french('Hello'), 'Bonjour')
        self.assertEqual(Translator().english_to_french('Hello'), 'Bonjour')
        self.assertEqual(Translator().french_to_english('Bonjour'), 'Hello')
        self.assertEqual(Translator().french_to_english('Bonjour'), 'Hello')


unittest.main()
