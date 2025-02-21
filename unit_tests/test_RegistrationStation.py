#!/usr/bin/python3
"""
Unit tests for the Registration Station.
"""
import unittest
from io import StringIO
import sys
from unittest.mock import patch
from features.RegistrationStation import *


class MyTestCase(unittest.TestCase):
    """
    Test cases for validating the Registration Station feature.
    """


    def setUp(self):
        """
        Helper function ensures sys.stdout is restored after each test
        """
        self.addCleanup(lambda: setattr(sys, "stdout", sys.__stdout__))


    def test_valid_username(self):
        """
        Test valid username input.
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        file_data = read_file("bootcampers.txt")
        result = find_username(file_data, "elomkhDBN2022")

        self.assertEqual(
                text_capture.getvalue(),
                "4 April - Johannesburg Physical - No prior experience\n"
        )
        self.assertTrue(result)


    def test_invalid_username(self):
        """
        Test invalid username.
        """
        file_data = read_file("bootcampers.txt")
        result = find_username(file_data, "elokhDBN2022")

        self.assertFalse(result)


    @patch("sys.stdin", StringIO("y"))
    def test_valid_confirmation(self):
        """
        Test confirmation of correct user details.
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        file_data = read_file("bootcampers.txt")
        find_username(file_data, "elomkhDBN2022")
        result = correct_or_incorrect()

        self.assertEqual(
                text_capture.getvalue(),
                "4 April - Johannesburg Physical - No prior experience\n"
                "Are these details correct? (y/n): \n"
        )
        self.assertEqual(result, "correct")


    @patch("sys.stdin", StringIO("n"))
    def test_invalid_confirmation(self):
        """
        Test denial of correctness of user details.
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        file_data = read_file("bootcampers.txt")
        find_username(file_data, "elomkhDBN2022")
        result = correct_or_incorrect()

        self.assertEqual(
                text_capture.getvalue(),
                "4 April - Johannesburg Physical - No prior experience\n"
                "Are these details correct? (y/n): \n"
        )
        self.assertEqual(result, "incorrect")


    @patch("sys.stdin", StringIO("elomkhDBN2022\nn\nelomkhDBN2022 - 4 April - Johannesburg Physical - No prior experience\n"))
    def test_incorrect_user_details_corrected(self):
        """
        Test correction of incorrect user details.
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        RegistrationStation.correct_or_incorrect()
        RegistrationStation.correct_details()
        self.assertEqual(
            "Select username: 4 April - Johannesburg Physical - No prior experience\n"
            "Is this correct? (Y/n): Username - Date - Location - Experience: 4 April - Johannesburg Physical - No prior experience\n""",
            text_capture.getvalue()
        )


    @patch("sys.stdin", StringIO("colootsJHB2023\nn\ncolootsJHB2023 - 13 May - Johannesburg Physical - No Prior Experience\n"))
    def test_incorrect_user_details_corrected_additional(self):
        """
        Test correction of details for a different username.
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        RegistrationStation.correct_or_incorrect()
        RegistrationStation.correct_details()
        self.assertEqual(
            "Select username: 13 May - Johannesburg Physical - No Prior Experience\n"
            "Is this correct? (Y/n): Username - Date - Location - Experience: 13 May - Johannesburg Physical - No Prior Experience\n",
            text_capture.getvalue()
        )


    @patch("sys.stdin", StringIO("colootsJHB2023\nn\ncolootsJHB2023 - 13 May - Johannesburg Physical - No Prior Experience\nn\ncolootsJHB2023 - 13 May - Johannesburg Physical - No Prior Experience\ny"))
    def test_incorrect_user_details_incorrect_addition(self):
        """
        Test multiple incorrect corrections before confirming.
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        RegistrationStation.correct_or_incorrect()
        RegistrationStation.correct_details()
        RegistrationStation.correct_or_incorrect()
        RegistrationStation.correct_details()
        self.assertEqual(
            "Select username: 13 May - Johannesburg Physical - No Prior Experience\n"
            "Is this correct? (Y/n): Username - Date - Location - Experience: 13 May - Johannesburg Physical - No Prior Experience\n"
            "Is this correct? (Y/n): Username - Date - Location - Experience: 13 May - Johannesburg Physical - No Prior Experience\n",
            text_capture.getvalue()
        )


if __name__ == '__main__':
    unittest.main()
