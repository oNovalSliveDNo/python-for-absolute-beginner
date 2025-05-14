# 📝 Notes for Chapter 2 — Types, Variables, and Input/Output

In Chapter 2, I learned the basics of working with strings, variables, user input, arithmetic, and type conversion. Below are the key concepts I studied while working through the chapter's programs.

## 📚 New Concepts

### 1. `end=` in `print()`
Allows control over the line ending character (default is `\n`).  
Example:
```python
print("Hello", end=" ")
print("World")
````

---

### 2. Multiline strings `"""..."""`

Used to display/store multi-line text.
Also useful for displaying ASCII art.

---

### 3. **Escape sequences** (`\t`, `\n`, `\\`, `\'`, `\"`, `\a`)

Used to insert special characters into strings.
Examples:

```python
print("Hello\tWorld")  # tab
print("Line1\nLine2")  # newline
print("She said: \"Hi!\"")  # quotes
print("\a")  # alert sound
```

---

### 4. String operations: `+` (concatenation), `*` (repetition)

```python
print("Hi" + " there")  # concatenation
print("Repeat!" * 3)    # repetition
```

---

### 5. **Arithmetic operators**

`+`, `-`, `*`, `/`, `//` (integer division), `%` (modulus)
Examples:

```python
print(7 / 2)   # 3.5
print(7 // 2)  # 3
print(7 % 2)   # 1
```

---

### 6. **Variables**

Allow you to store and use data.

```python
name = "Alex"
age = 20
```

---

### 7. `input()` and type conversion: `int()`, `float()`

`input()` returns a string, so conversion is often needed:

```python
age = int(input("Enter age: "))
```

---

### 8. String methods: `.upper()`, `.lower()`, `.title()`, `.replace()`

Used to transform strings:

```python
s = "hello"
print(s.upper())           # HELLO
print(s.replace("h", "H")) # Hello
```

---

### 9. **Logical errors**

For example, trying to add strings as if they were numbers:

```python
# Error:
total = "100" + "200"  # '100200', not 300
```

Fixed by converting to numbers: `int("100") + int("200")`

---

📌 This chapter helped me learn how to work with strings, variables, user input, and arithmetic. I also learned how to avoid common mistakes, such as adding strings instead of numbers.
