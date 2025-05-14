# 📘 Chapter 11 — Simple Graphics and Sprites with Superwires (Livewires)

In this chapter, we explore creating graphical windows and working with sprites using the `superwires` library (the modern version of `livewires`). It covers the basics of displaying images, text, as well as animation and interaction with objects using the mouse and collision detection.

## 🧠 Key Topics

- Creating a graphical window (`games.init()`)
- Setting a background image
- Displaying text and messages (`games.Text`, `games.Message`)
- Creating and animating sprites (`games.Sprite`)
- Controlling sprites with the mouse
- Checking for sprite collisions
- Handling game over events

## 🚀 Files

- `new_graphics_window.py` — creating an empty graphics window.
- `background_image.py` — setting a background image.
- `pizza_sprite.py` — displaying a pizza sprite on the background.
- `big_score.py` — displaying a large numerical score on the screen.
- `you_won.py` — showing a victory message.
- `moving_pizza.py` — animating a moving pizza.
- `bouncing_pizza.py` — pizza bouncing off screen edges.
- `moving_pan.py` — controlling a sprite (pan) with the mouse.
- `slippery_pizza.py` — sprite interaction: pizza "slips away" when touched by the pan.
- `pizza_panic.py` — final project: a game where you must catch falling pizzas while avoiding misses.

## ⚠ Important Note

The original **Livewires** library is outdated and causes errors:

```python
from livewires import games
````

Trying to run it results in an error:

```
ModuleNotFoundError: No module named 'beginners'
```

Therefore, you should use the modern compatible version:

```python
from superwires import games
```

## 📌 Running

> Replace the filename with the one you need.

```bash
python <filename>.py
```
