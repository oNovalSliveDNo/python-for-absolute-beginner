# 📝 Notes on Chapter 6 — Functions and Scope

In this chapter, I learned how to create my own functions, pass parameters, get values using `return`, use default values, and work with global variables.

---

## 📚 New Concepts

### 1. Creating Functions

A function is a block of code that performs a specific task. It is declared using the `def` keyword.

```python
def greet():
    print("Hello!")
````

Function call:

```python
greet()
```

---

### 2. Parameters and Arguments

Functions can accept values (arguments) passed through parameters:

```python
def greet(name):
    print("Hello,", name)

greet("Anna")
```

---

### 3. Return Values (`return`)

A function can return a result:

```python
def square(x):
    return x * x

print(square(4))  # 16
```

---

### 4. Default Values and Named Arguments

You can assign default values to parameters and specify argument names when calling a function:

```python
def birthday(name="Jack", age=1):
    print(f"Happy birthday, {name}! You are already {age} years old.")

birthday()
birthday("Anna", 5)
birthday(age=10, name="Sasha")
```

---

### 5. Global Variables

Global variables are declared outside of functions. To modify them inside a function, use the `global` keyword:

```python
value = 10

def change_value():
    global value
    value = 5
```

---

### 6. Simple User Interaction

Functions can include user input and validation:

```python
def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
```

---

📌 This chapter taught me how to break code into small functions, use parameters, return values, work with global variables, and build a simple architecture for projects.
