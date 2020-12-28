import random
from art import logo, vs
from replit import clear
from game_data import data


# generate random data
def generate_random_data():
    """
    Function generate random data from data list. Return list of dicts with keys:
    'name'-> str, 'follower_count'-> int, 'description'-> str, 'country-> str'
    """
    random_data_A = random.choice(data)
    random_data_B = random.choice(data)
    while random_data_A['name'] == random_data_B['name']:
        print("the same data")
        random_data_B = random.choice(data)
    list_of_data = [random_data_A, random_data_B]
    return list_of_data


# Display formatted questions
def formatted_text(data_A, data_B):
    """
    Function print formatted questions from random data and pass it to compare them. 
    Return None.
    """
    print(
        f"Compare A: {data_A['name']}, a {data_A['description']}, from {data_A['country']}."
    )
    print(vs)
    print(
        f"Against B: {data_B['name']}, a {data_B['description']}, from {data_B['country']}."
    )


# compare answer
def compare_answer(answer, data_A, data_B):
    """ 
    The function takes three attributes 'answer' -> str, 'data_A' -> dict, 'data_B' -> dict.
    Function return True or False. 
    """
    if answer == 'a' and data_A['follower_count'] > data_B['follower_count']:
        return True
    elif answer == 'b' and data_B['follower_count'] > data_A['follower_count']:
        return True
    else:
        return False


# main function
def game():
    score = 0
    is_play = True
    questions = generate_random_data()
    data_A = questions[0]
    data_B = questions[1]

    while is_play:
        clear()
        print(logo)
        print(f"Your score is {score}")
        formatted_text(data_A, data_B)
        answer = input("Who has more followers, type 'A' or 'B': ").lower()
        if compare_answer(answer, data_A, data_B):
            score += 1
            data_A = data_B
            while data_A['name'] == data_B['name']:
                print("the same data")
                data_B = generate_random_data()[0]
        else:
            is_play = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
