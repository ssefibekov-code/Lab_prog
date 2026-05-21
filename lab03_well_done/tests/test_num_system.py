#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для класса NumSystemSolver."""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from classes.num_system_solver import NumSystemSolver, Variant12NumSystem


class TestNumSystemSolver:
    """Тесты для NumSystemSolver."""
    
    def test_evaluate_simple(self):
        """Проверка вычисления простого выражения."""
        solver = NumSystemSolver("2 + 2", 10)
        assert solver.evaluate() == 4
    
    def test_to_base_binary(self):
        """Проверка перевода в двоичную систему."""
        solver = NumSystemSolver("5", 2)
        assert solver.to_base(5) == "101"
    
    def test_to_base_octal(self):
        """Проверка перевода в восьмеричную систему."""
        solver = NumSystemSolver("8", 8)
        assert solver.to_base(8) == "10"
    
    def test_count_digit(self):
        """Проверка подсчёта цифр."""
        solver = NumSystemSolver("5", 2)
        assert solver.count_digit('1') == 2  # 101 -> две единицы
    
    def test_count_zeros(self):
        """Проверка подсчёта нулей."""
        solver = NumSystemSolver("8", 8)
        assert solver.count_zeros() == 1  # 10 -> один ноль
    
    def test_variant12_solve(self):
        """Проверка решения варианта 12."""
        solver = Variant12NumSystem()
        # Значение должно быть целым числом
        assert isinstance(solver.solve(), int)
        assert solver.solve() > 0
    
    def test_get_digit_statistics(self):
        """Проверка статистики по цифрам."""
        solver = NumSystemSolver("8", 8)
        stats = solver.get_digit_statistics()
        assert '1' in stats
        assert '0' in stats


if __name__ == "__main__":
    pytest.main([__file__, "-v"])