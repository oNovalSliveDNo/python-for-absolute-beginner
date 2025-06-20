# Гибель пришельца
# Демонстрирует взаимодействие объектов

class Player(object):
    """ Игрок в экшен-игре. """

    def blast(self, enemy):
        """Метод, который выполняет выстрел в врага и вызывает его смерть."""
        print("Игpoк стреляет во врага.\n")  # Сообщение о выстреле игрока
        enemy.die()  # Враг умирает, вызывается его метод die()


class Alien(object):
    """ Враждебный пришелец-инопланетянин в экшен-игре. """

    def die(self):
        """Метод, который вызывается, когда пришелец умирает."""
        print("Tяжeлo дыша, пришелец произносит: 'Ну, вот и все. Спета моя песенка. \n" \
              "Уже и в глазах темнеет... Передай полутора миллионам моих личинок, что я любил их... \n" \
              "Прощай, безжалостный мир.'")  # Сообщение о гибели пришельца


# Основная часть программы
print("\t\tГибeль пришельца\n")  # Приветственное сообщение

hero = Player()  # Создаем объект игрока
invader = Alien()  # Создаем объект пришельца
hero.blast(invader)  # Игрок стреляет по пришельцу, вызывается его смерть

input("\n\nHaжмите Enter, чтобы выйти.")  # Ожидание нажатия Enter перед завершением программы
