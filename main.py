import random
from art import logo, vs
from replit import clear
from game_data import data


# generate random data
def generate_random_data():
    """
    Function generate one random data from data list. Return dict with keys:
    'name'-> str, 'follower_count'-> int, 'description'-> str, 'country-> str'
    """
    random_data = random.choice(data)
    return random_data


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
        f"Agains B: {data_B['name']}, a {data_B['description']}, from {data_B['country']}."
    )


# def compare_answer(answer, data_A, data_B):
#     score = 0
#     if answer == 'a' and data_A['follower_count'] > data_B['follower_count']:
#         score += 1
#         data_A = data_B
#         while data_A['name'] == data_B['name']:
#             print("the same data")
#             data_B = generate_random_data()
#     elif answer == 'b' and data_B['follower_count'] > data_A['follower_count']:
#         score += 1
#         data_A = data_B
#     else:
#         is_play = False
#         return is_play


score = 0
is_play = True
data_A = generate_random_data()
data_B = generate_random_data()
while data_A['name'] == data_B['name']:
    print("the same data")
    data_B = generate_random_data()
# print(data_A)
# print(data_B)
while is_play:
    clear()
    print(logo)
    print(f"Your score is {score}")
    formatted_text(data_A, data_B)
    answer = input("Who has more followers, type 'A' or 'B': ").lower()
    #compare_answer(answer, data_A, data_B)
    if answer == 'a' and data_A['follower_count'] > data_B['follower_count']:
        score += 1
        data_A = data_B
        data_B = generate_random_data()
        while data_A['name'] == data_B['name']:
            print("the same data")
            data_B = generate_random_data()
    elif answer == 'b' and data_B['follower_count'] > data_A['follower_count']:
        score += 1
        data_A = data_B
        data_B = generate_random_data()
        while data_A['name'] == data_B['name']:
            print("the same data")
            data_B = generate_random_data()
    else:
        is_play = False
