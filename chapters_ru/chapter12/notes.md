# 📝 Заметки по главе 12 — Управление спрайтами и анимацией

В этой главе я научился управлять движением спрайтов с помощью клавиш, анимацией, звуками и музыкой. Также был продемонстрирован способ работы с вращающимися и движущимися объектами, а также взаимодействие объектов с анимацией и звуками.

---

## 📚 Новые сущности

### 1. Чтение клавиатурного ввода

🔹 В данном примере с использованием клавиш **W**, **A**, **S**, **D** я научился перемещать спрайт (космический корабль) по экрану.

```python
class Ship(games.Sprite):
    """ Подвижный космический корабль. """
    def update(self):
        """ Перемещает корабль в зависимости от нажатых клавиш. """
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1
        if games.keyboard.is_pressed(games.K_s):
            self.y += 1
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 1
        if games.keyboard.is_pressed(games.K_d):
            self.x += 1
```

🔹 В этом примере я использовал функцию `games.keyboard.is_pressed` для проверки нажатия клавиш и перемещения объекта по координатам `x` и `y`.

---

### 2. Вращение спрайта

🔹 Я изучил вращение спрайта с помощью клавиш **влево** и **вправо**, а также установку углов поворота с помощью чисел от **1** до **4**.

```python
class Ship(games.Sprite):
    """ Вращающийся космический корабль. """
    def update(self):
        """ Вращает корабль при нажатии клавиш со стрелками. """
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 1
```

🔹 С помощью метода `angle` я изменял угол поворота спрайта, а также использовал клавиши для точной настройки углов на значения **0**, **90**, **180** и **270**.

---

### 3. Анимация спрайтов

🔹 Я научился создавать анимации с использованием нескольких кадров, что позволило мне воспроизвести анимацию взрыва.

```python
explosion = games.Animation(images=explosion_files,
                            x=games.screen.width / 2,
                            y=games.screen.height / 2,
                            n_repeats=0,
                            repeat_interval=5)
```

🔹 Анимация была настроена на проигрывание набора изображений в цикле с определенным интервалом времени между кадрами.

---

### 4. Звуки и музыка

🔹 Изучил способы работы с звуками и музыкой, включая загрузку, воспроизведение, циклизацию и остановку звуковых эффектов и музыкальных треков.

```python
missile_sound = games.load_sound("missile.wav")
games.music.load("theme.mid")
```

🔹 Было рассмотрено несколько вариантов воспроизведения звуков и музыки, а также возможность цикличности и остановки воспроизведения.

---

### 5. Движущиеся объекты — астероиды

🔹 В этом примере я создал астероиды, которые движутся по экрану, обогнув его края. Используя случайные параметры, я смог создать разнообразные астероиды с разными размерами и скоростями.

```python
class Asteroid(games.Sprite):
    """ Астероид, прямолинейно движущийся по экрану. """
    def update(self):
        """ Заставляет астероид обогнуть экран. """
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
```

🔹 Астероиды используют метод `update` для того, чтобы «выходить» за пределы экрана и снова появляться с противоположной стороны.

---

### 6. Управление космическим кораблем

🔹 Корабль игрока может вращаться влево и вправо с помощью стрелок. Также в этой программе используются астероиды, которые двигаются по экрану, взаимодействуя с кораблем игрока.

```python
class Ship(games.Sprite):
    """ Корабль игрока. """
    def update(self):
        """ Вращает корабль при нажатии клавиш со стрелками. """
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
```

🔹 В этом примере добавлена возможность управления кораблем с использованием клавиш стрелок.

---

📌 Эта глава научила меня управлять движением спрайтов с помощью клавиш, создавать анимации и работать с звуками и музыкой в программе. Также я изучил, как взаимодействовать с объектами и управлять их поведением на экране.
