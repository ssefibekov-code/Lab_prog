#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для задания 02_operations.py"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from tasks import task02_operations as task


def test_result_value():
    """Проверка, что результат равен 25."""
    task.run()
    assert task.result == 25


def test_result_type():
    """Проверка типа результата."""
    assert isinstance(task.result, int)