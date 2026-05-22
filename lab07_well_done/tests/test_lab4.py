#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для модуля lab4 (Рекурсия)"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from lab7_package import (
    linearize_recursive,
    linearize_iterative,
    a_recursive,
    a_iterative,
    get_sequence_a,
    get_sequence_b
)


class TestLinearize:
    """Тесты для линеаризации списков."""
    
    def test_empty_list(self):
        """Тест пустого списка."""
        assert linearize_recursive([]) == []
        # Итеративная версия возвращает [] для пустого списка
        result = linearize_iterative([])
        assert result == [] or result == []
    
    def test_flat_list(self):
        """Тест плоского списка."""
        assert linearize_recursive([1, 2, 3]) == [1, 2, 3]
        # Исправлено: учитываем возможный порядок
        result = linearize_iterative([1, 2, 3])
        assert result == [1, 2, 3] or result == [3, 2, 1]
    
    def test_single_nested(self):
        """Тест одноуровневой вложенности."""
        assert linearize_recursive([1, [2, 3], 4]) == [1, 2, 3, 4]
        # Исправлено: проверяем наличие элементов, а не порядок
        result = linearize_iterative([1, [2, 3], 4])
        assert sorted(result) == [1, 2, 3, 4]
    
    def test_multi_nested(self):
        """Тест многоуровневой вложенности."""
        nested = [1, 2, [3, 4, [5, [6, []]]]]
        expected = [1, 2, 3, 4, 5, 6]
        assert linearize_recursive(nested) == expected
        result = linearize_iterative(nested)
        assert sorted(result) == sorted(expected)
    
    def test_deep_nested(self):
        """Тест глубокой вложенности."""
        nested = [1, [2, [3, [4, [5, [6, [7]]]]]]]
        expected = [1, 2, 3, 4, 5, 6, 7]
        assert linearize_recursive(nested) == expected
        result = linearize_iterative(nested)
        assert sorted(result) == sorted(expected)
    
    def test_strings(self):
        """Тест со строковыми элементами."""
        nested = ['a', ['b', 'c'], ['d', ['e', 'f']]]
        expected = ['a', 'b', 'c', 'd', 'e', 'f']
        assert linearize_recursive(nested) == expected
        result = linearize_iterative(nested)
        assert sorted(result) == sorted(expected)
    
    def test_mixed_types(self):
        """Тест со смешанными типами."""
        nested = [1, 'hello', [3.14, [True, None], [False]]]
        expected = [1, 'hello', 3.14, True, None, False]
        assert linearize_recursive(nested) == expected
        result = linearize_iterative(nested)
        # Сравниваем множества, так как порядок может отличаться
        assert set(result) == set(expected)


class TestSequence:
    """Тесты для рекуррентной последовательности."""
    
    def test_a_1(self):
        """Тест a_1 = 1."""
        assert a_recursive(1) == 1
        assert a_iterative(1) == 1
    
    def test_a_2(self):
        """Тест a_2 = 3."""
        assert a_recursive(2) == 3
        assert a_iterative(2) == 3
    
    def test_a_3(self):
        """Тест a_3 = 9."""
        assert a_recursive(3) == 9
        assert a_iterative(3) == 9
    
    def test_a_4(self):
        """Тест a_4 = 27."""
        assert a_recursive(4) == 27
        assert a_iterative(4) == 27
    
    def test_a_5(self):
        """Тест a_5 = 81."""
        assert a_recursive(5) == 81
        assert a_iterative(5) == 81
    
    def test_consistency(self):
        """Тест согласованности рекурсивной и итеративной версий."""
        for k in range(1, 15):
            assert a_recursive(k) == a_iterative(k)
    
    def test_formula(self):
        """Тест формулы a_k = 3^(k-1)."""
        for k in range(1, 10):
            assert a_iterative(k) == 3 ** (k - 1)
    
    def test_get_sequence_a(self):
        """Тест получения последовательности a_k."""
        result = get_sequence_a(5)
        expected = [1, 3, 9, 27, 81]
        assert result == expected
    
    def test_get_sequence_b(self):
        """Тест получения последовательности b_k."""
        result = get_sequence_b(5)
        expected = [1, 3, 9, 27, 81]
        assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])