# ✊✋✌️ Rock Paper Scissors

A simple **Rock Paper Scissors** game built in Python where the player competes against the computer.

The computer randomly selects Rock, Paper, or Scissors, and the program determines the winner based on the classic game rules.

---

## 🎮 Introduction

**Rock Paper Scissors** is a classic hand game played between two players.

In this Python implementation:

* 👤 The user selects Rock, Paper, or Scissors.
* 🤖 The computer randomly chooses one of the three options.
* ⚖️ The choices are compared.
* 🏆 The winner is displayed.
* 🔄 The player can choose to play again.

The project focuses on practicing **conditional statements, loops, user input, exception handling, and Python's random module**.

---

## 📜 Game Rules

The winning rules are:

| User        | Computer    | Winner   |
| ----------- | ----------- | -------- |
| 🪨 Rock     | 🪨 Rock     | Draw     |
| 📄 Paper    | 📄 Paper    | Draw     |
| ✂️ Scissors | ✂️ Scissors | Draw     |
| 🪨 Rock     | ✂️ Scissors | User     |
| 📄 Paper    | 🪨 Rock     | User     |
| ✂️ Scissors | 📄 Paper    | User     |
| 🪨 Rock     | 📄 Paper    | Computer |
| 📄 Paper    | ✂️ Scissors | Computer |
| ✂️ Scissors | 🪨 Rock     | Computer |

### Quick Rule

```text
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
```

---

## 🕹️ How the Game Works

### 1. Display the rules

When the game starts, the program displays the winning rules and available choices:

```text
1 - Rock
2 - Paper
3 - Scissors
```

### 2. User selects a choice

The player enters:

```text
1
2
```

or:

```text
3
```

The program validates the input and asks again if the choice is invalid.

---

### 3. Computer makes a choice

The computer randomly generates a number between `1` and `3`:

```python
Comp_choice = rn.randint(1, 3)
```

The numbers represent:

```text
1 → Rock
2 → Paper
3 → Scissors
```

---

### 4. Determine the winner

The program compares the user's choice with the computer's choice.

For example:

```text
User → Rock
Computer → Scissors

Rock beats Scissors

🏆 User wins!
```

If both choices are the same:

```text
User → Paper
Computer → Paper

🤝 Draw!
```

Otherwise, the computer wins.

---

### 5. Play Again

After every round, the player is asked:

```text
Do you want to play again? (Y/N)
```

Entering:

```text
Y
```

starts another round.

Entering:

```text
N
```

ends the game.

---

## 🔄 Program Flow

```text
              ┌──────────────┐
              │     Start    │
              └──────┬───────┘
                     │
                     ▼
          Display Game Rules
                     │
                     ▼
          Get User's Choice
                     │
              ┌──────┴──────┐
              │             │
           Valid?         Invalid
              │             │
             Yes            │
              │             │
              │◄────────────┘
              ▼
       Generate Computer Choice
              │
              ▼
       Compare Both Choices
              │
       ┌──────┼───────┐
       │      │       │
       ▼      ▼       ▼
     Draw    User    Computer
             Wins      Wins
       │      │         │
       └──────┴─────────┘
              │
              ▼
         Play Again?
          │       │
         Yes      No
          │       │
          │       ▼
          │      End
          │
          └──────► New Round
```

---

## 🛠️ Tech Stack

| Technology         | Purpose                                |
| ------------------ | -------------------------------------- |
| 🐍 Python          | Programming language                   |
| 🎲 `random`        | Generates computer's random choice     |
| 🔁 `while` loops   | Game and input loops                   |
| `if / elif / else` | Game logic and validation              |
| `try / except`     | Handles invalid input and interruption |
| 🖨️ `print()`      | Displays game information              |

---

## 🧩 Important Components

### Random Computer Choice

```python
Comp_choice = rn.randint(1, 3)
```

Generates a random number from `1` to `3`.

---

### User Input Validation

The program uses `try-except` to prevent the game from crashing when the user enters something that cannot be converted to an integer.

```python
try:
    User_choice = int(input("Enter your choice: "))
except ValueError:
    print("Invalid choice")
```

It then checks whether the number is actually between `1` and `3`.

---

### Draw Detection

A draw occurs when both players choose the same option:

```python
if ((User_choice == 1 and Comp_choice == 1) or
        (User_choice == 2 and Comp_choice == 2) or
        (User_choice == 3 and Comp_choice == 3)):
    print("<== Draw! ==>")
```

---

### User Win Detection

The program checks the three situations where the user wins:

```python
elif ((User_choice == 2 and Comp_choice == 1) or
      (User_choice == 1 and Comp_choice == 3) or
      (User_choice == 3 and Comp_choice == 2)):
    print("<== User wins! ==>")
```

These correspond to:

```text
Paper → Rock
Rock → Scissors
Scissors → Paper
```

---

## 🧠 Concepts Practiced

This project helped practice:

* 🔢 Integer input
* 🔁 Nested `while` loops
* 🔀 Conditional statements
* 🎲 Random number generation
* 🧪 Exception handling
* ⌨️ User input validation
* 🔄 Game replay logic
* 🧠 Boolean conditions
* 🛑 `KeyboardInterrupt` handling
* 🧩 Combining multiple conditions with `and` / `or`

---

## 💻 Code

```python
import random as rn

while True:
    flag = 0

    print(
        "Winning rules of the game ROCK PAPER SCISSORS are:\n"
        "Rock vs Paper -> Paper wins \n"
        "Rock vs Scissors -> Rock wins \n"
        "Paper vs Scissors -> Scissors wins \n"
    )

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

    if ((User_choice == 1 and Comp_choice == 1) or
            (User_choice == 2 and Comp_choice == 2) or
            (User_choice == 3 and Comp_choice == 3)):
        print("<== Draw! ==>")

    elif ((User_choice == 2 and Comp_choice == 1) or
          (User_choice == 1 and Comp_choice == 3) or
          (User_choice == 3 and Comp_choice == 2)):
        print("<== User wins! ==>")

    else:
        print("<== Computer Wins! ==>")

    while True:
        try:
            choice = input("Do you want to play again? (Y/N)\n > ").capitalize()
        except KeyboardInterrupt:
            print("\nGame interrupted by user. Exiting gracefully.")
            exit(0)

        if choice == "Y":
            break
        elif choice == "N":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Choose again")

    if choice == "N":
        break
```

---

## 🖥️ Example Gameplay

```text
Winning rules of the game ROCK PAPER SCISSORS are:
Rock vs Paper -> Paper wins
Rock vs Scissors -> Rock wins
Paper vs Scissors -> Scissors wins

Enter your choice
1 - Rock
2 - Paper
3 - Scissors

Enter your choice: 1

User choice is: Rock
Computer choice is: Scissors

<== User wins! ==>

Do you want to play again? (Y/N)
> Y
```

---

## ⚠️ Current Limitations / Minor Issues

The game works correctly, but there are a few things that could be improved:

* `flag = 0` is currently unused.
* Variable names such as `User_choice` and `Comp_choice` don't follow Python's usual `snake_case` naming convention.
* `"Chose again"` should be `"Choose again"`.
* The original interruption message in the replay section contains an extra `n`.
* `exit(0)` is used for terminating the program.
* The game logic contains several repetitive conditions.
* There is no score tracking across multiple rounds.

These are mostly **style and maintainability issues**, not major functional problems.

---

## 🚀 Future Improvements

Some possible improvements:

* 🏆 Add a score system.
* 📊 Display total wins, losses, and draws.
* 🎮 Add best-of-3 or best-of-5 mode.
* 🔢 Allow the player to choose the number of rounds.
* ✨ Replace numeric choices with `R`, `P`, and `S`.
* 🧹 Refactor repeated logic into functions.
* 🤖 Add different computer strategies.
* 🖥️ Create a graphical interface.
* 📈 Display game statistics at the end.

---

## 📈 Project Status

🟢 **Completed**

The current version supports:

* ✅ Rock, Paper, and Scissors
* ✅ Random computer choices
* ✅ Input validation
* ✅ Winner detection
* ✅ Draw detection
* ✅ Replay functionality
* ✅ `KeyboardInterrupt` handling

---

## 🎓 What I Learned

This project is a practical exercise in combining several basic Python concepts into a complete interactive program.

The main takeaway is learning how **loops, conditions, randomization, and exception handling** can work together to create a simple game.

---

## 👨‍💻 Author

**Uzair Khan**

GitHub: `khanuzair-f15`

Email: `khanuzair.f15@gmail.com`

---

⭐ If you enjoyed the project, consider giving the repository a star!
