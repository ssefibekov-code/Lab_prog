#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль из лабораторной работы №6 - Генераторы
Вариант 12: Спиральный обход матрицы от центра
"""


def spiral_from_center(matrix):
    """
    Генератор для обхода матрицы по спирали, начиная с центра.
    
    Args:
        matrix: Квадратная матрица нечётного размера
        
    Yields:
        tuple: (строка, столбец, значение)
        
    Raises:
        ValueError: Если матрица не квадратная или имеет чётный размер
        
    Пример:
        >>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
        >>> list(spiral_from_center(matrix))
        [(1,1,5), (1,2,6), (0,2,3), (0,1,2), (0,0,1), (1,0,4), (2,0,7), (2,1,8), (2,2,9)]
    """
    # Проверка: матрица должна быть квадратной
    if not matrix or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("Матрица должна быть квадратной")
    
    n = len(matrix)
    
    # Проверка: размер должен быть нечётным
    if n % 2 == 0:
        raise ValueError("Матрица должна быть нечётного размера (3x3, 5x5, 7x7, ...)")
    
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
                    return  # вышли за границы
            # После двух направлений увеличиваем длину шага
            if idx % 2 == 1:
                step_length += 1


def spiral_values(matrix):
    """
    Генератор, возвращающий только значения элементов в спиральном порядке.
    
    Args:
        matrix: Квадратная матрица нечётного размера
        
    Yields:
        Значение элемента
    """
    for _, _, value in spiral_from_center(matrix):
        yield value


def spiral_coordinates(matrix):
    """
    Генератор, возвращающий только координаты в спиральном порядке.
    
    Args:
        matrix: Квадратная матрица нечётного размера
        
    Yields:
        tuple: (строка, столбец)
    """
    for row, col, _ in spiral_from_center(matrix):
        yield row, col


def create_matrix(size: int, fill_value=None):
    """
    Создаёт квадратную матрицу нечётного размера.
    
    Args:
        size: Размер матрицы (должен быть нечётным)
        fill_value: Значение для заполнения (по умолчанию - последовательные числа)
        
    Returns:
        list: Квадратная матрица
    """
    if size % 2 == 0:
        raise ValueError("Размер матрицы должен быть нечётным")
    
    if fill_value is None:
        # Заполняем числами от 1 до size*size
        return [[i * size + j + 1 for j in range(size)] for i in range(size)]
    else:
        return [[fill_value for _ in range(size)] for _ in range(size)]


# ========== ДЕМОНСТРАЦИЯ ==========

def demo():
    """Демонстрация работы модуля."""
    print("=" * 50)
    print("ГЕНЕРАТОРЫ (ЛР6)")
    print("=" * 50)
    
    print("\n1. Спиральный обход матрицы 3x3:")
    matrix_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    result = list(spiral_from_center(matrix_3x3))
    for r, c, v in result:
        print(f"   ({r}, {c}) -> {v}")
    
    print("\n2. Спиральный обход матрицы 5x5 (первые 10 элементов):")
    matrix_5x5 = create_matrix(5)
    
    for i, (r, c, v) in enumerate(spiral_from_center(matrix_5x5)):
        if i < 10:
            print(f"   ({r}, {c}) -> {v:2d}")
        else:
            print(f"   ... и ещё {25 - i} элементов")
            break
    
    print(f"\n   Всего элементов: {len(list(spiral_from_center(matrix_5x5)))}")


if __name__ == "__main__":
    demo()