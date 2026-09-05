# 🔥 FLAMES Game

A simple **Python command-line implementation of the classic FLAMES game**.

The program takes two names, removes their common characters, counts the remaining characters, and uses that count to eliminate relationship options in a circular manner.

The last remaining option is displayed as the predicted relationship. ❤️😂

> **F** — Friends
> **L** — Lovers
> **A** — Affection
> **M** — Marriage
> **E** — Enemies
> **S** — Siblings

---

## 🎮 How the Game Works

The program follows these basic steps:

```text
Two Names
    ↓
Convert to lowercase
    ↓
Remove spaces
    ↓
Remove common characters
    ↓
Count remaining characters
    ↓
Create FLAMES list
    ↓
Circular elimination
    ↓
One option remains
    ↓
Display Relationship
```

---

## 📜 Rules

1. Enter your name.
2. Enter your friend's name.
3. Both names are converted to lowercase.
4. Spaces are removed from the names.
5. Common characters are removed from both names.
6. The remaining characters are counted.
7. The count is used to eliminate options from the FLAMES list.
8. Elimination happens in a circular manner.
9. The last remaining option is displayed as the relationship result.
10. The player can choose to play again.

---

## 🔥 FLAMES Categories

| Letter | Relationship         |
| :----: | -------------------- |
|  **F** | 👥 Friends           |
|  **L** | ❤️ Lovers            |
|  **A** | 💕 Affection         |
|  **M** | 💍 Marriage          |
|  **E** | ⚔️ Enemies           |
|  **S** | 👨‍👩‍👧‍👦 Siblings |

---

## 🛠️ Tech Stack

| Technology          | Purpose                   |
| ------------------- | ------------------------- |
| 🐍 **Python**       | Main programming language |
| 💻 **Command Line** | User interface            |
| 🔤 **Strings**      | Processing names          |
| 📋 **Lists**        | Storing FLAMES options    |

The project uses Python's built-in functionality and does **not require any external package**.

---

## ⚙️ Main Operations

### 📝 Taking Names as Input

The program takes two names from the user:

```python
name1 = input("Enter your name: ").lower().replace(" ", "")
name2 = input("Enter your friend: ").lower().replace(" ", "")
```

The names are converted to lowercase and spaces are removed.

For example:

```text
"Uzair Khan"
      ↓
"uzairkhan"
```

This makes the comparison case-insensitive.

---

### ✂️ Removing Common Characters

The program compares the characters of both names:

```python
for i in list(name1):
    for j in list(name2):
        if i == j:
            name1 = name1.replace(i, "", 1)
            name2 = name2.replace(j, "", 1)
            break
```

When a matching character is found, one occurrence is removed from each name.

---

### 🔢 Counting Remaining Characters

After common characters have been removed:

```python
count = len(name1 + name2)
```

The remaining characters from both names are combined and counted.

This count becomes the basis for the FLAMES elimination process.

---

### 🔥 Creating the FLAMES List

The six relationship options are stored in a Python list:

```python
flames = [
    'Friends', 'Lovers', 'Affection',
    'Marriage', 'Enemies', 'Siblings'
]
```

The program removes options from this list until only one remains.

---

### 🔄 Circular Elimination

The program uses the modulo operator to perform circular elimination:

```python
ele = (count + start - 1) % len(flames)
```

The selected option is then removed:

```python
flames.pop(ele)
```

The process continues until:

```python
len(flames) == 1
```

The remaining option becomes the final result.

---

## 🧠 Skills & Concepts Used

This project demonstrates several Python programming concepts.

### 🐍 Python Fundamentals

* Variables
* Strings
* Lists
* `for` loops
* `while` loops
* `if / elif / else`
* User input
* String methods
* List methods

### 🔤 String Manipulation

The project uses methods such as:

```python
.lower()
.replace()
```

to clean and process user input.

### 📋 List Operations

The FLAMES list is modified using:

```python
list()
.pop()
```

### 🔄 Loops

Loops are used for:

* Comparing characters
* Performing circular elimination
* Running the game repeatedly
* Validating the play-again choice

### ➗ Modulo Operator

The modulo operator `%` is used to create circular indexing:

```python
(count + start - 1) % len(flames)
```

This is a useful technique for solving problems involving **circular lists**.

### 🛡️ Exception Handling

The program also handles interruptions and unexpected errors:

```python
try:
    choice = input("Wanna play again (Y/n) ?")
except KeyboardInterrupt:
    print("Something went wrong")
    break
```

---

## 💻 Example Gameplay

```text
Enter your name: Uzair
Enter your friend: Ibra

Relationship status: Friends

Wanna play again (Y/n) ? y

Enter your name: Alice
Enter your friend: Bob

Relationship status: Enemies

Wanna play again (Y/n) ? n
```

The result depends on the characters present in the two names.

---

## 🔄 Program Flow

```text
┌──────────────────────┐
│     Start Program    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Enter Two Names    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Lowercase + Remove   │
│ Spaces               │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Remove Common        │
│ Characters           │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Count Remaining      │
│ Characters           │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Create FLAMES List   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Circular Elimination │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Display Result       │
└──────────┬───────────┘
           │
           ▼
       Play Again?
        /      \
      Yes       No
       │         │
       ▼         ▼
    Restart     Exit
```

---

## ▶️ How to Run

### 1. Install Python

Check if Python is installed:

```bash
python --version
```

### 2. Save the program

For example:

```text
flames.py
```

### 3. Run the program

```bash
python flames.py
```

No external Python packages are required.

---

## 📊 Project Features

| Feature                      | Status |
| ---------------------------- | :----: |
| Two-name input               |    ✅   |
| Lowercase conversion         |    ✅   |
| Space removal                |    ✅   |
| Common character removal     |    ✅   |
| Remaining character counting |    ✅   |
| FLAMES categories            |    ✅   |
| Circular elimination         |    ✅   |
| Relationship result          |    ✅   |
| Play-again option            |    ✅   |
| Invalid choice handling      |    ✅   |
| Keyboard interrupt handling  |    ✅   |
| GUI                          |    ❌   |
| Statistics                   |    ❌   |

---

## 🐛 Known Issues & Minor Improvements

The current version is **functional**, but a few small improvements can be made.

### ⚠️ Unused Import

The code contains:

```python
from logging import exception
```

This import is not used anywhere in the program and can be removed.

---

### ⚠️ Broad Exception Handling

The program contains:

```python
except:
```

A bare `except` catches almost every type of exception.

It would be better to catch a specific exception when possible.

---

### ✏️ Output Typo

The current output contains:

```text
Relationship game_running:
```

This should ideally be:

```text
Relationship status:
```

This is only a display issue and does not affect the game logic.

---

## 🚀 Future Improvements

Possible improvements for future versions:

* 🧩 Split the game into separate functions
* 🧹 Improve naming and code organization
* 🛡️ Improve exception handling
* 🎨 Add a graphical interface
* 🌐 Create a web version
* 📊 Add result statistics
* 💾 Save previous game results
* 🎨 Add colored terminal output
* 🔁 Improve the restart system
* 🧪 Add automated tests

---

## 📚 What I Learned

This project was created to practice **Python fundamentals through a simple game**.

The main concepts practiced were:

> **String Manipulation + Lists + Loops + Conditions + Modulo + Basic Game Logic + Exception Handling**

The circular elimination part of the project was especially useful for understanding how the **modulo operator can be used with circular data structures**.

---

## 📌 Project Status

🟢 **Working**

The current version successfully implements the basic FLAMES game through the command line.

This project is mainly focused on practicing **Python fundamentals, string manipulation, list operations, loops, and basic algorithmic thinking**.

---

## 👨‍💻 Author

**Uzair Khan**

📧 **Email:** [khanuzair.f15@gmail.com](mailto:khanuzair.f15@gmail.com)

---

⭐ Feel free to explore the code, experiment with the FLAMES algorithm, and make your own improvements.

**Made with 🐍 Python & a little bit of relationship prediction 😂🔥**
