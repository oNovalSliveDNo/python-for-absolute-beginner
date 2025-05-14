# 📚 Chapters in English

This folder contains materials and examples for the book **"Python Programming for the Absolute Beginner"** by Michael Dawson in English.

All examples, exercises, and notes are organized by chapters in separate directories.

> 📝 All examples have been adapted and tested with **Python 3.13.3**.  
> ⚠ The original code in the book was written for Python 3.1.1, so there may be some differences.

---

## 📂 Folder Structure

Each chapter is represented in a separate folder and includes:

- `.py` — example code from the chapter;
- `README.md` — description and instructions for running the examples;
- `notes.md` — personal notes and explanations (optional).

### Example structure:
```markdown
chapters_en/
├── chapter1/
│   ├── README.md
│   ├── game_over.py
│   └── notes.md
├── chapter2/
│   └── ...
└── ...
````

---

## 🚀 How to Run Examples

1. Navigate to the desired chapter folder:

```bash
cd chapters_en/chapter1
```

2. Run the desired Python file:

```bash
python game_over.py
```

3. If needed, use a virtual environment and make sure you are using Python **3.13.3**:

```bash
python --version
```

---

## 💡 Good to Know

* In chapters 11 and 12, for graphics and sound examples, the third-party libraries `pygame` and `superwires` are used.
* To run these examples, install the dependencies:

```bash
pip install pygame superwires
```

Or install all dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

* In other chapters, only Python's standard libraries are used.

---

## 📘 Source

* Michael Dawson — *Python Programming for the Absolute Beginner*
* Edition: 3rd Edition
* Focus: Learning programming from scratch using Python through the creation of games and interactive programs.
