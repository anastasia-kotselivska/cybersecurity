from collections import Counter

#Зчитування тексту з файлу
with open("V6.txt", "r", encoding="utf-8") as file:
    text = file.read()

#Видалення символу переходу на новий рядок у кінці файлу
text = text.rstrip("\n")

#Підрахунок загальної кількості символів
total = len(text)

#Підрахунок частоти появи кожного символу
frequency = Counter(text)

#Виведення результатів обчислення частот
print("Загальна кількість символів:", total)
print("\nЧастота появи кожного символу:")
print("-" * 45)
print(f"{'Символ':<15} {'Кількість':<15} {'Частота':<15}")
print("-" * 45)

for symbol, count in frequency.most_common():
    relative_frequency = (count / total)

    if symbol == " ":
        display_symbol = "Пробіл"
    else:
        display_symbol = symbol

    print(f"{display_symbol:<15} {count:<15} {relative_frequency:.3f}")

print("-" * 45)

alpha = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя,.- "
ciph_alpha = "дорга веп,зинт-учкюь.бґєжіїйлмсфхшщяц"
#Розшифрування
dec_table = str.maketrans(ciph_alpha, alpha)
plain_text = text.translate(dec_table)

print("\nТАБЛИЦЯ ПІДСТАНОВКИ")
print(f"Відкритий алфавіт: {alpha}")
print(f"Шифроалфавіт:      {ciph_alpha}")

print("\nРОЗШИФРОВАНИЙ ТЕКСТ")
print(plain_text)
#Запис розшифрованого тексту у файл
with open("decrypted_V6.txt", "w", encoding="utf-8") as file:
    file.write(plain_text)
