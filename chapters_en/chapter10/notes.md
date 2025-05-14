# 📝 Notes on Chapter 10 — GUI Basics with tkinter

In this chapter, I got acquainted with the `tkinter` library and learned how to create simple graphical user interfaces: windows, labels, buttons, entry fields and text areas, checkbuttons, and radiobuttons. I also learned how to bind user actions to event handlers and organize the interface using the `grid` layout manager.

---

## 📚 New Concepts

### 1. Creating a window and basic GUI

```python
from tkinter import *

root = Tk()
root.title("Window Title")
root.geometry("200x100")
root.mainloop()
````

🔹 Use `Tk()` to create the main window
🔹 Set the window title and size
🔹 Start the event loop with `mainloop()`

---

### 2. Working with `Label` and `Frame`

```python
app = Frame(root)
app.grid()

lbl = Label(app, text="Example Label")
lbl.grid()
```

🔹 `Frame` is used to organize elements inside the window
🔹 `Label` displays text
🔹 `grid()` places elements in a grid layout

---

### 3. Creating buttons (`Button`)

```python
bttn = Button(app, text="Click Me")
bttn.grid()
```

🔹 `Button` creates a clickable button
🔹 Use `configure` or direct assignment (`bttn["text"]`) to change button properties

---

### 4. Creating a GUI class by inheriting from `Frame`

```python
class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
```

🔹 Inheritance from `Frame`
🔹 `create_widgets` method — a template for adding interface elements

---

### 5. Binding a button to an event handler

```python
self.bttn = Button(self, text="Click", command=self.update_count)
```

🔹 The `command` argument binds the button to a function
🔹 Allows actions to be performed when the button is clicked (e.g., count clicks)

---

### 6. Entry fields (`Entry`) and text areas (`Text`)

```python
self.pw_ent = Entry(self)
self.secret_txt = Text(self, width=35, height=5, wrap=WORD)
```

🔹 `Entry` — single-line text input
🔹 `Text` — multi-line text area
🔹 Use `get()`, `delete()`, `insert()` to interact with content

---

### 7. `grid` layout manager

```python
widget.grid(row=0, column=0, columnspan=2, sticky=W)
```

🔹 Allows precise control over element placement in the window
🔹 Parameters `row`, `column`, `columnspan`, `sticky` — for flexible layout settings

---

### 8. Checkbuttons (`Checkbutton`) and boolean variables (`BooleanVar`)

```python
self.likes_comedy = BooleanVar()
Checkbutton(self, text="Comedy", variable=self.likes_comedy)
```

🔹 `Checkbutton` — checkbox element
🔹 `BooleanVar` stores the checkbox state (`True` / `False`)

---

### 9. Radiobuttons (`Radiobutton`) and string variables (`StringVar`)

```python
self.favorite = StringVar()
Radiobutton(self, text="Drama", variable=self.favorite, value="drama")
```

🔹 `Radiobutton` allows selecting one option from a group
🔹 `StringVar` stores the selected value
🔹 All radiobuttons in a group must refer to the same variable

---

📌 This chapter taught me how to create basic graphical user interfaces using `tkinter`, use controls, bind actions to event handlers, and manage input/output through entry fields and text areas.
