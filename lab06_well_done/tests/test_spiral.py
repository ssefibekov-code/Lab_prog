#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для генератора спирального обхода матрицы."""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from spiral_generator import spiral_from_center, spiral_values, spiral_coordinates
from spiral_generator_parallel import spiral_from_center_parallel, ParallelSpiralGenerator


class TestSpiralGenerator:
    """Тесты для генератора спирального обхода."""
    
    def test_3x3_matrix(self):
        """Тест матрицы 3x3."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = list(spiral_from_center(matrix))
        expected = [(1, 1, 5), (1, 2, 6), (0, 2, 3), (0, 1, 2), 
                    (0, 0, 1), (1, 0, 4), (2, 0, 7), (2, 1, 8), (2, 2, 9)]
        assert result == expected
    
    def test_5x5_center(self):
        """Тест центра матрицы 5x5."""
        matrix = [[i * 5 + j + 1 for j in range(5)] for i in range(5)]
        result = list(spiral_from_center(matrix))
        # Первый элемент должен быть центром
        assert result[0][2] == 13  # центр матрицы 5x5
    
    def test_invalid_even_size(self):
        """Тест матрицы чётного размера."""
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        with pytest.raises(ValueError, match="нечётного размера"):
            list(spiral_from_center(matrix))
    
    def test_1x1_matrix(self):
        """Тест матрицы 1x1."""
        matrix = [[42]]
        result = list(spiral_from_center(matrix))
        assert result == [(0, 0, 42)]
    
    def test_spiral_values(self):
        """Тест получения только значений."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = list(spiral_values(matrix))
        assert result == [5, 6, 3, 2, 1, 4, 7, 8, 9]
    
    def test_spiral_coordinates(self):
        """Тест получения только координат."""
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = list(spiral_coordinates(matrix))
        expected = [(1, 1), (1, 2), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
        assert result == expected
    
    def test_all_elements_visited(self):
        """Тест посещения всех элементов."""
        size = 5
        matrix = [[i * size + j + 1 for j in range(size)] for i in range(size)]
        result = list(spiral_from_center(matrix))
        assert len(result) == size * size
    
    def test_parallel_vs_sequential_count(self):
        """Тест: параллельная версия возвращает то же количество элементов."""
        size = 11
        matrix = [[i * size + j + 1 for j in range(size)] for i in range(size)]
        
        seq_result = list(spiral_from_center(matrix))
        par_result = list(spiral_from_center_parallel(matrix, True))
        
        assert len(seq_result) == len(par_result)
    
    def test_string_matrix(self):
        """Тест матрицы строковых элементов."""
        matrix = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        result = list(spiral_from_center(matrix))
        assert result[0][2] == "E"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])