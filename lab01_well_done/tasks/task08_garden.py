#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)

# все виды цветов
all_flowers = garden_set.union(meadow_set)

# цветы, которые растут и там и там
both_places = garden_set.intersection(meadow_set)

# цветы, которые растут в саду, но не растут на лугу
only_garden = garden_set.difference(meadow_set)

# цветы, которые растут на лугу, но не растут в саду
only_meadow = meadow_set.difference(garden_set)


def run():
    """Функция для запуска задания из верхнеуровневого модуля"""
    print(f"Все виды цветов: {all_flowers}")
    print(f"Растут и в саду, и на лугу: {both_places}")
    print(f"Только в саду: {only_garden}")
    print(f"Только на лугу: {only_meadow}")


if __name__ == "__main__":
    run()