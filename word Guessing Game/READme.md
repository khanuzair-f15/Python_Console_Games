# 🎯 Hangman Word Guessing Game

A simple Python **word guessing game** where the player tries to discover a randomly selected word by guessing one character at a time.

The game provides a list of predefined words, randomly selects one, and allows the player to reveal the hidden word by entering individual characters.

---

## 🚧 Under Construction

The current version has a **major game-logic issue with the guess counter** that needs to be fixed.

### 🔴 Guess Counter Logic

The game starts with:

```python
count = 12
```

and decreases the counter for every valid, new character:

```python
count = count - 1
```

This happens even when the player guesses a **correct character**.

More importantly, the game only checks:

```python
if count == 1:
```

If `count` reaches `0`, the condition is no longer true, so the game can continue running with:

```text
0 guesses
-1 guesses
-2 guesses
...
```

This means the losing condition is not reliably triggered.

### 🔧 Needs Improvement

The guess-count logic should be redesigned so that:

* The game properly ends when the allowed guesses are exhausted.
* The counter cannot continue into negative numbers.
* The intended number of guesses is accurately enforced.

> ⚠️ The README documents the current behavior and does **not** silently fix the code.

---

## 📌 Introduction

This project is a beginner-friendly implementation of a **Hangman-style word guessing game**.

The player enters their name and then attempts to guess the hidden word one character at a time.

For every guessed character:

* ✅ If the character exists in the word, it is revealed.
* ❌ If the character does not exist, the player receives a wrong-answer message.
* 🔁 Previously guessed characters cannot be entered again.
* 🏆 The player wins when all characters of the word have been discovered.
* 💀 The game is intended to end when the allowed guesses are exhausted.

---

## 🎮 Game Features

* 👤 Asks for the player's name
* 🎲 Randomly selects a word
* 🔤 Accepts one character at a time
* 🚫 Prevents duplicate character guesses
* 👀 Displays hidden characters using `_`
* ❌ Detects incorrect guesses
* 🏆 Detects when the complete word has been guessed
* 🔢 Includes a guess counter
* 🖥️ Runs entirely in the terminal

---

## 📚 Word List

The game currently selects from these predefined words:

```python
guess_list = [
    'word',
    'eraser',
    'pencil',
    'alphabet',
    'bottle',
    'perfume',
    'laptop',
    'computer',
    'bed',
    'door'
]
```

The program randomly selects one using:

```python
guess_word = random.choice(guess_list)
```

Therefore, the player doesn't know which word will be selected before the game begins.

---

## 🔄 How the Game Works

### 1. Enter Your Name

The program starts by asking:

```text
what is your name?
```

It then displays:

```text
Good luck! <name>
```

---

### 2. Select a Random Word

Python's `random.choice()` selects a word from the predefined list:

```python
guess_word = random.choice(guess_list)
```

For example:

```text
Selected word → laptop
```

The player isn't shown the actual word.

---

### 3. Start Guessing Characters

The player is asked:

```text
Guess a character:
```

The program requires exactly one character:

```python
if len(character) != 1:
    print("please enter a single character")
    continue
```

For example:

```text
a
```

is valid, while:

```text
abc
```

is rejected.

---

### 4. Prevent Duplicate Guesses

Previously guessed characters are stored in:

```python
temp = []
```

Before accepting a new character, the program checks:

```python
if character in temp:
```

If the character has already been guessed, the player is asked to choose another one.

---

## 🔤 Correct Guess

If the character exists in the selected word:

```python
if character in guess_word:
    temp.append(character)
```

The character is added to the list of correctly guessed characters.

For example, if the word is:

```text
laptop
```

and the player guesses:

```text
a
```

the displayed word becomes:

```text
_ a _ _ _ _
```

---

## ❌ Wrong Guess

If the character isn't present:

```python
else:
    print("Wrong")
```

The program also displays the remaining guess count.

Example:

```text
Wrong
You have 8 more guesses
```

---

## 👀 Displaying the Hidden Word

The program loops through every character in the selected word:

```python
for char in guess_word:
    if char in temp:
        print(char, end=" ")
    else:
        print("_", end=" ")
```

Correctly guessed characters are displayed while unknown characters remain hidden.

Example:

```text
_ e _ _ _ _
```

---

## 🏆 Winning Condition

The program checks whether every character in the word has been guessed:

```python
if all(char in temp for char in guess_word):
    print("You Win")
```

If all characters have been discovered, the game ends.

Example:

```text
You Win
The word is: pencil
```

---

## 💀 Losing Condition

The intended losing condition is:

```python
if count == 1:
    print("You loose")
    print(f"Correct word is {guess_word}")
    break
```

However, as mentioned in the **Under Construction** section, the current implementation has a logic problem because `count` can reach `0` before this condition is properly triggered.

This needs to be fixed before the game's attempt system can be considered fully reliable.

---

## 🔄 Program Flow

```text
                ┌─────────────┐
                │    Start    │
                └──────┬──────┘
                       │
                       ▼
                 Enter Name
                       │
                       ▼
               Select Random Word
                       │
                       ▼
              Set Guess Counter
                       │
                       ▼
              Ask for Character
                       │
                       ▼
              ┌────────────────┐
              │ Single Character│
              │     entered?   │
              └───────┬────────┘
                  No  │  Yes
                      │
              ┌───────▼───────┐
              │ Ask Again      │
              └───────────────┘
                      │
                      ▼
             Already Guessed?
                │          │
               Yes         No
                │           │
                ▼           ▼
             Ask Again   Reduce Count
                            │
                            ▼
                     Character in Word?
                       │          │
                      Yes         No
                       │           │
                       ▼           ▼
                  Reveal Char    "Wrong"
                       │           │
                       └─────┬─────┘
                             ▼
                     Display Word
                             │
                             ▼
                    Complete Word?
                      │        │
                     Yes       No
                      │         │
                      ▼         ▼
                   You Win   Check Guesses
                                │
                                ▼
                         Continue / Lose
```

---

## 🛠️ Tech Stack

| Technology       | Purpose                                     |
| ---------------- | ------------------------------------------- |
| 🐍 Python        | Main programming language                   |
| 🎲 `random`      | Selects a random word                       |
| 🔤 Strings       | Stores and checks words/characters          |
| 📋 Lists         | Stores guessed characters                   |
| 🔁 `while` loop  | Runs the game                               |
| 🔄 `for` loop    | Displays the hidden word                    |
| 🧠 `all()`       | Checks whether the complete word is guessed |
| 🛡️ `try-except` | Handles input-related exceptions            |

---

## 🧩 Important Components

### Random Word Selection

```python
guess_word = random.choice(guess_list)
```

Selects one random word from the predefined list.

---

### Guess Tracking

```python
temp = []
```

Stores characters that the player has already guessed correctly.

---

### Character Validation

```python
if len(character) != 1:
    print("please enter a single character")
    continue
```

Prevents the player from entering multiple characters at once.

---

### Duplicate Prevention

```python
if character in temp:
    print("You already guessed this caracter")
    continue
```

Prevents the same character from being guessed repeatedly.

---

### Word Completion Check

```python
if all(char in temp for char in guess_word):
    print("You Win")
```

Checks whether every character in the selected word has been guessed.

---

## 🧠 Concepts Practiced

This project demonstrates:

* 🐍 Python fundamentals
* 🎲 Random selection
* 🔤 String manipulation
* 📋 Lists
* 🔁 `while` loops
* 🔄 `for` loops
* 🧠 `if / elif / else`
* 🛡️ Exception handling
* 🔎 Membership operators
* 🧮 `len()`
* ✅ `all()`
* ⌨️ User input
* 🎮 Game-state logic

---

## 💻 Current Code

```python
import random

name = input("what is your name? ")
print("Good luck! " + name)

guess_list = [
    'word',
    'eraser',
    'pencil',
    'alphabet',
    'bottle',
    'perfume',
    'laptop',
    'computer',
    'bed',
    'door'
]

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
```

---

## 🖥️ Example Gameplay

A successful round might look like:

```text
what is your name? Uzair
Good luck! Uzair

Guess a character: p
_ _ _ p _ _

Guess a character: e
_ e _ p _ _

Guess a character: n
_ e n p _ _

...
```

The exact word and output depend on the random selection.

---

## ⚠️ Known Issues

In addition to the major counter issue, there are several smaller issues:

### Spelling / Grammar

Some messages contain typos:

```text
caracter → character
loose → lose
```

There are also some inconsistent capitalization choices.

### Exception Handling

The program catches:

```python
except ValueError:
except IndexError:
```

However, the operations inside the `try` block don't normally produce these exceptions from ordinary character input.

Therefore, these handlers currently don't provide much practical benefit.

### Case Sensitivity

The game treats uppercase and lowercase characters as different.

For example:

```text
A ≠ a
```

A future version could normalize input with `.lower()`.

---

## 🚀 Future Improvements

Possible improvements include:

* 🔧 Fix the guess-counter logic.
* 🔤 Make guessing case-insensitive.
* 🧠 Don't consume attempts for correct guesses.
* 🎯 Add a proper maximum-attempt system.
* 📝 Expand the word database.
* 💡 Add hints.
* ❤️ Display lives visually.
* 📊 Add score tracking.
* 🔄 Add a replay option.
* 🏆 Add difficulty levels.
* 🎨 Improve terminal UI.
* 🧹 Refactor the program into functions.

---

## 📊 Project Structure

```text
Hangman/
│
├── main.py
└── README.md
```

---

## 📌 Project Status

🟠 **Under Construction**

The core word-guessing functionality works, but the **guess counter and losing condition need to be corrected** before the project can be considered fully complete.

### Current Status

* ✅ Random word selection
* ✅ User name input
* ✅ Single-character validation
* ✅ Duplicate guess detection
* ✅ Correct character detection
* ✅ Hidden word display
* ✅ Win detection
* ⚠️ Guess counter logic needs fixing
* ⚠️ Losing condition needs fixing

---

## 🎓 What I Learned

This project is a good exercise in turning basic Python concepts into an interactive game.

The most important concept here is **maintaining game state**:

```text
Selected Word
      +
Guessed Characters
      +
Remaining Attempts
      ↓
   Game State
      ↓
 Win / Lose
```

It also highlights how a seemingly small condition such as:

```python
if count == 1:
```

can significantly affect the behavior of an entire game.

---

## 👨‍💻 Author

**Uzair Khan**

GitHub: `khanuzair-f15`

Email: `khanuzair.f15@gmail.com`

---

⭐ If you found this project useful, consider giving the repository a star!
