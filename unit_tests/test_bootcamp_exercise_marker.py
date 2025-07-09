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

    @patch("sys.stdin", StringIO(""))
    def test_display_question_answer(self):
        """
        Testing std out- and input of one question 
        """
        question = ['How many leaves are in a tree?, C, A - 23, B - 45, C - 78']
    
        output = StringIO()
        sys.stdout = output

        answer = display_question(question)

        self.assertTrue(type(str, answer))
        self.assertEqual(1, len(answer))
        self.assertTrue(re.match("[A-C]", answer))
        self.assertEqual(
            "1. How many leaves are in a tree?\n"
            "A - 23\n"
            "B - 45\n"
            "C - 78\n",
            output.getvalue()
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
