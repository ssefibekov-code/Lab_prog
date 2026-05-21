#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для задания 01_circle.py"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from tasks import task01_circle as task


def test_area():
    """Проверка площади круга."""
    task.run()
    expected = 5541.7693  # Реальное значение из вашей программы
    assert abs(task.area_rounded - expected) < 0.0001


def test_point_1_inside():
    """Проверка, что точка (23,34) внутри круга."""
    task.run()
    assert task.is_inside_1 is True


def test_point_2_inside():
    """Проверка, что точка (30,30) вне круга."""
    task.run()
    assert task.is_inside_2 is False


def test_radius_value():
    """Проверка значения радиуса."""
    assert task.radius == 42