#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для класса CombinatoricsSolver."""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from classes.combinatorics_solver import CombinatoricsSolver, Variant12Combinatorics


class TestCombinatoricsSolver:
    """Тесты для CombinatoricsSolver."""
    
    def test_total_combinations(self):
        """Проверка общего количества комбинаций."""
        solver = CombinatoricsSolver(['A', 'B'], 3)
        assert solver.total_combinations() == 8  # 2^3 = 8
    
    def test_combinations_without_letter(self):
        """Проверка комбинаций без буквы."""
        solver = CombinatoricsSolver(['A', 'B', 'C'], 2, 'A')
        assert solver.combinations_without_letter('A') == 4  # 2^2 = 4
    
    def test_count_codes_with_required_letter(self):
        """Проверка подсчёта кодов с обязательной буквой."""
        solver = CombinatoricsSolver(['A', 'B'], 2, 'A')
        # Всего: 4 (AA, AB, BA, BB)
        # Без A: 1 (BB)
        # С A: 4 - 1 = 3
        assert solver.count_codes_with_required_letter() == 3
    
    def test_variant12_solve(self):
        """Проверка решения варианта 12."""
        solver = Variant12Combinatorics()
        assert solver.solve() == 781  # 4^5 - 3^5 = 1024 - 243 = 781
    
    def test_generate_all_codes(self):
        """Проверка генерации всех кодов."""
        solver = CombinatoricsSolver(['A', 'B'], 2)
        codes = solver.generate_all_codes()
        assert len(codes) == 4
        assert ('A', 'A') in codes
        assert ('A', 'B') in codes
        assert ('B', 'A') in codes
        assert ('B', 'B') in codes


if __name__ == "__main__":
    pytest.main([__file__, "-v"])