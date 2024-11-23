# Registration Station project


def read_file(data_flt):

    # Read and return contents of text file
    
    text_file = open("C:\\Users\\mogan\\Documents\\ThinkCode\\Bootcamp Helper Resources\\skeleton_code\\bootcampers.txt","r+")
    data_flt = text_file.readlines()
    return data_flt


def input_user_name():

    """
    Takes username as input
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


def get_file_contents():

    """Return desired text file"""


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