# 📝 Notes on Chapter 11 — Graphics and Sprites with SuperWires

In this chapter, I learned how to use the SuperWires module to create graphic windows, work with background images, display text, control sprites and handle their collisions, as well as process keyboard and mouse input.

---

## 📚 New Concepts

### 1. Creating a graphic window

```python
from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)
games.screen.mainloop()
````

🔹 The `games.init` method creates a window with specified dimensions and frame rate.

---

### 2. Setting a background image

```python
wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image
```

🔹 The `games.load_image` method loads an image.
🔹 The background image is set via `games.screen.background`.

---

### 3. Displaying text on the screen

```python
from superwires import games, color

score = games.Text(value=1756521, size=60, color=color.black, x=550, y=30)
games.screen.add(score)
```

🔹 Use `games.Text` to display a number or text on the screen.

---

### 4. Displaying messages with lifetime and ending the game

```python
won_message = games.Message(value="You won!", size=100, color=color.red, x=320, y=240, lifetime=250, after_death=games.screen.quit)
games.screen.add(won_message)
```

🔹 The `games.Message` class shows a message on the screen, automatically removing it after a given time (`lifetime`), and optionally calling a function (`after_death`) after it disappears.

---

### 5. Moving sprites and controlling speed

```python
the_pizza = games.Sprite(image=pizza_image, x=320, y=240, dx=1, dy=1)
games.screen.add(the_pizza)
```

🔹 The `games.Sprite` class allows creating and animating objects by setting speed along `dx` and `dy`.

---

### 6. Handling sprite collisions with screen borders

```python
if self.right > games.screen.width or self.left < 0:
    self.dx = -self.dx
```

🔹 Checks for sprite collisions with the screen edges and changes the direction accordingly.

---

### 7. Controlling sprites with the mouse

```python
self.x = games.mouse.x
self.y = games.mouse.y
```

🔹 Use `games.mouse.x` and `games.mouse.y` to bind the sprite’s position to the mouse pointer.

---

### 8. Checking sprite collisions

```python
for pizza in self.overlapping_sprites:
    pizza.handle_collide()
```

🔹 The `self.overlapping_sprites` list contains sprites overlapping with the current sprite, allowing collision handling.

---

### 9. Game control: ending the game and showing results

```python
end_message = games.Message(value="Game Over", size=90, color=color.red, x=320, y=240, lifetime=250, after_death=games.screen.quit)
games.screen.add(end_message)
```

🔹 When the sprite reaches the bottom of the screen, the game ends and a message is displayed.

---

📌 This chapter taught me how to create complete graphic games with animation, mouse control, and text display using SuperWires.
