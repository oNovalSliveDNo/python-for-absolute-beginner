# 📝 Заметки по главе 8 — Классы и объекты

В этой главе я научился создавать собственные классы и объекты, использовать конструкторы, атрибуты экземпляра и класса, свойства, закрытые атрибуты и методы.

---

## 📚 Новые сущности

### 1. Создание класса и объекта

```python
class Critter(object):
    """Виртуальный питомец"""
    def talk(self):
        print("Привет. Я зверюшка - экземпляр класса Critter.")

# Создание объекта
crit = Critter()
crit.talk()
```

---

### 2. Конструктор `__init__`

```python
class Critter(object):
    def __init__(self):
        print("Появилась на свет новая зверюшка!")

    def talk(self):
        print("Привет. Я зверюшка - экземпляр класса Critter.")

crit1 = Critter()
crit2 = Critter()
crit1.talk()
```

---

### 3. Атрибуты экземпляра и метод `__str__`

```python
class Critter(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Critter object\nимя: " + self.name + "\n"

    def talk(self):
        print("Привет. Меня зовут", self.name)

crit = Critter("Бобик")
print(crit)            # Вызов __str__
print(crit.name)       # Прямой доступ к атрибуту
```

---

### 4. Атрибуты класса и статические методы

```python
class Critter(object):
    total = 0  # Атрибут класса

    @staticmethod
    def status():
        print("Всего зверюшек сейчас", Critter.total)

    def __init__(self, name):
        self.name = name
        Critter.total += 1

Critter.status()
c1 = Critter("А")
c2 = Critter("Б")
Critter.status()
```

---

### 5. Закрытые атрибуты и методы (`__имя`)

```python
class Critter(object):
    def __init__(self, name, mood):
        self.name = name
        self.__mood = mood  # Закрытый атрибут

    def talk(self):
        print("Меня зовут", self.name)
        print("Сейчас я чувствую себя", self.__mood)

    def __private_method(self):
        print("Это закрытый метод.")

    def public_method(self):
        print("Это открытый метод.")
        self.__private_method()

crit = Critter("Бобик", "весело")
crit.talk()
crit.public_method()
```

---

### 6. Свойства (`@property`, `@name.setter`)

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
            print("Имя не может быть пустым.")
        else:
            self.__name = new_name

crit = Critter("Бобик")
print(crit.name)
crit.name = "Мурзик"
print(crit.name)
crit.name = ""  # Ошибка
```

---

📌 Эта глава научила меня создавать классы, управлять внутренним состоянием объектов, использовать инкапсуляцию и свойства, а также писать простые симуляции с объектами.
