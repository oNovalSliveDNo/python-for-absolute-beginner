# 📝 Notes on Chapter 4 — Working with Strings, `for` Loops, and Tuples

In this chapter, I got familiar with `for` loops, the `range()` function, working with strings, slicing, tuples, and new ways to process text. Practically, I learned how to iterate over string characters, filter and modify them, use immutable collections, and manage indexes.

## 📚 New Concepts

### 1. `for` Loop with a String

Allows iterating over each character of the string:

```python
word = "Example"
for letter in word:
    print(letter)
````

---

### 2. The `range()` Function

Creates a sequence of numbers for use in loops:

```python
for i in range(5):           # from 0 to 4
    print(i)

for i in range(0, 10, 2):    # from 0 to 8 with step 2
    print(i)

for i in range(10, 0, -1):   # from 10 to 1 with step -1
    print(i)
```

---

### 3. The `len()` Function and the `in` Operator

* `len()` returns the length of a string or collection.
* `in` checks for the presence of an element in a string, list, or tuple.

```python
message = "Hello"
print(len(message))  # 5

if "e" in message:
    print("Letter 'e' found")
```

---

### 4. Indexing and Negative Indexes

Allows accessing characters of a string by their position:

```python
word = "index"
print(word[0])   # 'i'
print(word[-1])  # 'x'
```

---

### 5. String Slicing

Extracts part of a string by a range of indices:

```python
word = "pizza"
print(word[1:4])   # 'izz'
```

---

### 6. Creating a New String via Filtering

You can create a new string by selecting specific characters:

```python
message = "example"
new_message = ""
VOWELS = "aeiou"

for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
```

---

### 7. Tuples (`tuple`)

An immutable sequence of elements:

```python
inventory = ("sword", "shield", "potion")

# Iterating over elements
for item in inventory:
    print(item)

# Checking presence
if "sword" in inventory:
    print("Armed!")

# Indexing and slicing
print(inventory[1])          # 'shield'
print(inventory[0:2])        # ('sword', 'shield')

# Concatenating tuples
chest = ("gold", "jewels")
inventory += chest
```

---

### 8. Modifying Strings — Anagram

An example of randomly shuffling characters of a string:

```python
import random
word = "python"
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[position+1:]
```

---

📌 This chapter taught me how to work with strings and tuples, use the `for` loop to iterate over characters and elements, apply `range()` to generate sequences, and work with indexes and slices. Now I know how to filter text, shuffle letters, and store data in an immutable form.
