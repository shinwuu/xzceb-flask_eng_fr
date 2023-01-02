"""
Sinsandra Nov 1/2/2023
Python for AI & Application Development Final Project
tests.py module
doc-string
"""
import unittest
from translator import *

# Sinsandra Nov 1/2/2023
# Python for AI & Application Development Final Project

class Test_french_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Null"), 'Null') # test for null input
        self.assertEqual(french_to_english("Bonjour"), "Hello")

class Test_english_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Null"), 'Null') # test for null input
        self.assertEqual(english_to_french("Hello"), "Bonjour")

unittest.main()
