import random

name = input("what is your name? ")
print("Good luck! " + name)

guess_list = ['word', 'eraser', 'pencil', 'alphabet', 'bottle', 'perfume', 'laptop', 'computer', 'bed', 'door']
count = 12
guess_word = random.choice(guess_list)
temp = []
while True:
    try:
        character = input("Guess a character: ")
        if len(character) != 1:
            print("please enter a single character")
            continue
        if character in temp:
            print("You already guessed this caracter")
            continue
        count = count - 1
    except ValueError:
        print("Please enter a single character")
    except IndexError:
        print("Please enter only single character")

    if character in guess_word:
        temp.append(character)
    else:
        print("Wrong")
        print(f'You have {count} more guesses')
        continue

    for char in guess_word:
        if char in temp:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print()
    if all(char in temp for char in guess_word):
        print("You Win")
        print(f"The word is: {guess_word}")
        break
    if count == 1:
        print("You loose")
        print(f"Correct word is {guess_word}")
        break
