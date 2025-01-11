#!/usr/bin/env python3
"""
Registration Station project
"""


def input_user_name():
    """
    Takes username as input
    """

    return (user_name)


def get_file_contents():
    """
    Return desired text file
    """

    return (file_name)


def read_file(file_name):
    """
    Read and return contents of text file
    """

    return (file_data)


def find_username(user_name, file_data):
    """
    Main functiontion for running Registration Station, which inlcude:
       * get username input from user
       * check if username exists and print corresponding details
    """


def correct_or_incorrect():
    """
    Prompt to ask if details are correct or not
    """


def correct_details():
    """
    Prompt to correct the user details in text file, which includes:
    * Username
    * Date
    * Location
    * Experience
    """


if __name__ == "__main__":
    registrations_file = get_file_contents()
    information = find_username(registrations_file)
    while True:
        answer = correct_or_incorrect()
        if answer == "correct":
            print(information)
            break
        else:
            correct_details()
