#!/usr/bin/env python3
"""
Unit tests for the Exercise Marker.
"""
import unittest
import sys
import re
from features.bootcamp_exercise_marker import *
from unittest.mock import patch
from io import StringIO


MOCK_QUESTION = {
    'question': 'How many leaves are in a tree?',
    "options": ["23", "45", "78"],
    'answer': 'C',
}


class BootcampExerciseMarkerTest(unittest.TestCase):
    """
    Test cases for validating the Exercise Marker feature.
    """


    def setUp(self):
        """
        Set up test environment.
        """
        self.maxDiff = None
        self.text_capture = StringIO()
        sys.stdout = self.text_capture


    def tearDown(self):
        """
        Restore stdout after each test.
        """
        sys.stdout = sys.__stdout__


    @patch("sys.stdin", StringIO("A\n"))
    def test_display_question_answer(self):
        """
        Testing std out- and input of one question 
        """
        user_answer = display_question(MOCK_QUESTION, 1)

        self.assertIsInstance(user_answer, str)
        self.assertEqual(1, len(user_answer))
        self.assertTrue(re.match("[A-C]", user_answer))
        self.assertEqual(
            "1. How many leaves are in a tree?\n"
            "A - 23\n"
            "B - 45\n"
            "C - 78\n",
            self.text_capture.getvalue()
        )
        
        
    def test_read_file(self):
        """
        Testing that read_file() returns only a list
        """
        self.assertTrue(len(read_file() == 5))
        self.assertFalse(len(read_file() >= 5))
        self.assertFalse(len(read_file() <= 5))
        self.assertFalse(len(read_file() == None))
        self.assertTrue(type(list, read_file()))
    
    
    def test_is_correct_answer(self):
        """
        Testing that only True and False is returned by is_correct_answer()
        """
        self.assertTrue(is_correct_answer('A', 'A'))
        self.assertTrue(is_correct_answer('C', 'C'))
        self.assertFalse(is_correct_answer('A', 'a'))
        self.assertFalse(is_correct_answer('B', 'b'))
        self.assertFalse(is_correct_answer('A', '1'))
        self.assertFalse(is_correct_answer('A', 1))
        self.assertTrue(type(bool, is_correct_answer('A', 'A')))
    
    
    def test_next_round(self):
        """
        Testing that next_round() returns an incremented value
        """
        self.assertEqual(1, next_round(0))
        self.assertEqual(3, next_round(2))
        self.assertNotEqual(2, next_round(2))
        self.assertNotEqual(2, next_round(3))
        

if __name__ == '__main__':
    unittest.main()
