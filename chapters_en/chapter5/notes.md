# 📝 Notes on Chapter 5 — Lists, Nested Structures, and Dictionaries

In this chapter, I learned how to work with lists, nested sequences, and dictionaries. I practiced adding and removing elements from lists, sorting them, storing pairs of values (name and score), and creating dictionaries with the ability to add, modify, and remove elements.

## 📚 New Concepts

### 1. Lists (`list`)

A list is a mutable collection of objects:

```python
inventory = ["sword", "chainmail", "shield", "healing potion"]

for item in inventory:
    print(item)
````

---

### 2. List Methods

These methods allow you to manage elements in a list:

```python
scores = []

# Add
scores.append(100)

# Remove by value
scores.remove(100)

# Sort (in descending order)
scores.sort(reverse=True)
```

---

### 3. User Menu Handling

Example of interaction via a menu with loops and lists:

```python
choice = None
while choice != '0':
    print("1 - Show", "2 - Add", sep="\n")
    choice = input("Your choice: ")
```

---

### 4. Nested Sequences (List of Tuples)

Storing multiple pieces of data in one element:

```python
scores = [(300, "Anya"), (250, "Boris")]

for entry in scores:
    score, name = entry
    print(name, score)
```

Sorting by score:

```python
scores.sort(reverse=True)
scores = scores[:5]  # keep the top-5
```

---

### 5. Dictionaries (`dict`)

Dictionaries store key-value pairs and allow quick access to data:

```python
geek = {"404": "error", "Googling": "searching on the internet"}

# Get value
print(geek["404"])

# Add
geek["LOL"] = "laughing out loud"

# Update
geek["404"] = "not found"

# Delete
del geek["LOL"]
```

Checking if a key exists:

```python
if "404" in geek:
    print("Definition exists")
```

---

📌 This chapter taught me how to use lists and their methods, work with nested data structures, and utilize dictionaries for storing and processing information.
