#!/usr/bin/env python3
from xml.dom import UserDataHandler
from datetime import datetime


def user_details():
    """
    Prompt user input
    """
    while True:
        first_name = input("Insert your first name:\n")
        if first_name.isalpha():
            break
        if first_name == "":
            print("Invalid first name.")
        else:
            print("Invalid first name. Names should not contain digits "
                  "or special characters.")

    while True:
        last_name = input("Insert your last name:\n")
        if last_name.isalpha():
            break
        if first_name == "":
            print("Invalid first name.")
        else:
            print("Invalid last name. Names should not contain digits "
                  "or special characters.")

    while True:
        current_year = datetime.now().year
        cohort = input("Insert your cohort:\n")
        if cohort.isdigit():
            cohort = int(cohort)
            if cohort >= current_year:
                break
            else:
                print("Invalid cohort.")
        else:
            print("Invalid input. Years should not contain alphabets "
                  "or special characters.")

    while True:
        campuses = [
            'johannesburg',
            'cape town',
            'durban',
            'phokeng'
            ]
        campus = input("Insert the campus you will be attending in:\n").lower()
        if campus in campuses:
            break
        else:
            print("Invalid campus.")

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
    campus = campus.lower()  # Normalise to lowercase
    final_campus = campusdict.get(campus, "Invalid campus.")

    return (final_campus)


def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """
    if len(first_name) < 3:
        first_name = first_name + "O"
    if len(last_name) < 3:
        last_name = last_name + "O"

    user_name = f"{first_name[-3:].lower()}{last_name[0:3].lower()}{cohort}{final_campus}"
    print(f"{user_name}")

    return (user_name)


if __name__ == '__main__':
    first_name, last_name, cohort, campus = user_details()
    final_campus = user_campus(campus)
    create_user_name(first_name, last_name, cohort, final_campus)
