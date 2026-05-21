#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для функции линеаризации списков."""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import (
    linearize_recursive_v1,
    linearize_recursive_v2,
    linearize_iterative_v1,
    linearize_iterative_v2,
    linearize_fast,
    linearize
)


class TestLinearize:
    """Тесты для линеаризации списков."""
    
    def test_empty_list(self):
        """Тест пустого списка."""
        assert linearize([]) == []
    
    def test_flat_list(self):
        """Тест плоского списка."""
        assert linearize([1, 2, 3]) == [1, 2, 3]
    
    def test_single_nested(self):
        """Тест одноуровневой вложенности."""
        assert linearize([1, [2, 3], 4]) == [1, 2, 3, 4]
    
    def test_multi_nested(self):
        """Тест многоуровневой вложенности."""
        nested = [1, 2, [3, 4, [5, [6, []]]]]
        expected = [1, 2, 3, 4, 5, 6]
        assert linearize(nested) == expected
    
    def test_deep_nested(self):
        """Тест глубокой вложенности."""
        nested = [1, [2, [3, [4, [5, [6, [7]]]]]]]
        expected = [1, 2, 3, 4, 5, 6, 7]
        assert linearize(nested) == expected
    
    def test_strings(self):
        """Тест со строковыми элементами."""
        nested = ['a', ['b', 'c'], ['d', ['e', 'f']]]
        expected = ['a', 'b', 'c', 'd', 'e', 'f']
        assert linearize(nested) == expected
    
    def test_mixed_types(self):
        """Тест со смешанными типами."""
        nested = [1, 'hello', [3.14, [True, None], [False]]]
        expected = [1, 'hello', 3.14, True, None, False]
        assert linearize(nested) == expected
    
    def test_large_list(self):
        """Тест большого списка."""
        # Создаём глубоко вложенный список
        nested = list(range(100))
        for i in range(100):
            nested = [nested]
        result = linearize(nested)
        assert len(result) == 100
        assert result == list(range(100))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])