# 🐍 Python Lab

Welcome to **Python Lab** — a collection of Python projects, experiments, practice problems, and small applications built while learning and improving Python programming.

This repository contains everything from **simple games and logic-building exercises to audio/video processing and DSA-style problems**.

The main goal of this repository is not to build production-ready software, but to **learn by building, experimenting, debugging, and improving**.

---

## 🚧 Under Construction

This repository is a **learning repository**, so some projects are still being improved.

One currently known project with a major issue is:

### 🎯 Hangman / Word Guessing Game

The current version has a problem with its **guess counter and losing condition**.

The counter can reach `0` and continue into negative values because the losing condition currently checks:

```python
if count == 1:
```

instead of reliably stopping when the allowed attempts are exhausted.

The project is therefore marked as **Under Construction** until the attempt logic is corrected.

> Other projects may contain minor bugs, rough code, spelling mistakes, or beginner-level implementations. These are part of the learning process and are documented where relevant.

---

## 📚 What's Inside?

The repository currently contains projects covering several areas of Python.

| Category                 | Projects / Concepts                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------- |
| 🎮 Games                 | Rock Paper Scissors, 21 Number Game, Bulls and Cows, FLAMES, Higher Lower, Mastermind |
| 🧠 Logic Building        | Number Guessing, Min/Max Tracker, Word Guessing                                       |
| 🎯 DSA Practice          | Array and algorithm-based exercises                                                   |
| 🧰 Utilities             | Emoji Text Tool                                                                       |
| 🖥️ Computer Interaction | Screen Recorder                                                                       |
| 🎙️ Audio Processing     | Audio Recorder                                                                        |
| 📦 Python Libraries      | NumPy, OpenCV, PyAutoGUI, SciPy, Wavio, Demoji                                        |
| 🔄 Core Python           | Loops, conditions, functions, lists, strings, exceptions                              |

---

# 🎮 Games

## ✊✋✌️ Rock Paper Scissors

A classic Rock Paper Scissors game where the player competes against a randomly generated computer choice.

### Concepts practiced

* `if / elif / else`
* `while` loops
* Random numbers
* Input validation
* Exception handling
* Game logic
* Replay systems

---

## 🔢 21 Number Game

A game where the player and computer take turns writing consecutive numbers.

The objective is to avoid being the player who writes **21**.

### Concepts practiced

* Loops
* Functions
* Input validation
* Game state
* Conditional logic

---

## 🐂🐄 Bulls and Cows

A number guessing game based on the Bulls and Cows concept.

The player attempts to guess a randomly generated four-digit number.

* 🐂 **Bull** → Correct digit in the correct position
* 🐄 **Cow** → Correct digit in the wrong position

The project also includes a maximum number of attempts.

### Concepts practiced

* Random number generation
* Lists
* Strings
* Functions
* Validation
* Loops
* Game logic

---

## 🔥 FLAMES

A classic FLAMES relationship game implemented in Python.

The program takes two names, removes common characters, and uses the remaining character count to determine a relationship category.

Possible results include:

```text
Friends
Lovers
Affection
Marriage
Enemies
Siblings
```

### Concepts practiced

* Strings
* Lists
* Loops
* Character comparison
* List manipulation
* Circular elimination logic
* User input

---

## 📈 Higher Lower

A Higher Lower game inspired by the concept of comparing the follower counts of famous accounts.

The player has to determine which account has the higher follower count.

### Concepts practiced

* Dictionaries / structured data
* Random selection
* Functions
* Comparison logic
* Score tracking
* Terminal UI

---

## 🧠 Mastermind

A simple four-digit guessing game.

The program generates a random four-digit number and asks the player to guess it.

After every guess, the program reports how many digits are correct in the **correct position**.

### Concepts practiced

* Random numbers
* Lists
* Strings
* Loops
* Input validation
* Exception handling

---

# 🧩 Logic & Practice Problems

## 🔢 Number Guessing Game

A simple game where the computer generates a random number within a user-defined range.

The player gets **7 valid attempts** to find the correct number.

The program provides feedback:

```text
Too Low
Too High
Correct!
```

### Concepts practiced

* Random numbers
* User-defined ranges
* Loops
* Input validation
* Attempt counters
* Conditional statements

---

## 🐾 Pokémon Power Tracker

A small algorithmic exercise that tracks the **minimum and maximum Pokémon power** as Pokémon are processed one by one.

Example:

```text
Input:
3 8 9 7

Output:
3 3
3 8
3 9
3 9
```

The project demonstrates the concept of maintaining a **running minimum and maximum**.

### Complexity

```text
Time  → O(n)
Space → O(1)
```

---

# 🧰 Utility Projects

## 😀 Emoji Text Tool

A command-line utility for working with emojis using the `demoji` library.

The project can:

* 🔍 Find emojis inside text
* 📝 Convert emojis into descriptive text
* 🗑️ Remove emojis
* 🔄 Replace emojis with custom text

### Concepts practiced

* External libraries
* Strings
* Functions
* Menus
* Exception handling
* Text processing

---

# 🖥️ Computer Interaction

## 🎥 Screen Recorder

A basic screen recording program built using:

* `PyAutoGUI`
* `NumPy`
* `OpenCV`

The program repeatedly captures screenshots and combines them into a video.

### Pipeline

```text
🖥️ Screen
   ↓
📸 PyAutoGUI
   ↓
🔢 NumPy Array
   ↓
🎨 RGB → BGR
   ↓
🎥 OpenCV VideoWriter
   ↓
📁 Video File
```

### Features

* Screen capture
* 15 FPS recording
* 1920×1080 configured resolution
* MJPG codec
* Live preview
* `q` to stop recording

---

# 🎙️ Audio Processing

## 🎤 Audio Recorder

A simple audio recording project using:

* `sounddevice`
* `SciPy`
* `WAVIO`
* `NumPy`

The current version records:

```text
Sample Rate → 44.1 kHz
Duration    → 5 seconds
Channels    → Mono
Data Type   → int32
```

The recording is saved using both SciPy and WAVIO:

```text
recording-0.wav
recording-1.wav
```

### Pipeline

```text
🎙️ Microphone
      ↓
sounddevice
      ↓
NumPy Array
      ↓
 ┌────┴────┐
 ↓         ↓
SciPy     WAVIO
 ↓         ↓
WAV       WAV
```

---

# 🧠 DSA Practice

This repository also contains dedicated **Data Structures and Algorithms practice**.

The goal is to improve:

* Problem-solving
* Algorithmic thinking
* Time complexity analysis
* Array manipulation
* Searching
* Iteration
* Logical reasoning

DSA practice will continue to be added as new problems are solved.

---

# 🛠️ Technologies & Libraries

The repository uses a variety of Python technologies:

| Technology      | Used For                       |
| --------------- | ------------------------------ |
| 🐍 Python       | Core programming language      |
| 🎲 `random`     | Randomized games               |
| 🔢 NumPy        | Numerical and array processing |
| 👀 OpenCV       | Image/video processing         |
| 📸 PyAutoGUI    | Screen capture                 |
| 🎙️ SoundDevice | Audio recording                |
| 🧪 SciPy        | Audio file processing          |
| 🎚️ Wavio       | WAV file creation              |
| 😀 Demoji       | Emoji processing               |

---

# 🧠 Python Concepts Covered

As this repository grows, it covers an increasing number of Python concepts.

### Fundamentals

* Variables
* Data types
* Strings
* Lists
* Input/output
* Operators

### Control Flow

* `if`
* `elif`
* `else`
* `for`
* `while`
* `break`
* `continue`

### Functions

* Function creation
* Parameters
* Return values
* Reusable logic

### Error Handling

* `try`
* `except`
* `ValueError`
* `KeyboardInterrupt`

### Data & Algorithms

* Lists
* Searching
* Comparisons
* Running minimum/maximum
* Randomization
* Basic complexity analysis

### External Libraries

Learning how to:

```text
Install → Import → Use → Experiment → Debug
```

with third-party Python packages.

---

# 📂 Repository Structure

The repository is organized around individual projects and exercises.

A simplified structure looks like:

```text
Python-Lab/
│
├── 21-Number-Game/
│
├── Bulls-and-Cows/
│
├── FLAMES/
│
├── Higher-Lower/
│
├── Mastermind/
│
├── Number-Guessing-Game/
│
├── Pokémon-Power-Tracker/
│
├── Rock-Paper-Scissors/
│
├── Screen-Recorder/
│
├── Audio-Recorder/
│
├── Emoji-Text-Tool/
│
├── DSA/
│
└── README.md
```

> The exact folder names may change as the repository evolves.

---

# 🚀 How to Use This Repository

## 1. Clone the Repository

```bash
git clone <repository-url>
```

## 2. Enter the Repository

```bash
cd Python-Lab
```

## 3. Choose a Project

For example:

```bash
cd Rock-Paper-Scissors
```

## 4. Install Required Dependencies

Projects using only Python's standard library generally require no additional installation.

Projects using external libraries may require:

```bash
pip install <package-name>
```

For example:

```bash
pip install numpy opencv-python pyautogui
```

or:

```bash
pip install sounddevice scipy wavio
```

## 5. Run the Project

```bash
python main.py
```

The exact entry file may vary between projects.

---

# 📊 Project Status

| Project                    | Status                |
| -------------------------- | --------------------- |
| ✊ Rock Paper Scissors      | 🟢 Completed          |
| 🔢 21 Number Game          | 🟢 Completed          |
| 🐂 Bulls and Cows          | 🟢 Completed          |
| 🔥 FLAMES                  | 🟢 Completed          |
| 📈 Higher Lower            | 🟢 Completed          |
| 🧠 Mastermind              | 🟢 Completed          |
| 🔢 Number Guessing Game    | 🟢 Completed          |
| 🐾 Pokémon Power Tracker   | 🟢 Completed          |
| 😀 Emoji Text Tool         | 🟢 Completed          |
| 🎥 Screen Recorder         | 🟢 Completed          |
| 🎙️ Audio Recorder         | 🟢 Completed          |
| 🎯 Hangman / Word Guessing | 🟠 Under Construction |
| 🧠 DSA Practice            | 🔄 Ongoing            |

---

# 📈 Learning Progress

This repository represents my journey from writing small Python programs to working with external libraries and more complex logic.

The progression roughly looks like:

```text
🐍 Python Basics
      ↓
🔀 Conditions & Loops
      ↓
🎮 Small Games
      ↓
🧩 Functions & Modular Logic
      ↓
🧠 Problem Solving
      ↓
📚 DSA Practice
      ↓
📦 External Libraries
      ↓
🎥 Image / Video Processing
      ↓
🎙️ Audio Processing
      ↓
🚀 Larger Projects
```

The repository will continue evolving as new concepts are learned.

---

# 🎯 Goals

The main goals of this repository are:

* 🐍 Improve Python fundamentals
* 🧠 Develop problem-solving skills
* 🧩 Practice algorithmic thinking
* 📚 Learn DSA
* 📦 Experiment with Python libraries
* 🛠️ Build small practical projects
* 🐛 Learn debugging by fixing my own mistakes
* 🚀 Gradually move toward larger applications

---

# 🚀 Future Plans

More projects will be added as I continue learning.

Possible future additions include:

* 🧠 More DSA problems
* 🎮 More Python games
* 🖥️ GUI applications
* 🌐 Flask projects
* 🗄️ Database-based applications
* 🤖 AI/ML experiments
* 🔌 API-based projects
* ⚙️ Automation scripts
* 📊 Data-processing projects
* 🚀 Larger Python applications

---

# 🤝 Learning Philosophy

This repository is built around a simple idea:

> **Learn → Build → Break → Debug → Improve → Repeat**

Not every project is perfect, and that's intentional.

Some programs contain beginner-level implementations, inefficient approaches, or small mistakes. Those mistakes are part of the learning process.

The goal is to understand **why something works**, **why something breaks**, and **how it can be improved**.

---

# 📌 Repository Status

🟢 **Active & Continuously Updated**

This is an evolving Python learning repository.

New projects, experiments, DSA problems, and improvements will be added over time.

---

# 👨‍💻 Author

**Uzair Khan**

GitHub: `khanuzair-f15`

Email: `khanuzair.f15@gmail.com`

---

⭐ If you're interested in my Python learning journey, feel free to explore the individual projects and follow the repository as it grows.
