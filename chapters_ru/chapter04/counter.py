# Считалка
# Демонстрирует использование функции range()

print("Посчитаем:")
for i in range(10):
    print(i, end=" ")

print("\n\nПеречислим кратные пяти:")
for i in range(0, 50, 5):
    print(i, end=" ")

print("\n\nПocчитaeм в обратном порядке:")
for i in range(10, 0, -1):
    print(i, end=" ")

input("\n\n\nHaжмитe Enter, чтобы выйти.")
