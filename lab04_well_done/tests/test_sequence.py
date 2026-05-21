#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для рекуррентной последовательности."""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import (
    a_recursive_v1,
    a_recursive_v2,
    a_iterative_v1,
    a_iterative_v2,
    a_fast,
    a,
    get_sequence,
    verify_sequence_formula
)


class TestSequence:
    """Тесты для рекуррентной последовательности."""
    
    def test_base_case(self):
        """Тест базового случая."""
        assert a(1) == 1
    
    def test_first_values(self):
        """Тест первых значений."""
        expected = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683]
        for k, exp in enumerate(expected, start=1):
            assert a(k) == exp
    
    def test_formula(self):
        """Тест формулы a_k = 3^(k-1)."""
        for k in range(1, 20):
            assert a(k) == 3 ** (k - 1)
    
    def test_get_sequence(self):
        """Тест получения последовательности."""
        assert get_sequence(1) == [1]
        assert get_sequence(3) == [1, 3, 9]
        assert get_sequence(5) == [1, 3, 9, 27, 81]
    
    def test_consistency(self):
        """Тест согласованности разных версий."""
        for k in range(1, 15):
            v1 = a_iterative_v1(k)
            v2 = a_iterative_v2(k)
            v3 = a_fast(k)
            assert v1 == v2 == v3
    
    def test_large_k(self):
        """Тест для больших k."""
        # Проверяем, что функция работает с большими числами
        result = a(100)
        assert result > 0
        assert len(str(result)) > 47  # 3^99 имеет 48 цифр


if __name__ == "__main__":
    pytest.main([__file__, "-v"])