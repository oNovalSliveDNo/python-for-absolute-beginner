# Ничего себе результат!
# Демонстрирует отображение текста на графическом экране

from superwires import games, \
    color  # Импортируем необходимые модули: games — для работы с графикой, color — для задания цветов

# Инициализируем графическое окно:
# - ширина 640 пикселей
# - высота 480 пикселей
# - частота обновления экрана — 50 кадров в секунду
games.init(screen_width=640, screen_height=480, fps=50)

# Загружаем фоновое изображение (например, стена) и сохраняем в переменную
# transparent=False — указывает, что у картинки не будет прозрачных областей
wall_image = games.load_image("wall.jpg", transparent=False)

# Устанавливаем фоновое изображение для графического окна
games.screen.background = wall_image

# Создаем текстовый объект, отображающий число 1756521
# - размер шрифта: 60 пикселей
# - цвет текста: черный
# - координаты: x=550, y=30 (справа сверху)
score = games.Text(value=1756521,  # Сам текст (число, например, очки)
                   size=60,  # Размер шрифта
                   color=color.black,  # Цвет текста
                   x=550,  # Горизонтальное положение на экране
                   y=30)  # Вертикальное положение на экране

# Добавляем текстовый объект на экран, чтобы он отображался поверх фона
games.screen.add(score)

# Запускаем главный цикл программы — окно остаётся активным и отображает все элементы
games.screen.mainloop()
