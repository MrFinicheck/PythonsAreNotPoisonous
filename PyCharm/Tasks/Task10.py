#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Ввести две строки.
    sentence1 = set(input("Введите первую строку: "))
    sentence2 = set(input("Введите вторую строку: "))

    # Найти общие элементы.
    inter_sentence = sentence1.intersection(sentence2)

    # Вывести общие символы у двух строк.
    print(f"Общие символы у двух строк: {inter_sentence}")



    