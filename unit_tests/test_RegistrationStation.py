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
                "4 April - Johannesburg Physical - No prior experience\n",
                text_capture.getvalue()
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
                "4 April - Johannesburg Physical - No prior experience\n"
                "Are these details correct? (y/n): \n",
                text_capture.getvalue()
        )
        self.assertEqual("correct", result)


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
                "4 April - Johannesburg Physical - No prior experience\n"
                "Are these details correct? (y/n): \n",
                text_capture.getvalue()
        )
        self.assertEqual("incorrect", result)


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
                "Date - Location - Experience: \n",
                text_capture.getvalue()
        )

        file_data = read_file("bootcampers.txt")
        self.assertEqual(
                "llomog2025JHB - 4 April - Johannesburg Physical - No prior experience",
                file_data[-1]
        )

        orig_data = read_file(campers)
        with open("bootcampers.txt", "w") as file:
            file.writelines(orig_data)


    @patch("sys.stdin", StringIO(
        "ytvgh\n"
        "14/05 - Johannesburg Physical - No Prior Experience\n"
        "14 May - Limpopo Physical - No Prior Experience\n"
        "14 May - Johannesburg Physical - Not a lot\n"
        "14 May - Johannesburg Physical - No Prior Experience"
    ))
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
                "Date - Location - Experience: \n"
                "Invalid input.\n"
                "Date - Location - Experience: \n"
                "Invalid Date format. Use `DD Month`.\n"
                "Date - Location - Experience: \n"
                "Invalid location.\n"
                "Date - Location - Experience: \n"
                "Invalid response for experience. Choose from: `Prior Experience`, `No Prior Experience`.\n",
                text_capture.getvalue()
        )

        file_data = read_file("bootcampers.txt")
        self.assertEqual(
                "colootsJHB2023 - 14 May - Johannesburg Physical - No Prior Experience",
                file_data[-2]
        )

        orig_data = read_file(campers)
        with open("bootcampers.txt", "w") as file:
            file.writelines(orig_data)


    @patch("features.RegistrationStation.open", side_effect=IOError("Write error"))
    @patch("sys.stdin", StringIO("colootsJHB2023 - 13 May - Johannesburg Physical - No Prior Experience"))
    def test_write_failur(self, mock_open):
        """
        Test file write failur in correct_details().
        """
        text_capture = StringIO()
        sys.stdout = text_capture

        file_data = read_file("bootcampers.txt")
        correct_details(file_data, "colootsJHB2023")

        self.assertEqual(
                "Error: Could not write to file.\n",
                text_capure.getvalue()
        )


if __name__ == '__main__':
    unittest.main()
