# 🐍 Python Programming for the Absolute Beginner — Practical Examples



## 📂 Table of Contents
- [📖 Description](#-description)
- [📚 About the Book](#-about-the-book)
- [🎯 Repository Goals](#-repository-goals)
- [💾 Installation](#-installation)
  - [1. Install Python 3.13.3](#1-install-python-3133)
  - [2. Download or Clone the Repository](#2-download-or-clone-the-repository)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Use a Virtual Environment (Optional)](#4-use-a-virtual-environment-optional)
- [📂 Project Structure](#-project-structure)
- [🚀 Running an Example](#-running-an-example)
  - [1. Running via Terminal](#1-running-via-terminal)
  - [2. Running via IDE](#2-running-via-ide)
- [📚 Topics Covered in the Book](#-topics-covered-in-the-book)
  - [📘 Chapter 1: Getting Started](#-chapter-1-getting-started)
  - [📘 Chapter 2: Types, Variables, and Input/Output](#-chapter-2-types-variables-and-inputoutput)
  - [📘 Chapter 3: Conditionals, Loops, and Pseudocode](#-chapter-3-conditionals-loops-and-pseudocode)
  - [📘 Chapter 4: for Loops, Strings, and Tuples](#-chapter-4-for-loops-strings-and-tuples)
  - [📘 Chapter 5: Lists and Dictionaries](#-chapter-5-lists-and-dictionaries)
  - [📘 Chapter 6: Functions](#-chapter-6-functions)
  - [📘 Chapter 7: Working with Files and Exceptions](#-chapter-7-working-with-files-and-exceptions)
  - [📘 Chapter 8: Introduction to OOP](#-chapter-8-introduction-to-oop)
  - [📘 Chapter 9: OOP](#-chapter-9-oop)
  - [📘 Chapter 10: Graphical Interfaces](#-chapter-10-graphical-interfaces)
  - [📘 Chapter 11: Graphics](#-chapter-11-graphics)
  - [📘 Chapter 12: Sound, Animation, and Large Projects](#-chapter-12-sound-animation-and-large-projects)
- [🔔 Note](#-note)
- [✅ Testing](#-testing)
- [📚 Useful Resources](#-useful-resources)
- [📝 License](#-license)



---



## 📖 Description

This repository is a result of my learning journey through the book **"Python Programming for the Absolute Beginner"** by Michael Dawson.  
It contains programs, exercises, and personal notes for each chapter of the book.

> This project primarily serves as a demonstration of my progress in learning the Python programming language.



## 📚 About the Book

Michael Dawson — *Python Programming for the Absolute Beginner*  
Edition: 3rd Edition  
Focus: Learning programming from scratch using Python by creating games and interactive programs.

> ⚠️ Important: The original code in the book was written for Python 3.1.1.  
> However, all the code in this repository has been tested and works successfully on **Python 3.13.3**.



## 🎯 Repository Goals

- 📌 Demonstrate basic Python skills.
- ✍️ Provide clean, well-commented code.
- 🧠 Capture key concepts from each chapter.
- 📂 Organize examples by chapter for easy navigation.



## 💾 Installation

To run the programs from this repository, follow these steps.

### 1. Install Python 3.13.3

All examples in this repository have been tested with **Python 3.13.3**.  
If you do not have this version installed yet, download it from the official website:

* [Python 3.13.3](https://www.python.org/downloads/release/python-3133/)

Check your Python version using the command:

```bash
python --version
````

If your version differs, it is recommended to use Python 3.13.3 for full compatibility.

### 2. Download or clone the repository

**Using Git:**

```bash
git clone https://github.com/oNovalSliveDNo/python-for-absolute-beginner.git
```

**Or download the archive:**

Go to the repository page and download the ZIP archive.

### 3. Install dependencies

Most examples from the book use Python's standard libraries (`random`, `math`, `pickle`, `shelve`, `sys`, `tkinter`) and do not require additional installations.

However, for chapters 11 and 12, which involve graphics and sound, you need to install the following third-party libraries:

```bash
pip install pygame superwires
```

* `pygame` — a library for creating games and multimedia applications.
* `superwires` — a modern fork of the outdated `livewires` library, adapted for Python 3.13.3 and `pygame`.

To simplify the installation of dependencies, you can use the `requirements.txt` file.
Run the following command to install everything from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This file contains all the necessary libraries required for the project.

### 4. Use a virtual environment (optional)

It is recommended to use a virtual environment to isolate project dependencies:

1. Create a virtual environment:

```bash
python -m venv env
```

2. Activate the environment:

* On Windows:

```bash
.\env\Scripts\activate
```

* On macOS/Linux:

```bash
source env/bin/activate
```

3. Verify that Python 3.13.3 is being used:

```bash
python --version
```



## 📂 Project Structure
```markdown
python-for-absolute-beginner
├── chapters_en/                   # Examples, notes, and descriptions in English
│   ├── chapter1/                  
│   │   ├── README.md              # Chapter 1 description
│   │   ├── game_over.py           # Program: Game Over
│   │   └── notes.md               # Personal notes for chapter 1
│   │
│   ├── chapter2/                  
│   │   └── ...                    
│   │
│   ├── ...                        
│   │
│   ├── chapter12/                 
│   │   └── ...
│   │
│   └── README.md                  # Overview of all chapters in English
│
├── chapters_ru/                   # (Optional) Materials in Russian
│   └── ...                        
│
├── .gitignore                     # Git ignore file
├── LICENSE                        # Project license (MIT)
├── README.md                      # Main README in English
├── README_ru.md                   # Full README in Russian
└── requirements.txt               # List of dependencies for installation via pip
```



## 🚀 Running an Example

### 1. Running via Terminal

Open the terminal, navigate to the appropriate folder, and run the command:

```bash
python <filename>.py
```

For example:

```bash
cd chapters_en/chapter1
python game_over.py
```

### 2. Running via IDE

If you are using an IDE (such as PyCharm or VSCode), open the project and run the `.py` files directly.



## 📚 Topics Covered in the Book

The book covers fundamental Python programming concepts with a focus on hands-on practice through creating simple yet illustrative games and programs. Each section includes example programs. Below are the key topics:

### 📘 Chapter 1: Getting Started

* Introduction to Python and its features
* Installing Python and working in IDLE
* Comments, text output, and waiting for user input
* First program: *Game Over*

### 📘 Chapter 2: Types, Variables, and Input/Output

* Strings and quotes, escape sequences
* String concatenation and repetition
* Numeric types and operators
* Variables, user input, string methods
* Type conversion and compound assignment operators
* Program: *Useless Facts*

### 📘 Chapter 3: Conditionals, Loops, and Pseudocode

* Conditional statements: `if`, `else`, `elif`
* `while` loops, infinite loops, `break` and `continue` commands
* Logical operators: `not`, `and`, `or`
* Step-by-step program development and pseudocode
* Game: *Guess the Number*

### 📘 Chapter 4: `for` Loops, Strings, and Tuples

* `for` loops, counting with steps and in reverse order
* Working with strings: indexing, slicing, methods
* Tuples: creation, iteration, immutability properties
* Game: *Anagrams*

### 📘 Chapter 5: Lists and Dictionaries

* Creating, modifying, and list methods
* Nested lists and tuples
* Distributed references
* Dictionaries: creating and working with key-value pairs
* Game: *Hangman*

### 📘 Chapter 6: Functions

* Defining functions, parameters, return values
* Abstraction, encapsulation, code reuse
* Named arguments, default parameters
* Scopes, global variables, and constants
* Game: *Tic-Tac-Toe*

### 📘 Chapter 7: Working with Files and Exceptions

* Reading and writing text files
* Serialization and deserialization (using `pickle` and `shelve` modules)
* Exception handling with `try/except`
* Game: *Quiz*

### 📘 Chapter 8: Introduction to OOP

* Basics of Object-Oriented Programming (OOP)
* Declaring classes, methods, and creating objects
* Constructors and object attributes
* Class attributes and static methods
* Encapsulation and data hiding
* Properties and access control for attributes
* Game: *My Pet*

### 📘 Chapter 9: OOP

* Object interaction and message passing
* Combining objects and working with collections
* Inheritance and extending classes
* Method overriding and polymorphism
* Structuring code with modules
* Game: *Blackjack*

### 📘 Chapter 10: Graphical Interfaces

* Introduction to event-driven programming
* Basics of working with tkinter: windows, labels, buttons
* Creating a GUI using classes
* Handling events and interacting with elements
* Advanced interface elements: text fields, checkboxes, radio buttons
* Game: *The Crazy Storyteller*

### 📘 Chapter 11: Graphics

* Introduction to `pygame` and `livewires` libraries
* Working with a graphical window, background, and coordinate system
* Sprites, text, and messages on the screen
* Movement control, mouse, and collision detection
* Building the final game: classes, logic, and main loop
* Game: *Panic at the Pizzeria*

### 📘 Chapter 12: Sound, Animation, and Large Projects

* Working with the keyboard, sprite rotation, and animation
* Adding sound effects and background music
* Creating object classes and the game world
* Implementing shooting, collisions, and visual effects
* Level creation, scoring system, and final logic
* Game: *Interrupted Flight*



## 🔔 Note

Some syntax features from the book may differ from the current Python 3.13.3.
All the code provided in the repository has been adapted and tested for compatibility with this version of Python.

* The deprecated library `livewires` is replaced with its modern fork, `superwires`, which is compatible with Python 3.13.3.



## ✅ Testing

The repository’s code does not contain automated tests, but all examples have been manually checked and work on Python 3.13.3.



## 📚 Useful Resources

* [Official Python Documentation](https://docs.python.org/3/)
* [Pygame Documentation](https://www.pygame.org/docs/)
* [Superwires Documentation](https://superwires.readthedocs.io/)



## 📝 License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.
