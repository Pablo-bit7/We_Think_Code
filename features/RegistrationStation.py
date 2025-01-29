#!/usr/bin/env python3
"""
Registration Station project
"""


def get_file_contents():
    """
    Return desired text file
    """
    return ("bootcampers.txt")


def read_file(file_name):
    """
    Read and return contents of text file
    """
    file_contents = []
    try:
        with open(file_name, "r+") as file:
            for line in file:
                file_contents.append(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{file_name}'.")

    return (file_contents)


def input_user_name():
    """
    Takes username as input
    """
    while True:
        user_name = input("Please enter you username:\n").strip()
        if user_name.isalnum():
            break
        else:
            print("Invalid username.")

    return (user_name)


def correct_or_incorrect():
    """
    Prompt to ask if details are correct or not
    """
    while True:
        answer = input("Are these details correct? (y/n):\n").strip().lower()
        if not answer:
            print("Invalid response")
        elif answer == "y":
            return ("correct")
        elif answer == "n":
            return ("incorrect")
        else:
            print("Invalid response.")


def correct_details():

    """
    Prompt to correct the user details in text file, which includes:
    * Username
    * Date
    * Location
    * Experience
    """


def find_username(file_name):

    """
    Main functiontion for running Registration Station, which inlcude:
       * get username input from user
       * check if username exists and print corresponding details
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
