# 📘 Chapter 12 — Basics of Animation and Sound in Python

This chapter covers the basics of animation and working with graphics and sound effects in Python using the **SuperWires** library. Examples include creating moving objects, animating explosions, playing sounds and music (including looping), as well as using keyboard input to control objects on the screen.

## 🧠 Key Topics

- Handling keyboard input to move objects on the screen.
- Rotating sprites based on pressed keys.
- Creating animations such as explosions.
- Playing sounds and music, including looping playback.
- Moving objects like asteroids across the screen with collision detection.
- Building gameplay using sprites and animation.
- Implementing a game interface with control elements.

## 🚀 Files

- `read_key.py` — demonstrates reading key presses to control object movement.
- `rotate_sprite.py` — rotates a sprite using keyboard input.
- `explosion.py` — creates an explosion animation using a series of images.
- `sound_and_music.py` — example of playing sounds and music, including looping.
- `astrocrash01.py` — moves asteroids across the screen.
- `astrocrash02.py` — continuation of the asteroid project.
- `astrocrash03.py` — adds ship movement.
- `astrocrash04.py` — adds missile shooting.
- `astrocrash05.py` — adds shooting delay for missiles.
- `astrocrash06.py` — handles object collisions.
- `astrocrash07.py` — adds explosion effects on collision.
- `astrocrash08.py` — adds objects for game over conditions.

## ⚠ Important Note

The original **LiveWires** library is outdated and causes errors:

```python
from livewires import games
````

When attempting to run it, you get an error:

```bash
ModuleNotFoundError: No module named 'beginners'
```

Therefore, you should use the modern compatible version:

```python
from superwires import games
```

## 📌 Running

> Replace the file name with the one you want to run.

```bash
python <file_name>.py
```
