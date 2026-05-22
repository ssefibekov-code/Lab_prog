#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для модуля lab6 (Генераторы)"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from lab7_package import spiral_from_center, get_spiral_order


class TestSpiralGenerator:
    """Тесты для генератора спирального обхода."""
    
    def test_3x3_matrix(self):
        """Тест матрицы 3x3."""
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        
        result = list(spiral_from_center(matrix))
        
        # Проверяем, что первый элемент - центр
        assert result[0][2] == 5
        
        # Проверяем количество элементов
        assert len(result) == 9
        
        # Проверяем, что все элементы посещены
        values = [v for _, _, v in result]
        assert sorted(values) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def test_5x5_center(self):
        """Тест центра матрицы 5x5."""
        size = 5
        matrix = [[i * size + j + 1 for j in range(size)] for i in range(size)]
        result = list(spiral_from_center(matrix))
        
        # Первый элемент должен быть центром
        center_value = matrix[size // 2][size // 2]
        assert result[0][2] == center_value
    
    def test_5x5_count(self):
        """Тест количества элементов матрицы 5x5."""
        size = 5
        matrix = [[i * size + j + 1 for j in range(size)] for i in range(size)]
        result = list(spiral_from_center(matrix))
        assert len(result) == size * size
    
    def test_1x1_matrix(self):
        """Тест матрицы 1x1."""
        matrix = [[42]]
        result = list(spiral_from_center(matrix))
        assert result == [(0, 0, 42)]
    
    def test_empty_matrix(self):
        """Тест пустой матрицы."""
        matrix = []
        result = list(spiral_from_center(matrix))
        assert result == []
    
    def test_get_spiral_order(self):
        """Тест функции get_spiral_order."""
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        
        result = get_spiral_order(matrix)
        values = [v for _, _, v in result]
        
        # Проверяем, что центр на первом месте
        assert values[0] == 5
        
        # Проверяем количество элементов
        assert len(values) == 9
        
        # Проверяем, что все элементы присутствуют
        assert sorted(values) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def test_all_elements_visited(self):
        """Тест посещения всех элементов."""
        size = 7
        matrix = [[i * size + j + 1 for j in range(size)] for i in range(size)]
        result = list(spiral_from_center(matrix))
        
        # Все элементы должны быть посещены
        visited_values = [v for _, _, v in result]
        expected_values = list(range(1, size * size + 1))
        
        assert sorted(visited_values) == expected_values
    
    def test_no_duplicates(self):
        """Тест отсутствия дубликатов."""
        size = 5
        matrix = [[i * size + j + 1 for j in range(size)] for i in range(size)]
        result = list(spiral_from_center(matrix))
        
        visited_values = [v for _, _, v in result]
        assert len(set(visited_values)) == len(visited_values)
    
    def test_string_matrix(self):
        """Тест матрицы строковых элементов."""
        matrix = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]
        
        result = list(spiral_from_center(matrix))
        expected_center = "E"
        
        assert result[0][2] == expected_center
        assert len(result) == 9
    
    def test_float_matrix(self):
        """Тест матрицы вещественных чисел."""
        matrix = [
            [1.1, 2.2, 3.3],
            [4.4, 5.5, 6.6],
            [7.7, 8.8, 9.9]
        ]
        
        result = list(spiral_from_center(matrix))
        assert result[0][2] == 5.5
        assert len(result) == 9
    
    def test_large_matrix(self):
        """Тест большой матрицы 11x11."""
        size = 11
        matrix = [[i * size + j + 1 for j in range(size)] for i in range(size)]
        result = list(spiral_from_center(matrix))
        assert len(result) == size * size


if __name__ == "__main__":
    pytest.main([__file__, "-v"])