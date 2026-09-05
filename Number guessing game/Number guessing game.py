"""
Readme.md

# Number Guessing Game

A simple console-based number guessing game written in Python. The program picks a random number within
a user-defined range, and the player has 7 attempts to guess it correctly.

## How It Works

1. The player enters a lower bound and an upper bound.
2. The program picks a random number between those two bounds (inclusive).
3. The player gets up to **7 guesses** to find the number.
4. After each guess, the program tells the player if their guess was too low, too high, or correct.
5. If the player runs out of guesses without finding the number, the game ends and reveals the correct number.

## Code Structure

The script is split into two main loops:

### 1. Setup Loop (Range Input)
Asks the player for a lower bound and upper bound, validates them, and generates the random number.

### 2. Guessing Loop
Repeatedly asks the player to guess, validates the guess, tracks the guess count, and checks for a win or loss.

## Error Handling

### Setup Loop
- **`ValueError`**: Triggered if the player enters non-integer text for either bound. The player is
prompted to re-enter both values.
- **Bare `except`**: Catches any other unexpected error during input, so the program doesn't crash outright.
- **Range check (`lower_bound > upper_bound`)**: If the lower bound is greater than the upper bound,
the player is asked to re-enter both values instead of proceeding with an invalid range.

### Guessing Loop
- **`ValueError`**: Triggered if the player enters non-integer text for a guess.
Note: an invalid (non-integer) guess does **not** use up one of the 7 attempts, since the guess
counter only increments after a value is successfully converted.
- **Bare `except`**: Catches any other unexpected error during the guess input,
keeping the game running instead of crashing.
- **Out-of-range check**: If the guess is below the lower bound or above the upper bound,
the player is told to guess within the valid range, and the attempt is **not** counted
(`continue` skips the counter increment).
- **Guess limit check (`count > 6`)**: Runs as a separate `if` block after
the too-low/too-high/correct check, so it's always evaluated regardless of which of those three
outcomes occurred. This ensures the game correctly ends in a loss after the 7th valid guess if the number
hasn't been found.

## Known Limitations

- The bare `except` blocks print a message saying to "restart the game," but they don't actually restart anything
— the loop just asks for input again. The wording doesn't fully match the behavior.
- The setup loop's validation message ("lower bound cannot be less than or equal to upper bound")
describes the opposite of the condition being checked (`lower_bound > upper_bound`).
It doesn't affect functionality, but the wording is misleading.

## Example Flow

```
Enter lower bound: 1
Enter upper bound: 20
now you have 7 chance to find the correct number between 1 and 20
Guess 1: 10
Too Low
1
Guess 2: 15
Too High
2
Guess 3: 12
Correct!
Congratulation Ibra
Total Guesses 3
3
```

"""
from random import randint

while True:
    try:
        lower_bound = int(input("Enter lower bound: "))
        upper_bound = int(input("Enter upper bound: "))
        if lower_bound >= upper_bound:
            print("upper bound cannot be less than or equal to lower bound")
            print("Enter values again")
            continue
        random_number = randint(lower_bound, upper_bound)
        print(f"now you have 7  chance to find the correct number between {lower_bound} and {upper_bound}")
        break
    except ValueError:
        print("Entered values must be integer")
    except:
        print("Somethin went wrong please restart the game")
        break

# total allowed change is 7

count = 0
while True:
    try:
        guessed_number = int(input(f"Guess {count + 1}: "))
        if guessed_number < lower_bound or guessed_number > upper_bound:
            print(f"Guess the number must be in the given range ({lower_bound},{upper_bound})")
            continue
        count = count + 1
        if random_number > guessed_number:
            print("Too Low")

        elif random_number < guessed_number:
            print("Too High")

        elif random_number == guessed_number:
            print("Correct!")
            print("Congratulation Ibra")
            print(f"Total Guesses {count}")

            break
        if count > 6:
            print("You exceeds the guesses limit")
            print("Loser")
            print(f"Correct number is {random_number}")
            break
    except ValueError:
        print("Entered value is not correct")
        print("Guess again")
    except:
        print("Something went wrong please resart the game")
        break
