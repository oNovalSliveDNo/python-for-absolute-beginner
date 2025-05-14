# 📝 Notes on Chapter 7 — File Handling and Error Handling

In this chapter, I learned how to read and write files, serialize data using `pickle` and `shelve`, and handle exceptions.

---

## 📚 New Concepts

### 1. Reading from a file (`open`, `read`, `readline`, `readlines`)

Opening and reading files:

```python
# Opening a file
file = open("example.txt", "r")

# Reading one character
print(file.read(1))

# Reading a line
print(file.readline())

# Reading all lines into a list
lines = file.readlines()

# Iterating through lines
for line in lines:
    print(line)

# Closing the file
file.close()
````

---

### 2. Writing to a file (`write`, `writelines`)

Creating and writing to a file:

```python
# Writing line by line
file = open("write_example.txt", "w")
file.write("First line\n")
file.write("Second line\n")
file.close()

# Writing a list of lines
lines = ["Line 1\n", "Line 2\n"]
file = open("write_example.txt", "w")
file.writelines(lines)
file.close()
```

---

### 3. Serialization: `pickle` and `shelve`

Saving (pickling) objects:

```python
import pickle

# Saving objects
data = ["apple", "banana", "cherry"]
with open("data.dat", "wb") as f:
    pickle.dump(data, f)

# Loading objects
with open("data.dat", "rb") as f:
    data_loaded = pickle.load(f)
    print(data_loaded)
```

Using `shelve` (key-value, like a dictionary):

```python
import shelve

shelf = shelve.open("mydata")
shelf["fruits"] = ["apple", "pear", "plum"]
print(shelf["fruits"])
shelf.close()
```

---

### 4. Exception Handling (`try`, `except`, `else`)

Basics of error handling:

```python
try:
    num = float(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
```

Handling multiple exception types:

```python
for value in (None, "Hello"):
    try:
        print(float(value))
    except (TypeError, ValueError):
        print("Cannot convert value.")
```

Getting the exception argument:

```python
try:
    num = float(input("Enter a number: "))
except ValueError as e:
    print("Error:", e)
```

Using the `else` block when no exception occurs:

```python
try:
    num = float(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
else:
    print("You entered:", num)
```

---

📌 This chapter taught me how to work with files, serialize data, and handle errors.
