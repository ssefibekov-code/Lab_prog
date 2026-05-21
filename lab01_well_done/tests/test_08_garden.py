#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для задания 08_garden.py"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from tasks import task08_garden as task


def test_both_places():
    """Проверка цветов, растущих везде."""
    task.run()
    expected = set(task.garden) & set(task.meadow)
    assert task.both_places == expected


def test_only_garden():
    """Проверка цветов, растущих только в саду."""
    task.run()
    expected = set(task.garden) - set(task.meadow)
    assert task.only_garden == expected