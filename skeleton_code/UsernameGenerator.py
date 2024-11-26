#!/usr/bin/env python3
from xml.dom import UserDataHandler
from datetime import datetime


def user_details():
    """
    Prompt user input
    """
    current_year = datetime.now().year
    campuses = ['Johannesburg', 'Cape Town', 'Durban', 'Phokeng']

    while True:
        first_name = input("Enter your first name: ")
        if first_name.isalpha():
            if len(first_name) < 3:
                first_name = first_name + "O"
            break
        else:
            print("Invalid input. Names should not contain digits "
                  "or special characters.")
            print()

    while True:
        last_name = input("Enter your last name: ")
        if last_name.isalpha():
            if len(last_name) < 3:
                last_name = last_name + "O"
            break
        else:
            print("Invalid input. Names should not contain digits "
                  "or special characters.")
            print()

    while True:
        cohort_year = input("Enter the year of your cohort (YYYY): ")
        if cohort_year.isdigit():
            cohort_year = int(cohort_year)
            if cohort_year >= current_year:
                break
            else:
                print(f"The cohort year {cohort_year} is in the past. "
                      "Please enter a future year.")
                print()
        else:
            print("Invalid input. Years should not contain alphabets "
                  "or special characters.")
            print()

    while True:
        final_campus = input("Enter your cohort's campus: ")
        if final_campus in campuses:
            break
        else:
            print("Please provide a valid campus.")
            print()

    return (first_name, last_name, cohort_year, final_campus)


def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """
    pass


def user_campus(campus):
    """
    Return valid campus abbreviations
    """
    pass


if __name__ == '__main__':
    user_details()
