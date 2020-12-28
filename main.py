import random
from art import logo, vs
from replit import clear
from game_data import data


# generate random data
def generate_random_data():
    """
    Function generate one random data from data list. Return dict with keys:
    'name', 'follower_count', 'description', 'country'
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


score = 0
is_play = True
while is_play:
    data_A = generate_random_data()
    data_B = generate_random_data()
    while data_A['name'] == data_B['name']:
        print("the same data")
        data_B = generate_random_data()
    # print(data_A)
    # print(data_B)
    formatted_text(data_A, data_B)
    answer = input("Who has more followers, type 'A' or 'B': ").lower()
    print(answer)
    is_play = False
