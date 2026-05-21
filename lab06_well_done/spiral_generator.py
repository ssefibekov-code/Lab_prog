#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Генератор для обхода матрицы по спирали от центра (Вариант 12)
Исходная версия
"""


def spiral_from_center(matrix):
    """
    Генератор, который обходит элементы матрицы по спирали, начиная с центра.
    
    Args:
        matrix: Квадратная матрица нечётного размера (3x3, 5x5, ...)
        
    Yields:
        tuple: (строка, столбец, значение) для каждого элемента в порядке обхода
    """
    n = len(matrix)
    if n % 2 == 0:
        raise ValueError("Матрица должна быть нечётного размера (3x3, 5x5, ...)")

    center = n // 2
    row, col = center, center

    # Первый элемент (центр)
    yield row, col, matrix[row][col]

    # Длина текущего шага: 1, 1, 2, 2, 3, 3, 4, 4, ...
    step_length = 1
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # право, вверх, влево, вниз

    while True:
        for idx, (dr, dc) in enumerate(directions):
            for _ in range(step_length):
                row += dr
                col += dc
                if 0 <= row < n and 0 <= col < n:
                    yield row, col, matrix[row][col]
                else:
                    return
            # После двух направлений увеличиваем длину шага
            if idx % 2 == 1:
                step_length += 1


def spiral_values(matrix):
    """Генератор, возвращающий только значения."""
    for _, _, value in spiral_from_center(matrix):
        yield value


def spiral_coordinates(matrix):
    """Генератор, возвращающий только координаты."""
    for row, col, _ in spiral_from_center(matrix):
        yield row, col