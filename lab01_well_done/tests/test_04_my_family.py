#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для задания 04_my_family.py"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from tasks import task04_my_family as task


def test_father_height():
    """Проверка роста отца."""
    task.run()
    assert task.father_height == 189


def test_total_height():
    """Проверка общего роста семьи."""
    task.run()
    expected = 189 + 169 + 189 + 190 + 173
    assert task.total_height == expected


def test_family_size():
    """Проверка размера семьи."""
    assert len(task.my_family) >= 3