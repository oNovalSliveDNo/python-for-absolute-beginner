# Только согласные
# Демонстрирует, как создавать новые строки из исходных с помощью цикла for

message = input("Введите текст: ")
new_message = ""
VOWELS = "аеiоuаеёиоуыэюя"
print()

for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("Создана новая строка:", new_message)

print("\nBoт ваш текст с изъятыми гласными буквами:", new_message)

input("\n\nHaжмитe Enter, чтобы выйти.")
