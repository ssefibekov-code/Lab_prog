#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента)
my_family = ['папа', 'мама', 'я', 'брат', 'сестра']

# список списков приблизительного роста членов вашей семьи
my_family_height = [
    ['папа', 189],
    ['мама', 169],
    ['я', 189],
    ['брат', 190],
    ['сестра', 173],
]

# Находим рост отца
father_height = 0
for member in my_family_height:
    if member[0] == 'папа':
        father_height = member[1]
        break

# Общий рост семьи
total_height = 0
for member in my_family_height:
    total_height += member[1]


def run():
    """Функция для запуска задания из верхнеуровневого модуля"""
    print(f"Рост отца - {father_height} см")
    print(f"Общий рост моей семьи - {total_height} см")


if __name__ == "__main__":
    run()