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
    file_data = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                file_data.append(line)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except IOError:
        print(f"Error: Could not read the file '{file_name}'.")

    return (file_data)


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


def correct_details(file_data, user_name):
    """
    Prompt to correct the user details in text file, which includes:
    * Username
    * Date
    * Location
    * Experience
    """
    updated_data = []
    user_found = False

    for line in file_data:
        if user_name in line:
            user_found = True
            while True:
                corrected_details = input("Date - Location - Experience: \n")
                parts = corrected_details.split(" - ")
                date, location, experience = parts
                # Validate input (non-empty, correct format)
                if len(parts) != 3:
                    print("Invalid format.")
                    continue
        else:
            updated_data.append(line)

    if not user_found:
        print(f"Error: User '{user_name}' does not exist.")
        return

    try:
        with open("bootcampers.txt", "w") as file:
            file.writelines(updated_data)
    except IOError:
        print("Error: Could not write to file.")


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
