"""
Working of the FLAMES Game

This project demonstrates string manipulation, list operations, loops and basic game logic in Python.

Take Two Names as Input: The names are converted to lowercase and spaces are removed.
Remove Common Letters: Matching characters are removed from both names.
Count Remaining Letters: The total number of unmatched characters is calculated.
Initialize FLAMES List: A list containing Friends, Lovers, Affection, Marriage, Enemies, and Siblings is created.
Eliminate Options: Relationship options are removed in a circular manner using the remaining letter count.
Display the Result: The last remaining option represents the predicted relationship.
"""

game_running = True
while game_running:
    # Take Two Names as Input: The names are converted to lowercase and spaces are removed.
    name1 = input("Enter your name: ").lower().replace(" ", "")
    name2 = input("Enter your friend: ").lower().replace(" ", "")

    # Remove Common Letters: Matching characters are removed from both names.

    for i in list(name1):
        for j in list(name2):
            if i == j:
                name1 = name1.replace(i, "", 1)
                name2 = name2.replace(j, "", 1)
                break

    # Count Remaining Letters: The total number of unmatched characters is calculated.
    count = len(name1 + name2)

    # Initialize FLAMES List: A list containing Friends, Lovers, Affection, Marriage, Enemies, and Siblings is created.
    flames = [
        'Friends', 'Lovers', 'Affection', 'Marriage', 'Enemies', 'Siblings'
    ]

    # Eliminate Options: Relationship options are removed in a circular manner using the remaining letter count.

    start = 0
    while True:
        ele = (count + start - 1) % len(flames)  # for circular
        flames.pop(ele)
        start = ele
        if len(flames) == 1:
            print("Relationship game_running:", flames[0])
            break

    while True:
        try:
            choice = input("Wanna play again (Y/n) ?")
        except KeyboardInterrupt:
            print("Exiting...")
            break
        except:
            print("Error 404 please restart the game")
            break
        if choice.strip().lower() == "y":
            game_running = True
            break
        elif choice.strip().lower() == "n":
            game_running = False
            break
        else:
            print("Enter a valid choice")
            continue
