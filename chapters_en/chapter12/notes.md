# 📝 Notes on Chapter 12 — Sprite Control and Animation

In this chapter, I learned how to control sprite movement using keyboard input, create animations, and work with sounds and music. It also demonstrated how to work with rotating and moving objects, as well as object interaction with animations and sounds.

---

## 📚 New Concepts

### 1. Reading Keyboard Input

🔹 In this example, using the **W**, **A**, **S**, and **D** keys, I learned to move a sprite (spaceship) across the screen.

```python
class Ship(games.Sprite):
    """ Movable spaceship. """
    def update(self):
        """ Moves the ship based on pressed keys. """
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1
        if games.keyboard.is_pressed(games.K_s):
            self.y += 1
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 1
        if games.keyboard.is_pressed(games.K_d):
            self.x += 1
````

🔹 I used the `games.keyboard.is_pressed` function to check key presses and move the object along the `x` and `y` coordinates.

---

### 2. Rotating the Sprite

🔹 I learned how to rotate a sprite using the **left** and **right** arrow keys, as well as set rotation angles to specific values from **1** to **4**.

```python
class Ship(games.Sprite):
    """ Rotating spaceship. """
    def update(self):
        """ Rotates the ship when arrow keys are pressed. """
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 1
```

🔹 Using the `angle` property, I changed the sprite's rotation angle, and used the keys to adjust the angle to **0**, **90**, **180**, and **270**.

---

### 3. Sprite Animation

🔹 I learned to create animations using multiple frames, allowing me to create an explosion animation.

```python
explosion = games.Animation(images=explosion_files,
                            x=games.screen.width / 2,
                            y=games.screen.height / 2,
                            n_repeats=0,
                            repeat_interval=5)
```

🔹 The animation was configured to play a set of images in a loop with a specific interval between frames.

---

### 4. Sounds and Music

🔹 I explored how to work with sounds and music, including loading, playing, looping, and stopping sound effects and music tracks.

```python
missile_sound = games.load_sound("missile.wav")
games.music.load("theme.mid")
```

🔹 Several playback options were shown, including looping and stopping playback.

---

### 5. Moving Objects — Asteroids

🔹 In this example, I created asteroids that move across the screen and wrap around its edges. Using random parameters, I was able to create varied asteroids with different sizes and speeds.

```python
class Asteroid(games.Sprite):
    """ Asteroid that moves straight across the screen. """
    def update(self):
        """ Makes the asteroid wrap around the screen. """
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
```

🔹 The asteroids use the `update` method to "wrap" around the screen and reappear from the opposite side.

---

### 6. Controlling the Spaceship

🔹 The player's ship can rotate left and right using the arrow keys. In this program, asteroids move across the screen, interacting with the player's ship.

```python
class Ship(games.Sprite):
    """ Player's ship. """
    def update(self):
        """ Rotates the ship when the arrow keys are pressed. """
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
```

🔹 This example adds the ability to control the ship using the arrow keys.

---

📌 This chapter taught me how to control sprite movement with keys, create animations, and work with sounds and music in the program. I also learned how to interact with objects and control their behavior on the screen.
