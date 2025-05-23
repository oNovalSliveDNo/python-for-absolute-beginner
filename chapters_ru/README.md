# 📚 Главы на русском языке

Эта папка содержит материалы и примеры к книге **"Python Programming for the Absolute Beginner"** Майкла Доусона на русском языке.

Все примеры, упражнения и заметки структурированы по главам в отдельных каталогах.

> 📝 Все примеры адаптированы и протестированы на **Python 3.13.3**.  
> ⚠ Оригинальный код из книги написан для Python 3.1.1, поэтому возможны отличия.

---

## 📂 Структура папок

Каждая глава представлена в отдельной папке и включает:

- `.py` — примеры кода из главы;
- `README.md` — описание и инструкции по запуску примеров;
- `notes.md` — личные заметки и пояснения.

### Пример структуры:
```markdown
chapters_ru/
├── chapter01/
│   ├── README.md
│   ├── game_over.py
│   └── notes.md
├── chapter02/
│   └── ...
└── ...
```

---

## 🚀 Как запустить примеры

1. Перейдите в папку нужной главы:

```bash
cd chapters_ru/chapter01
```

2. Запустите нужный Python файл:

```bash
python game_over.py
```

3. При необходимости используйте виртуальное окружение и убедитесь, что используется Python **3.13.3**:

```bash
python --version
```

---

## 💡 Полезно знать

* В главах 11 и 12 для примеров с графикой и звуком используются сторонние библиотеки `pygame` и `superwires`.
* Для их работы установите зависимости:

```bash
pip install pygame superwires
```

Или установите зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

* В остальных главах используются только стандартные библиотеки Python.

---

## 📘 Источник

* Michael Dawson — *Python Programming for the Absolute Beginner*
* Издание: 3rd Edition
* Фокус: обучение программированию с нуля на Python через создание игр и интерактивных программ.
