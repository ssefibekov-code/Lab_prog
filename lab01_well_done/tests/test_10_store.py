#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для задания 10_store.py"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from tasks import task10_store as task


def test_lamp_cost():
    """Проверка стоимости ламп."""
    task.run()
    expected = 27 * 42
    assert task.lamp_cost == expected


def test_table_cost():
    """Проверка стоимости столов."""
    task.run()
    expected = 22 * 510 + 32 * 520
    assert task.table_cost == expected


def test_sofa_cost():
    """Проверка стоимости диванов."""
    task.run()
    expected = 2 * 1200 + 1 * 1150
    assert task.sofa_cost == expected


def test_chair_cost():
    """Проверка стоимости стульев."""
    task.run()
    expected = 50 * 100 + 12 * 95 + 43 * 97
    assert task.chair_cost == expected