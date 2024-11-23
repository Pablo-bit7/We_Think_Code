
def read_file():
    '''
    Read contents from the text file
    @return a list of five random questions
    '''


def ask_questions(list_of_questions):
    '''
    Manages the list of questions selected from the text file
    @param list of five questions
    @return a list of questions the user answer incorrectly
    '''


def display_question(question):
    '''
    Displays a question
    Takes in an answer
    @param a single question
    @return the answer given by the user
    '''


def is_correct_answer(solution, user_answer):
    '''
    Checks if the answer given by the user is correct
    @param solution - The correct answer
    @param user_answer - The answer entered by the user
    @return boolean indicating if user answered correctly or not
    '''


def next_round(current_round):
    '''
    Calculates the round
    @param current round completed
    @return integer next round
    '''


if __name__ == '__main__':

    score = 0
    current_round = 0
    question_list = read_file()

    while score < 5:
        current_round = next_round(current_round)
        question_list = ask_questions(question_list)
        score = 5 - len(question_list)
