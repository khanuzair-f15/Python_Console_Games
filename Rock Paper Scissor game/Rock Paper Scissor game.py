import random as rn

while True:
    print(
        "Winning rules of the game ROCK PAPER SCISSORS are:\nRock vs Paper -> Paper wins \nRock vs Scissors -> Rock wins \nPaper vs Scissors -> Scissors wins \n")
    print("Enter your choice \n1 - Rock \n2 - Paper\n3 - Scissors\n")

    while True:
        try:
            User_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice")
            print()
            print("Choose again")
            continue
        except KeyboardInterrupt:
            print("\nGame interrupted by user. Exiting gracefully.")
            exit(0)
        print()
        if User_choice == 1:
            print("User choice is: Rock")
            break
        elif User_choice == 2:
            print("User choice is: Paper")
            break
        elif User_choice == 3:
            print("User choice is: Scissors")
            break
        else:
            print("Invalid choice")
            print("Chose again\n")

    Comp_choice = rn.randint(1, 3)
    if Comp_choice == 1:
        print("Computer choice is: Rock")
    elif Comp_choice == 2:
        print("Computer choice is: Paper")
    elif Comp_choice == 3:
        print("Computer choice is: Scissors")
    print()
    # rock
    # paper
    # scissors

    # compare rock with computers choice
    if ((User_choice == 1 and Comp_choice == 1) or
            (User_choice == 2 and Comp_choice == 2) or
            (User_choice == 3 and Comp_choice == 3)):
        print("<== Draw! ==>")
    elif ((User_choice == 2 and Comp_choice == 1) or  # paper beats rock
          (User_choice == 1 and Comp_choice == 3) or  # rock beats scissor
          (User_choice == 3 and Comp_choice == 2)):  # scissor beats paper  <-- fixed
        print("<== User wins! ==>")
    else:
        print("<== Computer Wins! ==>")
    while True:
        try:
            choice = input("Do you want to play again? (Y/N)\n > ").capitalize()
        except KeyboardInterrupt:
            print("\nnGame interrupted by user. Exiting gracefully.")
            exit(0)
        if choice == "Y":
            break
        elif choice == "N":
            print("Thanks for playing!")

            break
        else:
            print("Invalid choice Chose again")
    if choice == "N":
        break
