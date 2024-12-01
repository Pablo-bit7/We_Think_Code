#!/usr/bin/env python3
from xml.dom import UserDataHandler
from datetime import datetime


def user_details():
    """
    Prompt user input
    """

    while True:
        first_name = input("Insert your first name: ")
        if first_name.isalpha():
            break
        else:
            print("Invalid input. Names should not contain digits "
                  "or special characters.")
            print()

    while True:
        last_name = input("Enter your last name: ")
        if last_name.isalpha():
            break
        else:
            print("Invalid input. Names should not contain digits "
                  "or special characters.")
            print()

    while True:
        current_year = datetime.now().year
        cohort = input("Enter the year of your cohort (YYYY): ")
        if cohort.isdigit():
            cohort = int(cohort)
            if cohort >= current_year:
                break
            else:
                print(f"The cohort year {cohort} is in the past. "
                      "Please enter a future year.")
                print()
        else:
            print("Invalid input. Years should not contain alphabets "
                  "or special characters.")
            print()

    while True:
        campuses = [
            'Johannesburg',
            'johannesburg',
            'Cape Town',
            'cape town',
            'Durban',
            'durban',
            'Phokeng',
            'phokeng'
            ]
        campus = input("Enter your cohort's campus: ")
        if campus in campuses:
            campus = campus.lower()
            break
        else:
            print("Please provide a valid campus.")
            print()

    return (first_name, last_name, cohort, campus)


def user_campus(campus):
    """
    Return valid campus abbreviations
    """

    campusdict = {
        'johannesburg': 'JHB',
        'cape town': 'CPT',
        'durban': 'DBN',
        'phokeng': 'PHO'
    }

    final_campus = campusdict[campus]
    return (final_campus)


def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """

    if len(first_name) < 3:
        first_name = first_name + "O"
    if len(last_name) < 3:
        last_name = last_name + "O"

    user_name = f"{first_name[-3:].lower()}{last_name[0:3].lower()}{final_campus}{cohort}"

    print(
        f"\nFirst Name: {first_name}\n"
        f"Last Name: {last_name}\n"
        f"Cohort Year: {cohort}\n"
        f"Campus: {final_campus}\n"
    )
    print(f"Your username: {user_name}")

    return (user_name)


if __name__ == '__main__':
    first_name, last_name, cohort, campus = user_details()
    final_campus = user_campus(campus)
    create_user_name(first_name, last_name, cohort, final_campus)
