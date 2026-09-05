# 🎯 Number Guessing Game

A simple **Python command-line number guessing game** where the player chooses a range and then tries to guess the randomly generated number within **7 valid attempts**.

After every guess, the game provides a hint:

* 🔽 **Too Low** — the guessed number is smaller than the secret number.
* 🔼 **Too High** — the guessed number is larger than the secret number.
* 🎯 **Correct!** — the player has found the secret number.

The goal is to guess the number using as few attempts as possible.

---

## 🎮 How the Game Works

The game follows a simple two-stage process:

```text
        ┌─────────────────────┐
        │      Start Game     │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │ Enter Lower Bound   │
        │ Enter Upper Bound   │
        └──────────┬──────────┘
                   │
                   ▼
            Valid Range?
             /        \
           No          Yes
           │            │
           │            ▼
           │     Generate Random
           │        Number
           │            │
           └──────►     ▼
                 ┌──────────────┐
                 │ Enter Guess  │
                 └──────┬───────┘
                        │
                        ▼
                  Valid Guess?
                   /       \
                 No         Yes
                 │           │
                 │           ▼
                 │      Compare Guess
                 │           │
                 │     ┌─────┼─────┐
                 │     │     │     │
                 │    Low   High  Correct
                 │     │     │     │
                 │     └─────┴─────┘     │
                 │           │           ▼
                 │           │          🏆
                 │           │         WIN
                 │           │
                 │        Attempt 7?
                 │          /   \
                 │        No     Yes
                 │        │       │
                 └────────┘       ▼
                                  ❌
                                 LOSE
```

---

## 📜 Rules

1. The player enters a **lower bound**.
2. The player enters an **upper bound**.
3. The lower bound must be smaller than the upper bound.
4. The computer randomly selects a number within the given range.
5. The generated number is **inclusive** of both bounds.
6. The player gets a maximum of **7 valid attempts**.
7. Invalid non-integer input does not consume an attempt.
8. A guess outside the selected range does not consume an attempt.
9. After every valid guess, the game gives a **Too Low** or **Too High** hint.
10. Guessing the correct number immediately ends the game.
11. If the player fails to guess correctly within 7 valid attempts, the game is lost.
12. The correct number is revealed after losing.

---

## 🏆 Winning Condition

The player wins when the guessed number matches the randomly generated number:

```python
elif random_number == guessed_number:
```

The program then displays:

```text
Correct!
Congratulation Ibra
Total Guesses 3
```

The number of guesses used is also shown.

---

## ❌ Losing Condition

The player loses after **7 valid guesses** without finding the correct number.

```python
if count > 6:
    print("You exceeds the guesses limit")
    print("Loser")
    print(f"Correct number is {random_number}")
    break
```

The secret number is revealed so the player can see the answer.

---

## 🛠️ Tech Stack

| Technology                | Purpose                     |
| ------------------------- | --------------------------- |
| 🐍 **Python**             | Main programming language   |
| 🎲 **`random.randint()`** | Generates the secret number |
| 💻 **Command Line**       | User interface              |
| 🛡️ **`try-except`**      | Handles invalid input       |

The project uses only Python's **standard library**, so no external packages are required.

---

## ⚙️ Main Components

### 🎲 Random Number Generation

The program imports `randint` from Python's `random` module:

```python
from random import randint
```

The secret number is generated using:

```python
random_number = randint(lower_bound, upper_bound)
```

This means both the lower and upper bounds are included.

For example:

```text
Range: 1 - 20

Possible numbers:
1, 2, 3, ... 18, 19, 20
```

---

### 📏 Range Validation

The program checks whether the user has entered a valid range:

```python
if lower_bound >= upper_bound:
    print("upper bound cannot be less than or equal to lower bound")
    continue
```

This prevents the game from starting with an invalid range.

---

### ⌨️ Guess Validation

The player's guess is converted into an integer:

```python
guessed_number = int(input(f"Guess {count + 1}: "))
```

If the player enters something that cannot be converted to an integer, `ValueError` is handled:

```python
except ValueError:
    print("Entered value is not correct")
    print("Guess again")
```

---

### 🎯 Range Checking for Guesses

The program also makes sure the guess belongs to the selected range:

```python
if guessed_number < lower_bound or guessed_number > upper_bound:
    print("Guess the number must be in the given range")
    continue
```

An out-of-range guess **does not consume one of the 7 attempts**.

---

### 🔽 Too Low / 🔼 Too High

The program compares the guess with the secret number:

```python
if random_number > guessed_number:
    print("Too Low")

elif random_number < guessed_number:
    print("Too High")
```

This provides the player with a useful hint after every valid guess.

---

### 🧮 Attempt Counter

The attempt counter starts at:

```python
count = 0
```

and increases only after a valid guess:

```python
count = count + 1
```

This means invalid input and out-of-range guesses don't reduce the player's available attempts.

---

## 🧠 Skills & Concepts Used

This project demonstrates several important Python programming concepts.

### 🐍 Python Fundamentals

* Variables
* Integers
* Strings
* User input
* Conditional statements
* `while` loops
* Comparison operators
* Formatted strings

### 🎲 Randomization

Using:

```python
randint(lower_bound, upper_bound)
```

to generate unpredictable values.

### 🔄 Loops

Two main loops are used:

**Setup loop**

* Gets the range
* Validates the range
* Generates the random number

**Guessing loop**

* Takes guesses
* Validates guesses
* Tracks attempts
* Determines win/loss

### 🛡️ Exception Handling

The program uses `try-except` to prevent invalid user input from crashing the program.

For example:

```python
try:
    guessed_number = int(input(f"Guess {count + 1}: "))
except ValueError:
    print("Entered value is not correct")
```

---

## 💻 Example Gameplay

```text
Enter lower bound: 1
Enter upper bound: 20

now you have 7 chance to find the correct number between 1 and 20

Guess 1: 10
Too Low

Guess 2: 15
Too High

Guess 3: 12
Too Low

Guess 4: 14
Correct!

Congratulation Ibra
Total Guesses 4
```

---

## 📊 Project Features

| Feature                           | Status |
| --------------------------------- | :----: |
| Custom lower bound                |    ✅   |
| Custom upper bound                |    ✅   |
| Random number generation          |    ✅   |
| Inclusive range                   |    ✅   |
| Maximum 7 valid attempts          |    ✅   |
| Too High / Too Low hints          |    ✅   |
| Correct answer detection          |    ✅   |
| Invalid integer handling          |    ✅   |
| Out-of-range guess handling       |    ✅   |
| Secret number revealed after loss |    ✅   |
| Score/high-score system           |    ❌   |
| Play-again option                 |    ❌   |
| Difficulty levels                 |    ❌   |
| GUI                               |    ❌   |

---

## 🐛 Known Issues & Minor Improvements

The current version is **functional**, but there are a few small issues that could be improved.

### ⚠️ Broad `except` Blocks

The program contains:

```python
except:
    print("Something went wrong please restart the game")
```

A bare `except` catches almost every type of exception.

It would be better to catch specific exceptions where possible.

---

### ⚠️ Restart Message

The program says:

```text
Something went wrong please restart the game
```

but the program doesn't actually restart itself. It simply exits the relevant loop.

The message could therefore be changed to something more accurate.

---

### ✏️ Minor Grammar Issues

Some output messages contain grammatical mistakes, for example:

```text
You exceeds the guesses limit
```

could be:

```text
You exceeded the guess limit.
```

Similarly:

```text
Congratulation Ibra
```

could be:

```text
Congratulations, Ibra!
```

These are only presentation issues and don't affect the functionality.

---

### ⚠️ Hardcoded Attempt Limit

The number of attempts is effectively hardcoded to **7**:

```python
if count > 6:
```

A future version could store this in a variable:

```python
MAX_ATTEMPTS = 7
```

This would make the value easier to change.

---

## 🚀 Future Improvements

Possible improvements for future versions:

* 🎚️ Add difficulty levels
* 🔢 Allow the player to choose the number of attempts
* 🏆 Add a high-score system
* 📊 Track average guesses
* 🔁 Add a play-again option
* 💡 Add smarter hints
* 🎨 Improve terminal UI
* 🌈 Add colored output
* 🖥️ Create a graphical interface
* 🌐 Create a web version
* 🧪 Add automated tests

---

## 📚 What I Learned

This project was created to practice **Python fundamentals through a simple interactive game**.

The main concepts practiced were:

> **Randomization + Loops + Conditions + Input Validation + Exception Handling + User Input**

The project also helped demonstrate how to build a complete small program where **input validation, game logic, attempt tracking, and win/loss conditions** work together.

---

## 📌 Project Status

🟢 **Working**

The current version successfully implements a customizable number guessing game with:

* A user-defined range
* Random number generation
* Seven valid attempts
* Higher/lower hints
* Input validation
* Win and loss conditions

This is primarily a **Python learning project** focused on practicing basic programming and game logic.

---

## 👨‍💻 Author

**Uzair Khan**

📧 **Email:** [khanuzair.f15@gmail.com](mailto:khanuzair.f15@gmail.com)

---

⭐ Feel free to explore the code and experiment with different ranges, attempt limits, and game mechanics.

**Made with 🐍 Python & a little bit of guessing! 🎯**
