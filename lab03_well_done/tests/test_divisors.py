#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для класса DivisorsSolver."""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from classes.divisors_solver import DivisorsSolver, Variant12Divisors


class TestDivisorsSolver:
    """Тесты для DivisorsSolver."""
    
    def test_count_divisors_prime(self):
        """Проверка количества делителей простого числа."""
        assert DivisorsSolver.count_divisors(7) == 2  # 1 и 7
    
    def test_count_divisors_composite(self):
        """Проверка количества делителей составного числа."""
        assert DivisorsSolver.count_divisors(12) == 6  # 1,2,3,4,6,12
        assert DivisorsSolver.count_divisors(48) == 10
    
    def test_get_divisors(self):
        """Проверка получения списка делителей."""
        divisors = DivisorsSolver.get_divisors(12)
        assert divisors == [1, 2, 3, 4, 6, 12]
    
    def test_prime_factorization(self):
        """Проверка разложения на простые множители."""
        factors = DivisorsSolver.prime_factorization(12)
        assert factors == {2: 2, 3: 1}
    
    def test_divisors_count_from_factors(self):
        """Проверка вычисления количества делителей из разложения."""
        factors = {2: 2, 3: 1}
        assert DivisorsSolver.divisors_count_from_factors(factors) == (2+1)*(1+1) == 6
    
    def test_find_max_divisors_number(self):
        """Проверка поиска числа с максимальным количеством делителей."""
        solver = DivisorsSolver(2, 48)
        count, number = solver.find_max_divisors_number()
        assert count == 10  # 48 имеет 10 делителей
        assert number == 48
    
    def test_variant12_solve(self):
        """Проверка решения варианта 12."""
        solver = Variant12Divisors()
        count, number = solver.solve()
        assert isinstance(count, int)
        assert isinstance(number, int)
        assert 84052 <= number <= 84130
        assert count > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])