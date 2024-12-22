from datetime import date
from io import StringIO
import unittest
from unittest.mock import patch

from features.UsernameGenerator import create_user_name, user_campus, user_details

class username_generator_test(unittest.TestCase):
    """Tests for the Username Generator module."""

    def run_user_details_test(self, input, expected_output):
        """
        Helper method to test user_details function with provided inputs
        and verify the output matches expectations.
        """
        with patch("sys.stdin", StringIO("\n".join(inputs))), patch("sys.stdout", new_callable=StringIO) as output:
            user_details()
            self.assertEqual(output.getvalue(), expected_output)

    def test_invalid_name(self):
        """Test invalid input for first name."""
        inputs = ["Chand1er", "Chandler", "Jacobs", "2023", "Durban"]
        expected_output = (
            "Insert your first name\n"
            "Invalid first name\n"
            "Insert your first name\n"
            "Insert your last name\n"
            "Insert your cohort\n"
            "Insert the campus you will be attending in\n"
            "lerjac2023DBN\n"
        )
        self.run_user_details_test(inputs, expected_output)

    def test_invalid_surname(self):
        """Test invalid input for last name."""
        inputs = ["Lekau", "Mamabo1o", "Mamabolo", "2022", "Cape Town"]
        expected_output = (
            "Insert your first name\n"
            "Insert your last name\n"
            "Invalid last name\n"
            "Insert your last name\n"
            "Insert your cohort\n"
            "Insert the campus you will be attending in\n"
            "kaumam2022CPT\n"
        )
        self.run_user_details_test(inputs, expected_output)

    def test_invalid_cohort(self):
        """Test invalid input for cohort."""
        inputs = ["Joshua", "Overton", "2020", "2021", "2022", "Phokeng"]
        expected_output = (
            "Insert your first name\n"
            "Insert your last name\n"
            "Insert your cohort\n"
            "Invalid cohort\n"
            "Insert your cohort\n"
            "Invalid cohort\n"
            "Insert your cohort\n"
            "Insert the campus you will be attending in\n"
            "huaove2022PHO\n"
        )
        self.run_user_details_test(inputs, expected_output)

    def test_invalid_campus(self):
        """Test invalid input for campus."""
        inputs = ["Sandiselwe", "Zwane", "2026", "Pretoria", "Johannesburg"]
        expected_output = (
            "Insert your first name\n"
            "Insert your last name\n"
            "Insert your cohort\n"
            "Insert the campus you will be attending in\n"
            "Invalid campus\n"
            "Insert the campus you will be attending in\n"
            "lwezwa2026JHB\n"
        )
        self.run_user_details_test(inputs, expected_output)

    def test_empty_first_name(self):
        """Test empty first name."""
        inputs = ["", "Thandeka", "Mngomezulu", "2022", "Phokeng"]
        expected_output = (
            "Insert your first name\n"
            "Invalid first name\n"
            "Insert your first name\n"
            "Insert your last name\n"
            "Insert your cohort\n"
            "Insert the campus you will be attending in\n"
            "ekamng2022PHO\n"
        )
        self.run_user_details_test(inputs, expected_output)

    def test_name_extractions(self):
        """Test username extraction of name components."""
        username = create_user_name("Zenani", "Zwane", "2020", "Durban")
        self.assertEqual(username[:3], "ani")
        self.assertEqual(username[3:6], "zwa")

    def test_valid_user_details(self):
        """Test valid user details."""
        valid_campuses = ["Johannesburg", "Cape Town", "Durban", "Phokeng"]
        first_name = "Thandeka"
        last_name = "Mngomezulu"
        cohort = str(date.today().year)
        final_campus = "Durban"

        self.assertGreaterEqual(len(first_name), 3)
        self.assertGreaterEqual(len(last_name), 3)
        self.assertEqual(int(cohort), date.today().year)
        self.assertIn(final_campus, valid_campuses)

    def test_campus_abbreviations(self):
        """Test campus abbreviation translations."""
        self.assertEqual(user_campus("johannesburg"), "JHB")
        self.assertEqual(user_campus("cape town"), "CPT")
        self.assertEqual(user_campus("durban"), "DBN")
        self.assertEqual(user_campus("phokeng"), "PHO")

    @patch("sys.stdin", StringIO("Corban\nLoots\n2022\nDurban"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_username_generation(self, mock_stdout):
        """Test full username generation flow."""
        user_details()
        self.assertEqual(mock_stdout.getvalue(), (
            "Insert your first name\n"
            "Insert your last name\n"
            "Insert your cohort\n"
            "Insert the campus you will be attending in\n"
            "banloo2022DBN\n"
        ))

    def test_edge_case_campus_abbreviation(self):
        """Test campus abbreviation with mixed casing."""
        self.assertEqual(user_campus("PhOkEnG"), "PHO")
        self.assertEqual(user_campus("CAPe ToWN"), "CPT")

    def test_edge_case_names(self):
        """Test name extraction with edge cases like short names."""
        username = create_user_name("Al", "Li", "2025", "Durban")
        self.assertEqual(username, "alili2025DBN")

    def test_numeric_and_special_name_inputs(self):
        """Test usernames with numeric or special characters in names."""
        inputs = ["An@", "#Smith", "2023", "Johannesburg"]
        expected_output = (
            "Insert your first name\n"
            "Invalid first name\n"
            "Insert your first name\n"
            "Insert your last name\n"
            "Invalid last name\n"
            "Insert your last name\n"
            "Insert your cohort\n"
            "Insert the campus you will be attending in\n"
            "nthsmi2023JHB\n"
        )
        self.run_user_details_test(inputs, expected_output)


if __name__ == "__main__":
    unittest.main()
