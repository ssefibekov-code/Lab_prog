#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Фикстуры pytest для лабораторной работы №1
"""

import pytest
import sys
import os

# Добавляем пути для импорта
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture
def sample_list():
    """Фикстура с примером списка для линеаризации."""
    return [1, 2, [3, 4, [5, [6, []]]]]


@pytest.fixture
def sample_matrix():
    """Фикстура с примером матрицы."""
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]