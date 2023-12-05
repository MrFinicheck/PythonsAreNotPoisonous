#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Ввести строку.
    user_input = input("Введите предложение: ")

    # Указать гласные.
    vowels = {'а', 'е', 'ё', 'и', 'о', 'у',
              'ы', 'э', 'ю', 'я', 'a', 'e',
              'i', 'o', 'u'}

    # Инициализировать счетчик.
    count = 0
    for char in user_input:
        # Посчитать количество гласных.
        if char.lower() in vowels:
            count += 1

    # Вывести количество гласных.
    print(f"Количество гласных: {count}")








