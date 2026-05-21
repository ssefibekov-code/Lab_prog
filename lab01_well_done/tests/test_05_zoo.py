#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для задания 05_zoo.py"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from tasks import task05_zoo as task


def test_zoo_length():
    """Проверка количества животных."""
    task.run()
    assert len(task.zoo) == 7


def test_elephant_removed():
    """Проверка, что слона удалили."""
    task.run()
    assert 'elephant' not in task.zoo


def test_birds_added():
    """Проверка, что птицы добавлены."""
    task.run()
    assert 'rooster' in task.zoo
    assert 'ostrich' in task.zoo
    assert 'lark' in task.zoo


def test_lion_cage():
    """Проверка номера клетки льва."""
    task.run()
    assert task.lion_index == task.zoo.index('lion') + 1