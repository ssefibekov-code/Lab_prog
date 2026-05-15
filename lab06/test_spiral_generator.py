#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Тесты для генератора спирального обхода матрицы (Вариант 12)
Уровень Medium - pytest тесты
"""

import pytest
from spiral_generator import spiral_from_center, spiral_values, spiral_coordinates


# ============================================================
# ТЕСТЫ ДЛЯ ПРОВЕРКИ ВАЛИДАЦИИ ВХОДНЫХ ДАННЫХ
# ============================================================

def test_invalid_empty_matrix():
    """Тест: пустая матрица должна вызывать ошибку."""
    with pytest.raises(ValueError, match="Матрица должна быть квадратной"):
        list(spiral_from_center([]))


def test_invalid_non_square_matrix():
    """Тест: неквадратная матрица должна вызывать ошибку."""
    matrix = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError, match="Матрица должна быть квадратной"):
        list(spiral_from_center(matrix))


def test_invalid_even_size_matrix():
    """Тест: матрица чётного размера должна вызывать ошибку."""
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    with pytest.raises(ValueError, match="Матрица должна быть нечётного размера"):
        list(spiral_from_center(matrix))


# ============================================================
# ТЕСТЫ ДЛЯ МАТРИЦЫ 3x3
# ============================================================

def test_3x3_matrix_order():
    """Тест: проверка порядка обхода матрицы 3x3."""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    expected = [
        (1, 1, 5),  # центр
        (1, 2, 6),  # право
        (0, 2, 3),  # вверх
        (0, 1, 2),  # влево
        (0, 0, 1),  # влево
        (1, 0, 4),  # вниз
        (2, 0, 7),  # вниз
        (2, 1, 8),  # право
        (2, 2, 9),  # право
    ]
    
    result = list(spiral_from_center(matrix))
    assert result == expected


def test_3x3_matrix_values():
    """Тест: получение только значений для матрицы 3x3."""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    expected_values = [5, 6, 3, 2, 1, 4, 7, 8, 9]
    result = list(spiral_values(matrix))
    assert result == expected_values


def test_3x3_matrix_coordinates():
    """Тест: получение только координат для матрицы 3x3."""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    expected_coords = [(1, 1), (1, 2), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    result = list(spiral_coordinates(matrix))
    assert result == expected_coords


def test_3x3_matrix_count():
    """Тест: количество элементов для матрицы 3x3."""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = list(spiral_from_center(matrix))
    assert len(result) == 9  # 3x3 = 9 элементов


# ============================================================
# ТЕСТЫ ДЛЯ МАТРИЦЫ 5x5
# ============================================================

def test_5x5_matrix_count():
    """Тест: количество элементов для матрицы 5x5."""
    matrix = [[i * 5 + j + 1 for j in range(5)] for i in range(5)]
    result = list(spiral_from_center(matrix))
    assert len(result) == 25  # 5x5 = 25 элементов


def test_5x5_center_first():
    """Тест: первым должен быть центральный элемент."""
    matrix = [[i * 5 + j + 1 for j in range(5)] for i in range(5)]
    center = 2, 2  # индекс центра
    expected_center_value = matrix[center[0]][center[1]]
    
    result = list(spiral_from_center(matrix))
    assert result[0][0] == center[0]
    assert result[0][1] == center[1]
    assert result[0][2] == expected_center_value


def test_5x5_last_element():
    """Тест: последним должен быть правый нижний угол."""
    matrix = [[i * 5 + j + 1 for j in range(5)] for i in range(5)]
    last_expected = (4, 4, 25)  # правый нижний угол
    
    result = list(spiral_from_center(matrix))
    assert result[-1] == last_expected


# ============================================================
# ТЕСТЫ ДЛЯ МАТРИЦЫ 1x1
# ============================================================

def test_1x1_matrix():
    """Тест: матрица 1x1."""
    matrix = [[42]]
    result = list(spiral_from_center(matrix))
    assert result == [(0, 0, 42)]
    assert len(result) == 1


def test_1x1_values():
    """Тест: значения для матрицы 1x1."""
    matrix = [[100]]
    result = list(spiral_values(matrix))
    assert result == [100]


# ============================================================
# ТЕСТЫ ДЛЯ МАТРИЦЫ С РАЗНЫМИ ТИПАМИ ДАННЫХ
# ============================================================

def test_string_matrix():
    """Тест: матрица строковых элементов."""
    matrix = [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"]
    ]
    
    expected = ["E", "F", "C", "B", "A", "D", "G", "H", "I"]
    result = list(spiral_values(matrix))
    assert result == expected


def test_float_matrix():
    """Тест: матрица вещественных чисел."""
    matrix = [
        [1.1, 2.2, 3.3],
        [4.4, 5.5, 6.6],
        [7.7, 8.8, 9.9]
    ]
    
    result = list(spiral_values(matrix))
    assert result[0] == 5.5  # центр
    assert len(result) == 9


def test_mixed_types_matrix():
    """Тест: матрица со смешанными типами."""
    matrix = [
        [1, "two", 3],
        [4, 5, 6.6],
        [None, 8, "nine"]
    ]
    
    result = list(spiral_from_center(matrix))
    assert len(result) == 9
    
    # Центр матрицы (1, 1) = 5
    assert result[0][2] == 5
    
    # Право от центра (1, 2) = 6.6
    assert result[1][2] == 6.6
    
    # Вверх-вправо (0, 2) = 3
    assert result[2][2] == 3
    
    # Вверх (0, 1) = "two"
    assert result[3][2] == "two"
    
    # Вверх-влево (0, 0) = 1
    assert result[4][2] == 1
    
    # Вниз-влево (1, 0) = 4
    assert result[5][2] == 4
    
    # Вниз (2, 0) = None
    assert result[6][2] is None
    
    # Вниз-вправо (2, 1) = 8
    assert result[7][2] == 8
    
    # Вниз-вправо (2, 2) = "nine"
    assert result[8][2] == "nine"


# ============================================================
# ТЕСТЫ ДЛЯ ПРОВЕРКИ НЕЗАВИСИМОСТИ ГЕНЕРАТОРОВ
# ============================================================

def test_generators_independence():
    """Тест: разные генераторы должны работать независимо."""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    gen1 = spiral_from_center(matrix)
    gen2 = spiral_from_center(matrix)
    
    # Первый элемент обоих генераторов должен быть одинаковым
    assert next(gen1) == (1, 1, 5)
    assert next(gen2) == (1, 1, 5)
    
    # Второй элемент также должен быть одинаковым
    assert next(gen1) == (1, 2, 6)
    assert next(gen2) == (1, 2, 6)


# ============================================================
# ТЕСТЫ ДЛЯ ПРОВЕРКИ ПРАВИЛЬНОСТИ ОБХОДА
# ============================================================

def test_all_elements_visited():
    """Тест: все элементы матрицы должны быть посещены ровно один раз."""
    matrix = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]
    
    result = list(spiral_from_center(matrix))
    visited_values = [value for _, _, value in result]
    
    # Все значения от 1 до 25 должны быть посещены
    assert sorted(visited_values) == list(range(1, 26))


def test_no_duplicates():
    """Тест: не должно быть повторяющихся элементов."""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = list(spiral_from_center(matrix))
    visited_values = [value for _, _, value in result]
    
    # Все значения уникальны
    assert len(set(visited_values)) == len(visited_values)


# ============================================================
# ТЕСТЫ ДЛЯ БОЛЬШИХ МАТРИЦ
# ============================================================

def test_7x7_matrix():
    """Тест: матрица 7x7 должна содержать 49 элементов."""
    matrix = [[i * 7 + j + 1 for j in range(7)] for i in range(7)]
    result = list(spiral_from_center(matrix))
    assert len(result) == 49


def test_9x9_matrix():
    """Тест: матрица 9x9 должна содержать 81 элемент."""
    matrix = [[i * 9 + j + 1 for j in range(9)] for i in range(9)]
    result = list(spiral_from_center(matrix))
    assert len(result) == 81


# ============================================================
# ЗАПУСК ТЕСТОВ
# ============================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])