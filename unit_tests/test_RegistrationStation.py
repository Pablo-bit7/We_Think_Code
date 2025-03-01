#!/usr/bin/python3
"""
Unit tests for the Registration Station.
"""
import unittest
from io import StringIO
import sys
from unittest.mock import patch
import tempfile
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


    @patch("sys.stdin", StringIO("4 April - Johannesburg Physical - No prior experience"))
    def test_correction_with_valid_user_details(self):
        """
        Test correction with correctly formatted user details.
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        file_data = read_file("bootcampers.txt")

        with tempfile.NamedTemporary(mode="w+", delete=True) as temp_file:
            temp_file.writelines(file_data)
            campers = temp_file.name

        correct_details(file_data, "llomog2025JHB")
        self.assertEqual(
                text_capture.getvalue(),
                "Date - Location - Experience: \n"
        )

        file_data = read_file("bootcampers.txt")
        self.assertEqual(
                file_data[-1],
                "llomog2025JHB - 4 April - Johannesburg Physical - No prior experience"
        )

        orig_data = read_file(campers)
        with open("bootcampers.txt", "w") as file:
            file.writelines(orig_data)


    @patch("sys.stdin", StringIO("ytvgh\n14/05 - Johannesburg Physical - No Prior Experience\n14 May - Limpopo Physical - No Prior Experience\n14 May - Johannesburg Physical - Not a lot\n14 May - Johannesburg Physical - No Prior Experience"))
    def test_correction_with_invalid_user_details(self):
        """
        Test correction with incorrectly formatted user details.
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        file_data = read_file("bootcampers.txt")

        with tempfile.NamedTemporary(mode="w+", delete=True) as temp_file:
            temp_file.writelines(file_data)
            campers = temp_file.name

        correct_details(file_data, "colootsJHB2023")
        self.assertEqual(
                text_capture.getvalue(),
                "Date - Location - Experience: \n"
                "Invalid input.\n"
                "Date - Location - Experience: \n"
                "Invalid Date format. Use `DD Month`.\n"
                "Date - Location - Experience: \n"
                "Invalid location.\n"
                "Date - Location - Experience: \n"
                "Invalid response for experience. Choose from: `Prior Experience`, `No Prior Experience`.\n"
        )

        file_data = read_file("bootcampers.txt")
        self.assertEqual(
                file_data[-2],
                "colootsJHB2023 - 14 May - Johannesburg Physical - No Prior Experience"
        )

        orig_data = read_file(campers)
        with open("bootcampers.txt", "w") as file:
            file.writelines(orig_data)


    
    @patch("sys.stdin", StringIO("colootsJHB2023 - 13 May - Johannesburg Physical - No Prior Experience\n"))
    def test_write_failur(self):
        """
        Test multiple incorrect corrections before confirming.
        """
        text_capture = StringIO()
        sys.stdout = text_capture


if __name__ == '__main__':
    unittest.main()
