# 📝 Заметки по главе 9 — Взаимодействие объектов и наследование

В этой главе я научился создавать взаимодействующие между собой объекты, использовать наследование, переопределять методы, а также создавать собственные модули и использовать их в других программах.

---

## 📚 Новые сущности

### 1. Взаимодействие объектов

```python
class Player(object):
    """Игрок в экшен-игре."""
    def blast(self, enemy):
        print("Игрок стреляет во врага.\n")
        enemy.die()

class Alien(object):
    """Враждебный пришелец-инопланетянин."""
    def die(self):
        print("Тяжело дыша, пришелец произносит: 'Прощай, безжалостный мир.'")

# Создание и взаимодействие объектов
hero = Player()
invader = Alien()
hero.blast(invader)
```

---

### 2. Составные объекты и композиция

```python
class Card(object):
    """Игральная карта."""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + self.suit

class Hand(object):
    """'Рука' игрока — набор карт."""
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def clear(self):
        self.cards = []

    def __str__(self):
        return " ".join(str(card) for card in self.cards) if self.cards else "<пусто>"

# Работа с составными объектами
card1 = Card("A", "c")
my_hand = Hand()
my_hand.add(card1)
print(my_hand)
```

---

### 3. Наследование и расширение класса

```python
class Deck(Hand):
    """Колода карт — наследует Hand."""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for _ in range(per_hand):
            for hand in hands:
                if self.cards:
                    self.give(self.cards[0], hand)
```

---

### 4. Переопределение методов в наследуемых классах

```python
class Unprintable_Card(Card):
    """Карта, которую нельзя напечатать."""
    def __str__(self):
        return "<нельзя напечатать>"

class Positionable_Card(Card):
    """Карта, которую можно переворачивать."""
    def __init__(self, rank, suit, face_up=True):
        super().__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        return super().__str__() if self.is_face_up else "XX"

    def flip(self):
        self.is_face_up = not self.is_face_up
```

---

### 5. Создание и использование модуля

```python
# games.py — модуль с классами и функциями
class Player(object):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}:\t{self.score}"

def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
```

---

### 6. Импорт и использование собственного модуля

```python
import games, random

print("Добро пожаловать в простую игру!\n")

again = None
while again != "n":
    players = []
    num = games.ask_number("Сколько игроков? (2 - 5): ", 2, 5)
    for i in range(num):
        name = input("Имя игрока: ")
        score = random.randrange(100) + 1
        players.append(games.Player(name, score))

    print("\nРезультаты игры:")
    for player in players:
        print(player)

    again = games.ask_yes_no("\nХотите сыграть еще раз? (y/n): ")
```

---

📌 Эта глава научила меня создавать программы с взаимодействующими объектами, использовать наследование для расширения классов, переопределять методы и создавать собственные модули для использования в других проектах.
