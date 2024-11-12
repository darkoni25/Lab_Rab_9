import re
from collections import defaultdict

# Етап а: Створення текстового файлу TF4_1 із символами різної довжини
def create_text_file():
    text = """Привіт, це приклад тексту для файлу TF4_1. Цей текст містить слова різної довжини: короткі й довгі слова, символи, числа 12345, та знаки пунктуації! Сподіваюся, приклад відповідає вимогам завдання?"""

    with open("TF4_1.txt", "w", encoding="utf-8") as file:
        file.write(text)

# Етап б: Читання вмісту TF4_1 і підрахунок кількості слів різної довжини
def count_words_by_length():
    word_length_count = defaultdict(int)

    # Читання та обробка тексту з файлу TF4_1
    with open("TF4_1.txt", "r", encoding="utf-8") as file:
        text = file.read()

        # Розбиття тексту на слова
        words = re.findall(r'\b\w+\b', text)

        # Підрахунок слів за довжиною
        for word in words:
            if len(word) <= 16:  # Враховуємо слова довжиною не більше 16 символів
                word_length_count[len(word)] += 1

    # Запис результатів у файл TF4_2
    with open("TF4_2.txt", "w", encoding="utf-8") as file:
        for length in sorted(word_length_count.keys()):
            file.write(f"Слів довжиною {length} символ(ів): {word_length_count[length]}\n")

# Етап в: Читання файлу TF4_2 і виведення його вмісту по рядках
def print_word_lengths():
    with open("TF4_2.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(line.strip())

# Запуск усіх етапів програми
create_text_file()
count_words_by_length()
print_word_lengths()
