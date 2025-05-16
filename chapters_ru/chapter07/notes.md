# 📝 Заметки по главе 7 — Работа с файлами и обработка ошибок

В этой главе я научился читать и записывать файлы, сериализовать данные с помощью `pickle` и `shelve`, обрабатывать исключения.

---

## 📚 Новые сущности

### 1. Чтение из файла (`open`, `read`, `readline`, `readlines`)

Открытие и чтение файлов:

```python
# Открытие файла
file = open("example.txt", "r")

# Чтение одного символа
print(file.read(1))

# Чтение строки
print(file.readline())

# Чтение всех строк в список
lines = file.readlines()

# Перебор строк
for line in lines:
    print(line)

# Закрытие файла
file.close()
```

---

### 2. Запись в файл (`write`, `writelines`)

Создание и запись в файл:

```python
# Запись по строкам
file = open("write_example.txt", "w")
file.write("Первая строка\n")
file.write("Вторая строка\n")
file.close()

# Запись списка строк
lines = ["Строка 1\n", "Строка 2\n"]
file = open("write_example.txt", "w")
file.writelines(lines)
file.close()
```

---

### 3. Сериализация: `pickle` и `shelve`

Сохранение (консервация) объектов:

```python
import pickle

# Сохранение объектов
data = ["яблоко", "банан", "вишня"]
with open("data.dat", "wb") as f:
    pickle.dump(data, f)

# Загрузка объектов
with open("data.dat", "rb") as f:
    data_loaded = pickle.load(f)
    print(data_loaded)
```

Использование `shelve` (ключ-значение, как словарь):

```python
import shelve

shelf = shelve.open("mydata")
shelf["fruits"] = ["яблоко", "груша", "слива"]
print(shelf["fruits"])
shelf.close()
```

---

### 4. Обработка исключений (`try`, `except`, `else`)

Основы обработки ошибок:

```python
try:
    num = float(input("Введите число: "))
except ValueError:
    print("Это не число!")
```

Обработка нескольких типов исключений:

```python
for value in (None, "Привет"):
    try:
        print(float(value))
    except (TypeError, ValueError):
        print("Нельзя преобразовать значение.")
```

Получение аргумента исключения:

```python
try:
    num = float(input("Введите число: "))
except ValueError as e:
    print("Ошибка:", e)
```

Блок `else` при отсутствии исключений:

```python
try:
    num = float(input("Введите число: "))
except ValueError:
    print("Это не число!")
else:
    print("Вы ввели:", num)
```

---

📌 Эта глава научила меня работать с файлами, сериализовать данные, обрабатывать ошибки.
