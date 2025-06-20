#!/usr/bin/env python3
"""
Registration Station project
"""
import re


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
        answer = input("Are these details correct? (y/n): \n").strip().lower()
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
    * Date
    * Location
    * Experience
    """
    valid_locations = {
        "Johannesburg Physical", "Johannesburg Virtual",
        "Cape Town Physical", "Cape Town Virtual",
        "Durban Physical", "Durban Virtual",
        "Phokeng Physical", "Phokeng Virtual"
    }

    valid_experience = ["Prior Experience", "No Prior Experience"]

    for i, line in enumerate(file_data):
        if user_name in line:
            while True:
                corrected_details = input("Date - Location - Experience: \n")

                parts = [part.strip() for part in corrected_details.split(" - ")]
                if len(parts) != 3:
                    print("Invalid input or format.")
                    continue

                date, location, experience = parts

                date_pattern = (
                    r"^\d{1,2} "
                    r"(January|February|March|April|May|June|July|August|September|October|November|December)$"
                )
                if not re.match(date_pattern, date):
                    print("Invalid date format. Use `DD Month`.")
                    continue

                if location.title() not in valid_locations:
                    print(f"Invalid location.") # Choose from: {', '.join(valid_locations)}
                    continue

                if experience.title() not in valid_experience:
                    print(f"Invalid response for experience. Choose from: {', '.join(valid_experience)}.")
                    continue

                updated_line = f"{user_name} - {corrected_details}\n"
                file_data[i] = updated_line
                break

            break

    try:
        with open("bootcampers.txt", "w") as file:
            file.writelines(file_data)
    except IOError:
        print("Error: Could not write to file.")


def find_username(file_data, user_name):
    """
    Main function for running Registration Station, which inlcudes:
       * get username input from user
       * check if username exists and print corresponding details
    """
    for line in file_data:
        if user_name in line:
            parts = line.strip().split(" - ")
            details = parts[1:]
            print(' - '.join(details))
            return (True)

    return (False)


if __name__ == "__main__":
    file_name = get_file_contents()
    file_data = read_file(file_name)
    user_name = input_user_name()
    
    user_found = find_username(file_data, user_name)

    if user_found:
        answer = correct_or_incorrect()
        if answer == "incorrect":
            correct_details(file_data, user_name)
        elif answer == "correct":
            print("Registration complete!")

    else:
        print(f"The user {user_name} does not exist.")
