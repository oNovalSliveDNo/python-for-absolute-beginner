# 📝 Notes for Chapter 3 — Conditionals and Loops

In this chapter, I learned the basics of flow control in programs: conditional statements (`if`, `elif`, `else`), loops (`while`), logical operations, and control instructions `break` and `continue`.

## 📚 New Concepts

### 1. `if`, `elif`, `else`
Allow executing different code blocks based on conditions:

```python
if condition:
    # code runs if condition is true
elif another_condition:
    # alternative if the first condition is false
else:
    # runs if none of the above conditions are true
````

---

### 2. Comparison operators

Used to create logical conditions:

* `==` — equals
* `!=` — not equals
* `>` — greater than
* `<` — less than
* `>=` — greater than or equal to
* `<=` — less than or equal to

```python
if score >= 90:
    print("Excellent!")
```

---

### 3. Logical operators: `and`, `or`, `not`

Combine conditions:

```python
if username == "admin" and password == "1234":
    print("Access granted")
```

---

### 4. `while` loop

Repeats a block of code while the condition is true:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

### 5. `break` and `continue`

Control the loop execution:

* `break` — immediately exits the loop
* `continue` — skips the current iteration and moves to the next one

```python
while True:
    if some_condition:
        break
    if skip_condition:
        continue
```

---

### 6. Truthy and falsy values

In conditionals, Python interprets certain values as `True` or `False`. For example:

* `0`, `""`, `None`, `[]`, `{}` → `False`
* Everything else → `True`

```python
tip = int(input("How much tip will you leave? "))
if tip:
    print("Let's find a table.")
```

---

### 7. Generating random numbers with `random.randint()` and `random.randrange()`

Allows generating pseudo-random numbers:

* `random.randint(a, b)` — returns a random **integer** from `a` to `b`, inclusive
* `random.randrange(n)` — returns a random **integer** from `0` to `n-1`. You can also specify a start and step: `random.randrange(start, stop, step)`

```python
import random
number = random.randint(1, 6)    # from 1 to 6 inclusive
number = random.randrange(6) + 1 # from 0 to 5, add 1 → from 1 to 6
```

---

### 8. Handling user input

To input numbers:

```python
guess = int(input("Enter a number: "))
```

---

📌 This chapter taught me how to control the program's logic using conditions and loops. I learned how to write interactive scripts that respond to user input, handle errors, and model behavior. This is the foundation for creating more complex games and systems.
