# 📝 Заметки по главе 11 — Графика и спрайты с SuperWires

В этой главе я научился использовать модуль SuperWires для создания графических окон, работы с фоновыми изображениями, отображения текста, управления спрайтами и их столкновениями, а также обрабатывать ввод с клавиатуры и мыши.

---

## 📚 Новые сущности

### 1. Создание графического окна

```python
from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)
games.screen.mainloop()
```

🔹 Используется метод `games.init` для создания окна с заданными размерами и частотой обновления кадров.  

---

### 2. Назначение фонового изображения

```python
wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image
```

🔹 Метод `games.load_image` загружает изображение.  
🔹 Фоновое изображение устанавливается через `games.screen.background`.  

---

### 3. Отображение текста на экране

```python
from superwires import games, color

score = games.Text(value=1756521, size=60, color=color.black, x=550, y=30)
games.screen.add(score)
```

🔹 Использование `games.Text` для отображения числового значения или текста на экране.  

---

### 4. Отображение сообщений с временем жизни и завершением игры

```python
won_message = games.Message(value="You won!", size=100, color=color.red, x=320, y=240, lifetime=250, after_death=games.screen.quit)
games.screen.add(won_message)
```

🔹 Класс `games.Message` показывает сообщение на экране с автоматическим удалением через заданное время (`lifetime`), после чего может вызываться функция `after_death`.

---

### 5. Движущиеся спрайты и управление скоростью

```python
the_pizza = games.Sprite(image=pizza_image, x=320, y=240, dx=1, dy=1)
games.screen.add(the_pizza)
```

🔹 Класс `games.Sprite` позволяет создать и анимировать объекты, задавая скорость по осям `dx` и `dy`.

---

### 6. Обработка столкновений спрайтов с границами экрана

```python
if self.right > games.screen.width or self.left < 0:
    self.dx = -self.dx
```

🔹 Проверяется пересечение спрайта с границами экрана, и изменяется направление движения.

---

### 7. Управление спрайтом мышью

```python
self.x = games.mouse.x
self.y = games.mouse.y
```

🔹 Использование `games.mouse.x` и `games.mouse.y` для привязки позиции спрайта к указателю мыши.

---

### 8. Проверка соприкосновения спрайтов

```python
for pizza in self.overlapping_sprites:
    pizza.handle_collide()
```

🔹 Список `self.overlapping_sprites` содержит спрайты, пересекающиеся с данным, что позволяет обрабатывать столкновения.

---

### 9. Управление игрой: окончание игры и отображение результата

```python
end_message = games.Message(value="Game Over", size=90, color=color.red, x=320, y=240, lifetime=250, after_death=games.screen.quit)
games.screen.add(end_message)
```

🔹 При достижении нижней границы спрайтом вызывается метод завершения игры с отображением сообщения.

---

📌 Эта глава научила меня создавать полноценные графические игры с анимацией, управлением мышью и отображением текста, используя SuperWires.
