#!/usr/bin/env python3
from xml.dom import UserDataHandler
from datetime import datetime


def user_details():
    """
    Prompt user input
    """

    while True:
        first_name = input("Enter your first name: ")
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
        campuses = ['Johannesburg', 'Cape Town', 'Durban', 'Phokeng']
        campus = input("Enter your cohort's campus: ")
        if campus in campuses:
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
        'Johannesburg': 'JHB',
        'Cape Town': 'CPT',
        'Durban': 'DBN',
        'Phokeng': 'PHO'
    }

    final_campus = campusdict[campus]
    return (final_campus)


def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """
    
    #return (username)


if __name__ == '__main__':
    first_name, last_name, cohort, campus = user_details()
    final_campus = user_campus(campus)
    #create_user_name(first_name, last_name, cohort, final_campus)
