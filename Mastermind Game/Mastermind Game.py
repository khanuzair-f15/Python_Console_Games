import random as rn

print("Welcome to Mastermind!\nTry to guess the 4-digit number.\n")

attempts = 0
n = rn.randint(1000, 9999)
n = list(str(n))

while True:
    count = 0
    # this loop will extract error free input
    while True:
        try:
            number = int(input("Guess the 4-digit number: "))
            if not 1000 <= number <= 9999:
                print("\nEntered number must be four digit\n")
                continue
            number = list(str(number))
            attempts += 1
            break
        except ValueError:
            print("Invalid input")
            continue
        except KeyboardInterrupt:
            print("Something went wrong")
            print("Quiting...!!!")
            exit(0)

    for i in range(len(n)):
        if n[i] == number[i]:
            count += 1

    if count == 4:
        print(f"You've become a Mastermind!\nIt took you only {attempts} tries.")
        break
    else:
        print(f"Not quite the number. You got {count} digit(s) correct.\n")
