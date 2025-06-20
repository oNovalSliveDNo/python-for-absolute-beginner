# Новое графическое окно
# Демонстрирует создание графического окна

from superwires import games  # Импортируем модуль games из библиотеки superwires

# Инициализируем игровое окно:
# - ширина 640 пикселей
# - высота 480 пикселей
# - fps (количество кадров в секунду) — 50
games.init(screen_width=640, screen_height=480, fps=50)

# Запускаем главный цикл экрана — окно открывается и остаётся активным
games.screen.mainloop()
