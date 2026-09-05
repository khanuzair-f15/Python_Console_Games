# importing content from other file

from game_data import data
from art import logo, vs
import random as rn

# this will help to clear data on terminal for cleaner look
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# in this function we will assing a random data from gae_data.py file
def assign():
    return rn.choice(data)


def compare(person1, person2, user_input):
    # creating max variable to store a name of account who have more follower
    Maxx = ""
    # accessing folower count of both accounts
    follower_of_p1 = person1.get("follower_count")
    follower_of_p2 = person2.get("follower_count")

    if follower_of_p2 > follower_of_p1:
        Maxx = person2.get("name")
    else:
        Maxx = person1.get("name")

    Maxx = Maxx.strip().lower()

    if user_input == Maxx:
        return True
    else:
        return False


def play_higher_lower():
    # outer loop
    still_playing = True

    while still_playing:
        person1 = assign()
        person2 = assign()
        score = 0

        if person2 == person1:
            person2 = assign()
            continue

        while True:

            if score >= 1:
                person1 = person2
                person2 = assign()
                while person2 == person1:
                    person2 = assign()

            # displaying logo
            print(logo)

            # displaying first person name and country
            print(f'  ------<=Account 1=>------  ')
            print(f'    ~ Name: {person1.get("name")} \n    ~ Country: {person1.get("country")}')

            # displaying VS asci art
            print(vs)

            # displaying second person name and country
            print(f'  ------<=Account 2=>------  ')
            print(f'    ~ Name: {person2.get("name")} \n    ~ Country: {person2.get("country")}')
            print()

            # display current score
            print("----------------------------------------------")
            print(f"Your current score is: {score}")
            print("----------------------------------------------")

            user_input = input("Enter your guess: ").strip().lower()
            if compare(person1, person2, user_input):
                score += 1
            else:
                print("Wrong guess")
                break
            clear()

        while True:
            choice = input("You wanna pay again (Y/N) ?").strip().lower()
            if choice.lower() == "y":
                still_playing = True
                break
            elif choice.lower() == "n":
                still_playing = False
                break
            else:
                print("Enter a valid choice")
                continue


play_higher_lower()
