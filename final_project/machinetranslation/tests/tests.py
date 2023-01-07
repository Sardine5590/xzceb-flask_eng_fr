import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertRaises(ValueError, englishToFrench, None)


class TestFrenchToEnglish(unittest.TestCase):
    def test(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertRaises(ValueError, frenchToEnglish, None)

unittest.main()