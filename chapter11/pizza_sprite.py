# Спрайт-пицца
# Демонстрирует создание спрайта

from superwires import games  # Импортируем модуль games из библиотеки superwires

# Инициализируем графическое окно:
# - ширина окна 640 пикселей
# - высота окна 480 пикселей
# - частота обновления экрана — 50 кадров в секунду
games.init(screen_width=640, screen_height=480, fps=50)

# Загружаем фоновое изображение (стена) и сохраняем его в переменную
# transparent=False означает, что у изображения не будет прозрачных участков
wall_image = games.load_image("wall.jpg", transparent=False)

# Устанавливаем изображение стены как фон для графического экрана
games.screen.background = wall_image

# Загружаем изображение пиццы
pizza_image = games.load_image("pizza.bmp")

# Создаем спрайт (объект) с изображением пиццы и указываем его координаты на экране (по центру)
pizza = games.Sprite(image=pizza_image, x=320, y=240)

# Добавляем пиццу на экран, чтобы она отобразилась поверх фона
games.screen.add(pizza)

# Запускаем главный цикл программы — окно открывается и остаётся активным
games.screen.mainloop()
