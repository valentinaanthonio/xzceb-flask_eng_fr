import unittest
from translator import englishtofrench,frenchtoenglish

class TestEnglishToFrench(unittest.TestCase):
    def frenchToEnglish(self):
        self.assertEqual(englishtofrench(" ")," ")
        self.assertEqual(englishtofrench('Hello'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def englishToFrench(self):
        self.assertEqual(frenchtoenglish(" ")," ")
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')


unittest.main()