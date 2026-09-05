# 🐾 Pokémon Power Tracker

A simple Python program that tracks the **minimum and maximum power level** of Pokémon caught by a trainer.

After each Pokémon is caught, the program updates and displays the lowest and highest power levels among all Pokémon caught so far.

---

## 📌 Introduction

Imagine a Pokémon trainer catching Pokémon one by one, with each Pokémon having a positive integer representing its power.

The goal is to keep track of the team's:

* 📉 **Minimum Power** — weakest Pokémon caught so far
* 📈 **Maximum Power** — strongest Pokémon caught so far

Instead of repeatedly calculating the minimum and maximum from the entire list, the program maintains the current values and updates them as each new Pokémon is processed.

---

## 🎯 Example

Given the Pokémon powers:

```text
3 8 9 7
```

The output is:

```text
3 3
3 8
3 9
3 9
```

### Step-by-step

| Pokémon Caught | Minimum | Maximum |
| -------------- | ------: | ------: |
| 3              |       3 |       3 |
| 8              |       3 |       8 |
| 9              |       3 |       9 |
| 7              |       3 |       9 |

### Explanation

**After catching Pokémon with power `3`:**

```text
min = 3
max = 3
```

**After catching Pokémon with power `8`:**

```text
min = 3
max = 8
```

**After catching Pokémon with power `9`:**

```text
min = 3
max = 9
```

**After catching Pokémon with power `7`:**

```text
min = 3
max = 9
```

The Pokémon with power `7` doesn't change either value because `3` is still the minimum and `9` is still the maximum.

---

## ⚙️ How It Works

The program first initializes both `mini` and `maxi` with the power of the first Pokémon:

```python
mini = maxi = power[0]
```

This means:

```text
minimum = first Pokémon's power
maximum = first Pokémon's power
```

The first result is then displayed:

```python
print(mini, maxi)
```

After that, the program processes every remaining Pokémon:

```python
for power in power[1:]:
```

For each Pokémon:

```python
mini = min(mini, power)
maxi = max(maxi, power)
```

The current minimum and maximum are updated using Python's built-in `min()` and `max()` functions.

Finally:

```python
print(mini, maxi)
```

displays the updated values.

---

## 🔄 Program Flow

```text
        Start
          │
          ▼
   Pokémon power list
          │
          ▼
Initialize min & max
 using first element
          │
          ▼
   Display min & max
          │
          ▼
 Process remaining powers
          │
          ▼
   ┌─────────────────┐
   │ Is current power│
   │ smaller than min│
   │      or larger? │
   └────────┬────────┘
            │
       Update values
            │
            ▼
    Display min & max
            │
            ▼
   More Pokémon?
      │         │
     Yes        No
      │          │
      └──────────┘
            │
            ▼
           End
```

---

## 🧠 Core Logic

The important idea is that we **don't need to search the whole collection every time**.

For every new power:

```python
mini = min(mini, current_power)
maxi = max(maxi, current_power)
```

Conceptually:

```text
New power < current minimum
        ↓
Update minimum
```

and

```text
New power > current maximum
        ↓
Update maximum
```

Otherwise, the existing values remain unchanged.

---

## 🛠️ Tech Stack

| Technology | Usage                          |
| ---------- | ------------------------------ |
| 🐍 Python  | Main programming language      |
| `min()`    | Finds the smaller value        |
| `max()`    | Finds the larger value         |
| Lists      | Stores Pokémon power levels    |
| `for` loop | Processes Pokémon sequentially |

---

## 📚 Python Concepts Practiced

This project demonstrates several fundamental Python concepts:

* 📋 Lists
* 🔁 `for` loops
* 🔢 Integer values
* 🔀 List slicing
* 🧮 Built-in `min()` function
* 🧮 Built-in `max()` function
* 📦 Multiple assignment
* 🖨️ Console output
* 📈 Running minimum and maximum

---

## 💻 Code

```python
power = [3, 8, 9, 7]

mini = maxi = power[0]
print(mini, maxi)

for power in power[1:]:
    mini = min(mini, power)
    maxi = max(maxi, power)
    print(mini, maxi)
```

---

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed:

```bash
python --version
```

### 2. Clone the repository

```bash
git clone <repository-url>
```

### 3. Navigate into the project

```bash
cd <project-folder>
```

### 4. Run the program

```bash
python main.py
```

---

## 📤 Sample Output

For:

```python
power = [3, 8, 9, 7]
```

the program produces:

```text
3 3
3 8
3 9
3 9
```

---

## ⏱️ Time & Space Complexity

Let `n` be the number of Pokémon caught.

### Time Complexity

```text
O(n)
```

Each Pokémon is processed once.

### Space Complexity

```text
O(1)
```

Apart from the input list, only a few variables are used to maintain the current minimum and maximum.

---

## ⚠️ Current Limitations

This is intentionally a simple implementation.

* The Pokémon powers are currently **hardcoded**:

  ```python
  power = [3, 8, 9, 7]
  ```
* There is no user input.
* The program assumes the list contains at least one element.
* The variable name `power` is reused as both the list and the loop variable. This works, but using a name such as `current_power` would improve readability.

---

## 🚀 Possible Improvements

Future versions could:

* 🎮 Allow users to enter Pokémon powers.
* 🐾 Simulate catching Pokémon one at a time.
* 📊 Display the strongest and weakest Pokémon.
* 🔢 Support an unlimited number of Pokémon.
* 🧪 Handle empty input safely.
* 📈 Display the change in minimum/maximum after every catch.
* 🖥️ Build a small interactive Pokémon-themed interface.

---

## 🎓 What I Learned

This small problem demonstrates an important programming technique:

> **Maintain the information you need while processing data instead of recalculating everything from scratch.**

The same running minimum/maximum concept is useful in many algorithms and data-processing problems.

---

## 📌 Project Status

🟢 **Completed**

The current implementation successfully tracks and displays the minimum and maximum Pokémon power after every catch.

---

## 👨‍💻 Author

**Uzair Khan**

GitHub: `khanuzair-f15`

Email: `khanuzair.f15@gmail.com`

---

⭐ If you found this project useful, consider giving the repository a star!
