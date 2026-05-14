#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# посадите медведя (bear) между львом и кенгуру
zoo.insert(1, 'bear')

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
zoo.extend(birds)

# уберите слона
zoo.remove('elephant')

# находим номера клеток льва и жаворонка
lion_index = zoo.index('lion') + 1
lark_index = zoo.index('lark') + 1


def run():
    """Функция для запуска задания из верхнеуровневого модуля"""
    print(f"Итоговый список животных в зоопарке: {zoo}")
    print(f"Лев сидит в клетке номер {lion_index}")
    print(f"Жаворонок сидит в клетке номер {lark_index}")


if __name__ == "__main__":
    run()