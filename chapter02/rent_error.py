# Рантье (версия с ошибкой)
# Демонстрирует логическую ошибку

# Многострочная строка с описанием программы — выводится вся сразу
print(
    """
                    Рантье
    Программа подсчитывает ваши ежемесячные расходы. Эту статистику нужно 
    знать, чтобы у вас не закончились деньги и вам не пришлось искать работу.
    
    Введите суммы расходов по всем статьям, перечисляемым ниже. Вы богаты - 
    так не мелочитесь, пишите суммы в долларах, без центов.
    """
)

# Получаем расходы пользователя по разным категориям
# input() всегда возвращает строку, даже если пользователь вводит число
car = input("Техническое обслуживание машины 'Ламборгини': ")
rent = input("Съем роскошной квартиры на Манхэттене: ")
get = input("Аренда самолета: ")
gifts = input("Подарки: ")
food = input("Обеды и ужины в ресторанах: ")
staff = input("Жалованье прислуги (дворецкий, повар, водитель, секретарь): ")
guru = input("Плата личному психоаналитику: ")
games = input("Компьютерные игры: ")

# ЛОГИЧЕСКАЯ ОШИБКА:
# Здесь происходит сложение строк, а не чисел — так как переменные содержат строки
# Например: "1000" + "2000" = "10002000", а не 3000
total = car + rent + get + gifts + food + staff + guru + games

# Вывод "общей суммы", но это на самом деле просто склеенные строки
print("\nобщая сумма:", total)

# Ждём нажатия Enter, чтобы программа не закрылась сразу
input("\n\nНажмите Enter, чтобы выйти.")
