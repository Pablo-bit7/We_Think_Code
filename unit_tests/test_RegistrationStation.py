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

    @patch("sys.stdin", StringIO("elomkhDBN2022\ny\n"))
    def test_valid_username_lowercase(self):
        """
        Test valid lowercase username input.
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        self.assertEqual(
            "Select username: 4 April - Johannesburg Physical - No prior experience\n",
            text_capture.getvalue()
        )


    @patch("sys.stdin", StringIO("elomkhDBN2022\nY\n"))
    def test_valid_username_Uppercase(self):
        """
        Test valid uppercase username input.
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        self.assertEqual(
            "Select username: 4 April - Johannesburg Physical - No prior experience\n",
            text_capture.getvalue()
        )


    @patch("sys.stdin", StringIO("elokhDBN2022\nelomkhDBN2022\ny\n"))
    def test_invalid_username(self):
        """
        Test invalid username followed by a valid username.
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        self.assertEqual(
            "Select username: Please enter valid existing username\n"
            "Select username: 4 April - Johannesburg Physical - No prior experience\n",
            text_capture.getvalue()
        )


    @patch("sys.stdin", StringIO("elomkhDBN2022\ny\n"))
    def test_valid_confirmation(self):
        """
        Test confirmation of correct user details.
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        RegistrationStation.correct_or_incorrect()
        self.assertEqual(
            "Select username: 4 April - Johannesburg Physical - No prior experience\n"
            "Is this correct? (Y/n): ",
            text_capture.getvalue()
        )


    @patch("sys.stdin", StringIO("elonkhDBN2022\nelomkhDBN2022\ny\n"))
    def test_valid_confirmation_invalid_username(self):
        """
        Test valid confirmation after correcting an invalid username.
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        RegistrationStation.correct_or_incorrect()
        self.assertEqual(
            "Select username: Please enter valid existing username\n"
            "Select username: 4 April - Johannesburg Physical - No prior experience\n"
            "Is this correct? (Y/n): ",
            text_capture.getvalue()
        )


    @patch("sys.stdin", StringIO("elomkhDBN2022\nn\n"))
    def test_incorrect_user_details(self):
        """
        Test when user denies the correctness of their details.
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        RegistrationStation.find_username('bootcampers.txt')
        RegistrationStation.correct_or_incorrect()
        self.assertEqual(
            "Select username: 4 April - Johannesburg Physical - No prior experience\n"
            "Is this correct? (Y/n): ",
            text_capture.getvalue()
        )


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
