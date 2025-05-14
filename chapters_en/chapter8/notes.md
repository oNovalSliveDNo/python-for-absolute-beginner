# 📝 Notes on Chapter 8 — Classes and Objects

In this chapter, I learned how to create my own classes and objects, use constructors, instance and class attributes, properties, and private attributes and methods.

---

## 📚 New Concepts

### 1. Creating a Class and Object

```python
class Critter(object):
    """Virtual pet"""
    def talk(self):
        print("Hello. I am a critter - an instance of the Critter class.")

# Creating an object
crit = Critter()
crit.talk()
````

---

### 2. Constructor `__init__`

```python
class Critter(object):
    def __init__(self):
        print("A new critter has been born!")

    def talk(self):
        print("Hello. I am a critter - an instance of the Critter class.")

crit1 = Critter()
crit2 = Critter()
crit1.talk()
```

---

### 3. Instance Attributes and `__str__` Method

```python
class Critter(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Critter object\nname: " + self.name + "\n"

    def talk(self):
        print("Hello. My name is", self.name)

crit = Critter("Bobik")
print(crit)            # Calling __str__
print(crit.name)       # Direct access to the attribute
```

---

### 4. Class Attributes and Static Methods

```python
class Critter(object):
    total = 0  # Class attribute

    @staticmethod
    def status():
        print("There are currently", Critter.total, "critters")

    def __init__(self, name):
        self.name = name
        Critter.total += 1

Critter.status()
c1 = Critter("A")
c2 = Critter("B")
Critter.status()
```

---

### 5. Private Attributes and Methods (`__name`)

```python
class Critter(object):
    def __init__(self, name, mood):
        self.name = name
        self.__mood = mood  # Private attribute

    def talk(self):
        print("My name is", self.name)
        print("I feel", self.__mood)

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print("This is a public method.")
        self.__private_method()

crit = Critter("Bobik", "happy")
crit.talk()
crit.public_method()
```

---

### 6. Properties (`@property`, `@name.setter`)

```python
class Critter(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Name cannot be empty.")
        else:
            self.__name = new_name

crit = Critter("Bobik")
print(crit.name)
crit.name = "Murzik"
print(crit.name)
crit.name = ""  # Error
```

---

📌 This chapter taught me how to create classes, manage the internal state of objects, use encapsulation and properties, and write simple simulations with objects.
