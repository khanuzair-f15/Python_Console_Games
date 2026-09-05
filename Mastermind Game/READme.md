# 🧠 Mastermind — 4-Digit Guessing Game

A simple **Python command-line guessing game** inspired by the classic Mastermind concept.

The computer randomly generates a **4-digit number**, and the player tries to guess it.

After every guess, the game tells the player how many digits are **correct and in the correct position**.

The goal is to become a **Mastermind** by guessing the complete number in as few attempts as possible. 🎯

---

## 🎮 How the Game Works

At the beginning of the game, Python randomly generates a 4-digit number.

For example:

```text id="jv2v8d"
Secret Number: 5831
```

The player then enters guesses:

```text id="0y5tdu"
Guess: 5839

Result:
3 digits correct
```

The program checks each position individually.

```text id="s1l2kw"
Secret:  5 8 3 1
Guess:   5 8 3 9
         ✓ ✓ ✓ ✗

Correct digits: 3
```

The game continues until all **4 digits are correct in their exact positions**.

---

## 📜 Rules

1. The computer generates a random **4-digit number**.
2. The number is between **1000 and 9999**.
3. The player must enter a valid 4-digit number.
4. Invalid input is rejected.
5. After every valid guess, the program checks each digit.
6. A digit is counted as correct only if it is in the **correct position**.
7. If all 4 digits match, the player wins.
8. There is **no maximum attempt limit**.
9. The objective is to guess the number using as few attempts as possible.

---

## 🏆 Winning Condition

The player wins when:

```python id="dd9hsk"
count == 4
```

The program then displays:

```text id="70s7di"
You've become a Mastermind!
It took you only 6 tries.
```

---

## 🛠️ Tech Stack

| Technology           | Purpose                     |
| -------------------- | --------------------------- |
| 🐍 **Python**        | Main programming language   |
| 🎲 **random module** | Generates the secret number |
| 💻 **Command Line**  | User interface              |

The project uses only Python's built-in functionality and **does not require any external packages**.

---

## ⚙️ Main Components

### 🎲 Random Number Generation

The secret number is generated using:

```python id="n4q0zo"
n = rn.randint(1000, 9999)
```

The number is then converted into a list of characters:

```python id="7v5w2q"
n = list(str(n))
```

For example:

```text id="zj1gye"
5831
 ↓
['5', '8', '3', '1']
```

This makes it possible to compare individual digits.

---

### ⌨️ User Input

The player enters a guess:

```python id="hzq18c"
number = int(input("Guess the 4-digit number: "))
```

The program checks whether the number is within the valid range:

```python id="k84vde"
if not 1000 <= number <= 9999:
```

If the input is invalid, the program asks the player to try again.

---

### 🔢 Digit Comparison

The program compares the secret number and the player's guess position by position:

```python id="4d7q91"
for i in range(len(n)):
    if n[i] == number[i]:
        count += 1
```

For example:

```text id="q2i5cl"
Secret:  7 4 2 9
Guess:   7 1 2 5
         ✓ ✗ ✓ ✗

Result: 2 digits correct
```

---

### 🧮 Attempt Counter

Every valid guess increases the attempt counter:

```python id="l0q2pj"
attempts += 1
```

The number of attempts is displayed when the player wins.

---

## 🧠 Skills & Concepts Used

This project demonstrates several Python fundamentals.

### 🐍 Python Basics

* Variables
* Integers
* Strings
* Lists
* `if / else`
* `while` loops
* `for` loops
* User input
* Type conversion
* Comparison operators

### 🎲 Randomization

The `random` module is used to generate the secret number:

```python id="g35s0n"
rn.randint(1000, 9999)
```

### 🔄 Loops

Nested loops are used to:

* Validate user input
* Keep the game running
* Compare the digits

### 🛡️ Exception Handling

The program uses `try-except` to prevent invalid input from crashing the game:

```python id="vbb2qm"
try:
    number = int(input("Guess the 4-digit number: "))
except ValueError:
    print("Invalid input")
```

It also handles `KeyboardInterrupt` so the user can exit using `Ctrl+C`.

---

## 🔄 Program Flow

```text id="yikg3d"
┌──────────────────────┐
│     Start Game       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Generate 4-Digit     │
│ Secret Number        │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Enter 4-Digit Guess  │
└──────────┬───────────┘
           │
           ▼
      Valid Input?
       /        \
     No          Yes
     │            │
     │            ▼
     │    ┌─────────────────┐
     │    │ Compare Digits  │
     │    └────────┬────────┘
     │             │
     │             ▼
     │       Count Matches
     │             │
     │       ┌─────┴─────┐
     │       │           │
     │     4 Match     < 4 Match
     │       │           │
     │       ▼           ▼
     │     🏆 WIN     Try Again
     │
     └───────────────┐
                     │
                     └──────► Enter Guess
```

---

## 💻 Example Gameplay

```text id="8v5hgc"
Welcome to Mastermind!
Try to guess the 4-digit number.

Guess the 4-digit number: 1234
Not quite the number. You got 0 digit(s) correct.

Guess the 4-digit number: 5834
Not quite the number. You got 3 digit(s) correct.

Guess the 4-digit number: 5831

You've become a Mastermind!
It took you only 3 tries.
```

---

## ▶️ How to Run

### 1. Install Python

Check whether Python is installed:

```bash id="gr0f4q"
python --version
```

### 2. Save the program

For example:

```text id="3qf8a4"
mastermind.py
```

### 3. Run the game

```bash id="b6oy2k"
python mastermind.py
```

No external packages are required.

---

## 📊 Project Features

| Feature                     | Status |
| --------------------------- | :----: |
| Random 4-digit number       |    ✅   |
| Input validation            |    ✅   |
| Digit comparison            |    ✅   |
| Correct-position counting   |    ✅   |
| Attempt counter             |    ✅   |
| Win condition               |    ✅   |
| Invalid input handling      |    ✅   |
| Keyboard interrupt handling |    ✅   |
| Maximum attempt limit       |    ❌   |
| Hints                       |    ❌   |
| Difficulty levels           |    ❌   |
| Score system                |    ❌   |
| GUI                         |    ❌   |

---

## 🐛 Known Issues & Limitations

The current version is **functional**, but there are some limitations.

### ⚠️ Not Full Traditional Mastermind

The current game only counts digits that are:

> **Correct digit + Correct position**

For example:

```text id="4jq9e1"
Secret: 5831
Guess:  1583
```

Although all four digits are present, the current program would not count them as correct because none are in the correct position.

A traditional Bulls/Cows-style Mastermind implementation would also detect **correct digits in the wrong positions**.

---

### ⚠️ No Maximum Attempt Limit

The player can continue guessing indefinitely until the correct number is found.

A future version could introduce:

```text id="z0j8xx"
Maximum Attempts: 10
```

and provide a losing condition when the limit is reached.

---

### ✏️ Minor Typo

The program currently prints:

```text id="8h5q9p"
Quiting...!!!
```

The correct spelling is:

```text id="9glfdd"
Quitting...!!!
```

This does not affect the game.

---

## 🚀 Future Improvements

Possible additions for future versions:

* 🐂 Add Bulls and Cows-style feedback
* 🎯 Add difficulty levels
* 🔢 Add a maximum number of attempts
* 💡 Add hints
* 🏆 Add a scoring system
* 📊 Track best scores
* 🔁 Add a play-again option
* 🎨 Add a graphical interface
* 🌈 Improve terminal formatting
* 🧪 Add automated tests
* 📈 Show game statistics

---

## 📚 What I Learned

This project was created to practice **Python fundamentals through a simple guessing game**.

The main concepts practiced were:

> **Randomization + Lists + Strings + Loops + Conditions + Input Validation + Exception Handling**

The project also provided practice with comparing individual elements of lists and using a counter to track the number of correct positions.

---

## 📌 Project Status

🟢 **Working**

The current version successfully implements a basic 4-digit number guessing game.

It is primarily a **Python learning project** focused on practicing loops, lists, random numbers, input validation, and basic game logic.

---

## 👨‍💻 Author

**Uzair Khan**

📧 **Email:** [khanuzair.f15@gmail.com](mailto:khanuzair.f15@gmail.com)

---

⭐ Feel free to explore the code and experiment with adding hints, difficulty levels, or full Bulls & Cows-style feedback.

**Made with 🐍 Python & a little bit of guessing! 🧠🎯**
