# 📈 Higher Lower Game

A simple **Python command-line guessing game** inspired by the classic **Higher Lower** concept.

The player is shown two accounts and has to guess **which account has more followers**.

Every correct answer increases the score, while a wrong answer ends the current round. The player can then choose whether to play again.

---

## 🎮 How the Game Works

The game displays two accounts:

```text
------<=Account 1=>------
~ Name: Instagram
~ Country: United States

       VS

------<=Account 2=>------
~ Name: Cristiano Ronaldo
~ Country: Portugal
```

The player then has to guess which account has the **higher follower count**.

If the answer is correct:

```text
Your current score is: 1
```

The game continues with a new comparison.

If the answer is incorrect:

```text
Wrong guess
```

The current round ends and the player gets the option to play again.

---

## 📜 Rules

1. Two accounts are randomly selected from the game data.
2. The two accounts must be different.
3. The follower counts are hidden from the player.
4. The player guesses which account has more followers.
5. The answer is entered using the account's name.
6. A correct answer increases the score by **1**.
7. After a correct answer, the previous second account becomes the first account.
8. A new account is randomly selected as the second account.
9. If the player gives a wrong answer, the round ends.
10. The player can choose to play another round.

---

## 🏆 Scoring

The score represents the number of consecutive correct guesses.

For example:

```text
Correct → Score: 1
Correct → Score: 2
Correct → Score: 3
Wrong   → Game Over
```

The higher the score, the better the player's performance.

---

## 🛠️ Tech Stack

| Technology            | Purpose                                |
| --------------------- | -------------------------------------- |
| 🐍 **Python**         | Main programming language              |
| 🎲 **random**         | Randomly selects accounts              |
| 🖥️ **OS module**     | Clears the terminal                    |
| 📦 **Python modules** | Separates game data, artwork and logic |
| 💻 **Command Line**   | User interface                         |

The project uses only Python's built-in modules and does **not require external packages**.

---

## 📁 Project Structure

```text
Higher-Lower/
│
├── main.py
├── art.py
└── game_data.py
```

### `main.py`

Contains the main game logic, user interaction, score handling, and comparison system.

### `art.py`

Contains the ASCII artwork used by the game:

* Game logo
* VS artwork

### `game_data.py`

Contains the account data used by the game.

Each account contains:

```python
{
    'name': 'Instagram',
    'follower_count': 346,
    'description': 'Social media platform',
    'country': 'United States'
}
```

---

# ⚙️ Functions

## `clear()`

Clears the terminal to keep the game interface clean.

```python
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
```

It checks the operating system:

* `cls` → Windows
* `clear` → Linux/macOS

---

## `assign()`

Randomly selects an account from the `data` list.

```python
def assign():
    return rn.choice(data)
```

This uses:

```python
random.choice()
```

to randomly select one account.

---

## `compare()`

Determines which of the two accounts has more followers and checks whether the player's answer matches it.

```python
def compare(person1, person2, user_input):
```

The function:

1. Gets the follower count of both accounts.
2. Determines which account has the larger follower count.
3. Gets the name of that account.
4. Compares it with the user's answer.
5. Returns `True` or `False`.

```text
Correct answer → True
Wrong answer   → False
```

---

## `play_higher_lower()`

This is the **main game function**.

It controls:

* Account selection
* Score
* Game rounds
* User input
* Answer checking
* Displaying the game
* Restarting the game

The function contains the main game loops.

---

# 🧠 Skills & Concepts Used

This project demonstrates several important Python concepts.

### 🐍 Python Fundamentals

* Variables
* Functions
* Lists
* Dictionaries
* Strings
* Conditional statements
* `while` loops
* User input
* String formatting

### 📦 Modules

The project demonstrates how to divide a Python project into multiple files:

```python
from game_data import data
from art import logo, vs
```

This makes the project more organized than keeping everything inside one file.

### 🎲 Randomization

The program uses:

```python
rn.choice(data)
```

to randomly select accounts.

This makes each game round less predictable.

### 🗂️ Dictionaries

Account information is stored using dictionaries:

```python
{
    'name': 'Ariana Grande',
    'follower_count': 183,
    'description': 'Musician and actress',
    'country': 'United States'
}
```

Values can then be accessed using:

```python
person.get("name")
person.get("country")
person.get("follower_count")
```

### 🔄 Loops

`while` loops are used to:

* Keep the game running
* Continue the guessing rounds
* Prevent duplicate account selection
* Validate the play-again option

### 🧹 Terminal Control

The `os` module is used to clear the terminal after each correct guess:

```python
os.system('cls' if os.name == 'nt' else 'clear')
```

This gives the game a cleaner interface.

---

# 🔄 Game Flow

```text
                ┌────────────────────┐
                │    Start Game      │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Select Account 1   │
                │ Select Account 2   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Display Accounts   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │  Player's Guess    │
                └─────────┬──────────┘
                          │
                ┌─────────┴─────────┐
                │                   │
             Correct              Wrong
                │                   │
                ▼                   ▼
        ┌──────────────┐      ┌──────────────┐
        │ Score + 1    │      │ Game Over    │
        └──────┬───────┘      └──────┬───────┘
               │                     │
               ▼                     ▼
        New Account Pair?       Play Again?
               │                  /       \
               │                Yes        No
               │                 │          │
               └─────────────────┘          ▼
                                           Exit
```

---

# 💻 Example Gameplay

```text
  _    _ _       _                 _
 | |  | (_)     | |               | |
 | |__| |_  __ _| |__   ___ _ __  | |
 |  __  | |/ _` | '_ \ / _ \ '__| | |
 | |  | | | (_| | | | |  __/ |    | |___
 |_|  |_|_|\__, |_| |_|\___|_|    |______|
            __/ |
           |___/

------<=Account 1=>------
~ Name: Instagram
~ Country: United States

 _    __
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)

------<=Account 2=>------
~ Name: Ariana Grande
~ Country: United States

----------------------------------------------
Your current score is: 0
----------------------------------------------

Enter your guess: instagram
```

If Instagram has more followers:

```text
Score: 1
```

The game continues.

---

# ▶️ How to Run

### 1. Install Python

Make sure Python is installed:

```bash
python --version
```

### 2. Keep all files in the same folder

```text
Higher-Lower/
├── main.py
├── art.py
└── game_data.py
```

### 3. Run the game

Open a terminal in the project directory:

```bash
python main.py
```

---

# 📊 Project Features

| Feature                      | Status |
| ---------------------------- | :----: |
| Player vs Computer/Data      |    ✅   |
| Random account selection     |    ✅   |
| Follower comparison          |    ✅   |
| Score tracking               |    ✅   |
| Duplicate account prevention |    ✅   |
| ASCII logo                   |    ✅   |
| VS artwork                   |    ✅   |
| Terminal clearing            |    ✅   |
| Play again option            |    ✅   |
| Input validation             |    ✅   |
| Separate game data file      |    ✅   |
| Separate artwork file        |    ✅   |
| Difficulty levels            |    ❌   |
| High-score storage           |    ❌   |
| Large account database       |    ❌   |
| GUI                          |    ❌   |

---

# 🐛 Known Issues & Minor Improvements

The current version is **functional**, but there are a few minor things that could be improved.

### ⚠️ Limited Game Data

The current `game_data.py` contains only **three accounts**:

```text
Instagram
Cristiano Ronaldo
Ariana Grande
```

This makes the game fairly repetitive after several rounds.

Adding more accounts would make the game much more interesting.

---

### ⚠️ `Maxx` Naming

The variable:

```python
Maxx = ""
```

works correctly, but Python's usual naming convention would be:

```python
max_account = ""
```

This would make the code more descriptive.

---

### ⚠️ Typo in Play Again Message

The program currently says:

```text
You wanna pay again (Y/N) ?
```

This should be:

```text
You wanna play again (Y/N) ?
```

This is only a display/typing issue.

---

### ⚠️ Unused Account Information

Each account contains a:

```python
'description'
```

field, but the current game doesn't display or use it.

For example:

```python
'description': 'Footballer'
```

This could be incorporated into the game display in a future version.

---

### ⚠️ Input Matching

The player's answer is compared with the account name.

Because the input is converted to lowercase, capitalization isn't important, but the user still needs to enter the account's name correctly.

A future version could provide options such as:

```text
A → Account 1
B → Account 2
```

This would make the game easier to play.

---

# 🚀 Future Improvements

Possible improvements for future versions:

* 📚 Add hundreds of accounts
* 🏆 Add a high-score system
* 💾 Save player scores
* 📈 Add difficulty levels
* 🎯 Allow `A/B` answers instead of typing names
* 👤 Display account descriptions
* 📊 Add game statistics
* 🎨 Improve terminal UI
* 🌈 Add terminal colors
* 🖥️ Create a graphical version
* 🌐 Create a web version
* 🧪 Add automated tests
* 🔊 Add sound effects

---

# 📚 What I Learned

This project helped me practice **Python programming using multiple files and basic game logic**.

The main concepts practiced were:

> **Functions + Lists + Dictionaries + Loops + Randomization + Modules + User Input + Conditional Logic**

One of the important things learned from this project was how to organize a Python program into separate files:

```text
main.py       → Game logic
game_data.py  → Data
art.py        → Visuals
```

This makes the project easier to read and maintain.

---

# 📌 Project Status

🟢 **Working**

The current version successfully implements the basic Higher Lower game in the terminal.

The project is primarily a **Python learning project** focused on practicing randomization, dictionaries, functions, loops, modules, and game logic.

---

## 👨‍💻 Author

**Uzair Khan**

📧 **Email:** [khanuzair.f15@gmail.com](mailto:khanuzair.f15@gmail.com)

---

⭐ Feel free to explore the code, add more accounts to `game_data.py`, and experiment with the game logic.

**Made with 🐍 Python, 🎲 randomness & 📈 follower counts**
