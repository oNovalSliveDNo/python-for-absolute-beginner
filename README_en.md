# 🐍 Python Programming for the Absolute Beginner — Practical Examples

This repository is the result of my learning based on the book **"Python Programming for the Absolute Beginner"** by Michael Dawson. It contains programs, exercises, and my notes for each chapter. The project was created primarily to demonstrate my progress in learning Python.

## 📚 About the Book

Michael Dawson — *Python Programming for the Absolute Beginner*  
Edition: 3rd Edition  
Focus: teaching programming from scratch in Python through the development of games and interactive programs.  
> ⚠️ Note: the code in the book was written using Python 3.1.1.  
> Some syntax and features may differ from those in newer versions of Python 3.x.

## 🎯 Purpose of This Repository

- 📌 Demonstrate basic Python skills  
- ✍️ Provide clean, well-commented code  
- 🧠 Capture key concepts from each chapter  
- 📂 Organize examples by chapter for easy navigation  

## 📚 Topics Covered in the Book

The book covers fundamental concepts of Python programming with an emphasis on hands-on practice through building simple, illustrative games and programs. Each chapter includes example programs. Below are the main topics:

### 📘 Chapter 1. Getting Started

- Introduction to Python and its features  
- Installing Python and using IDLE  
- Comments, text output, and waiting for user input  
- First program: *Game Over*

### 📘 Chapter 2. Types, Variables, and Input/Output

- Strings, quotation marks, and escape sequences  
- String concatenation and repetition  
- Numeric types and operators  
- Variables, user input, string methods  
- Type casting and compound assignment operators  
- Program: *Useless Facts*

### 📘 Chapter 3. Branching, Loops, and Pseudocode

- Conditional statements: `if`, `else`, `elif`  
- `while` loops, infinite loops, `break` and `continue`  
- Logical operators: `not`, `and`, `or`  
- Step-by-step program design and pseudocode  
- Game: *Guess the Number*

### 📘 Chapter 4. `for` Loops, Strings, and Tuples

- `for` loops, including stepped and reverse iteration  
- String operations: indexing, slicing, methods  
- Tuples: creation, iteration, immutability  
- Game: *Anagrams*

### 📘 Chapter 5. Lists and Dictionaries

- Creating, modifying, and using list methods  
- Nested lists and tuples  
- Shared references  
- Dictionaries: creation and key-value manipulation  
- Game: *Hangman*

### 📘 Chapter 6. Functions

- Defining functions, parameters, return values  
- Abstraction, encapsulation, and code reuse  
- Named arguments and default parameter values  
- Scope, global variables, and constants  
- Game: *Tic-Tac-Toe*

### 📘 Chapter 7. Working with Files and Exceptions

- Reading and writing text files  
- Serialization and deserialization (`pickle`, `shelve` modules)  
- Exception handling with `try/except`  
- Game: *Quiz*

### 📘 Chapter 8. Introduction to OOP

- Fundamentals of object-oriented programming  
- Declaring classes and methods, creating objects  
- Constructors and object attributes  
- Class attributes and static methods  
- Encapsulation and data hiding  
- Properties and attribute access control  
- Game: *My Pet*

### 📘 Chapter 9. Object-Oriented Programming (Continued)

- Object interaction and message passing  
- Combining objects and working with collections  
- Inheritance and class extension  
- Method overriding and polymorphism  
- Organizing code with modules  
- Game: *Blackjack*

### 📘 Chapter 10. Graphical Interfaces

- Introduction to event-driven programming  
- Basics of tkinter: windows, labels, buttons  
- Building GUI applications with classes  
- Event handling and widget interaction  
- Advanced widgets: text fields, checkboxes, radio buttons  
- Game: *Crazy Storyteller*

### 📘 Chapter 11. Graphics

- Overview of `pygame` and `livewires` libraries  
- Working with the graphics window, background, coordinate systems  
- Sprites, text, and messages on screen  
- Movement, mouse control, and collision detection  
- Building the final game: classes, logic, and main loop  
- Game: *Panic in the Pizzeria*

### 📘 Chapter 12. Sound, Animation, and Large Projects

- Keyboard input, rotation, and sprite animation  
- Adding sound and background music  
- Creating object classes and the game world  
- Implementing shooting, collisions, and visual effects  
- Building levels, scoring systems, and final logic  
- Game: *Aborted Flight*

## 🚀 Getting Started

To run the programs from this repository, follow these simple steps:

### 0. Important Notes:

- The code was written for Python 3.1.1, so incompatibilities with newer versions may occur. Some examples may not work correctly due to deprecated syntax or functions. Using Python 3.1.1 is recommended for best compatibility.
- Some syntax and features may have changed in newer Python versions, so be sure to follow the instructions for installing Python 3.1.1.

### 1. Install Python 3.1.1

If you don’t already have Python 3.1.1 installed, download it from the official website:

* [Python 3.1.1](https://www.python.org/downloads/release/python-311/)

Check your current Python version with:

```bash
python --version
```

If the Python version does not match, install Python 3.1.1 or configure the virtual environment with the required version.

### 2. Download or clone the repository

To get all the repository files to your computer, use one of the following commands:

**If you use Git:**

```bash
git clone https://github.com/oNovalSliveDNo/python-for-absolute-beginner.git
```

**Or download the archive:**

Follow the link on GitHub and download the ZIP archive with the repository.

### 3. Project Navigation

Each chapter of the book is arranged in a separate folder inside the `chapters/` directory. Each folder contains:

* `.py` files are code examples from the chapter.
* `README.md ` is a description of the contents of the chapter.
* `notes.md ` — my personal notes and explanations.

### 4. Running the example

To run the example, open a terminal, navigate to the desired folder, and run the command:

```bash
python <file_name>.py
```

For example, to run the program from chapter 1:

```bash
cd chapters/chapter1
python game_over.py
```

### 5. Using a virtual environment (optional)

It is recommended to use a virtual environment to isolate project dependencies. If you are using Python 3.1.1, follow these steps:

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

3. Make sure that the Python version you are using is correct (3.1.1).

### 6. Launch using the IDE

If you are using an IDE (for example, PyCharm or VSCode), simply open the project in the IDE and run the required `.py` file.
