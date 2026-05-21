#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение площади этого круга с точностью до 4-х знаков после запятой
pi = 3.1415926
area = pi * (radius ** 2)
area_rounded = round(area, 4)

# Координаты точек
point_1 = (23, 34)
point_2 = (30, 30)

# Вычисление расстояний и проверка попадания в круг
x1, y1 = point_1
distance_1 = (x1 ** 2 + y1 ** 2) ** 0.5
is_inside_1 = distance_1 <= radius

x2, y2 = point_2
distance_2 = (x2 ** 2 + y2 ** 2) ** 0.5
is_inside_2 = distance_2 <= radius


def run():
    """Функция для запуска задания из верхнеуровневого модуля"""
    print(f"Площадь круга (радиус {radius}): {area_rounded}")
    print(f"Точка {point_1} внутри круга? {is_inside_1}")
    print(f"Точка {point_2} внутри круга? {is_inside_2}")


if __name__ == "__main__":
    run()