#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для задания 00_distance.py"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from tasks import task00_distance as task


def test_distances_structure():
    """Проверка структуры словаря расстояний."""
    task.run()
    assert hasattr(task, 'distances')
    assert 'Moscow' in task.distances
    assert 'London' in task.distances
    assert 'Paris' in task.distances


def test_moscow_to_london():
    """Проверка расстояния Москва-Лондон."""
    task.run()
    expected = 145.6  # Реальное значение из вашей программы
    assert abs(task.distances['Moscow']['London'] - expected) < 0.01


def test_moscow_to_paris():
    """Проверка расстояния Москва-Париж."""
    task.run()
    expected = 130.38  # Реальное значение из вашей программы
    assert abs(task.distances['Moscow']['Paris'] - expected) < 0.01


def test_london_to_paris():
    """Проверка расстояния Лондон-Париж."""
    task.run()
    expected = 42.43  # Реальное значение из вашей программы
    assert abs(task.distances['London']['Paris'] - expected) < 0.01


def test_symmetry():
    """Проверка симметрии расстояний."""
    task.run()
    assert task.distances['Moscow']['London'] == task.distances['London']['Moscow']
    assert task.distances['Moscow']['Paris'] == task.distances['Paris']['Moscow']
    assert task.distances['London']['Paris'] == task.distances['Paris']['London']