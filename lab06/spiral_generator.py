#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Генератор для обхода матрицы по спирали, начиная с центра.
Вариант 12 лабораторной работы №6
"""


def spiral_from_center(matrix):
    """
    Генератор, который обходит элементы матрицы по спирали, начиная с центра.
    
    Args:
        matrix: Квадратная матрица нечётного размера (3x3, 5x5, 7x7, ...)
        
    Yields:
        tuple: (строка, столбец, значение) для каждого элемента в порядке обхода
        
    Raises:
        ValueError: Если матрица не квадратная или имеет чётный размер
        
    Пример:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> list(spiral_from_center(matrix))
        [(1, 1, 5), (1, 2, 6), (0, 2, 3), (0, 1, 2), (0, 0, 1), (1, 0, 4), (2, 0, 7), (2, 1, 8), (2, 2, 9)]
    """
    # Проверка: матрица должна быть квадратной
    if not matrix or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("Матрица должна быть квадратной")
    
    n = len(matrix)
    
    # Проверка: размер должен быть нечётным
    if n % 2 == 0:
        raise ValueError("Матрица должна быть нечётного размера (3x3, 5x5, 7x7, ...)")
    
    if n == 0:
        return
    
    center = n // 2
    row, col = center, center
    
    # Первый элемент (центр)
    yield row, col, matrix[row][col]
    
    # Длина текущего шага: 1, 1, 2, 2, 3, 3, 4, 4, ...
    step_length = 1
    # Направления: право, вверх, влево, вниз
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    
    while True:
        for idx, (dr, dc) in enumerate(directions):
            for _ in range(step_length):
                row += dr
                col += dc
                # Проверяем границы
                if 0 <= row < n and 0 <= col < n:
                    yield row, col, matrix[row][col]
                else:
                    return  # вышли за границы - завершаем
            # После каждых двух направлений увеличиваем длину шага
            if idx % 2 == 1:
                step_length += 1


def spiral_values(matrix):
    """
    Генератор, возвращающий только значения элементов в спиральном порядке.
    
    Args:
        matrix: Квадратная матрица нечётного размера
        
    Yields:
        Значение элемента
        
    Пример:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> list(spiral_values(matrix))
        [5, 6, 3, 2, 1, 4, 7, 8, 9]
    """
    for _, _, value in spiral_from_center(matrix):
        yield value


def spiral_coordinates(matrix):
    """
    Генератор, возвращающий только координаты (строка, столбец) в спиральном порядке.
    
    Args:
        matrix: Квадратная матрица нечётного размера
        
    Yields:
        tuple: (строка, столбец)
    """
    for row, col, _ in spiral_from_center(matrix):
        yield row, col