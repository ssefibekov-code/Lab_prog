#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для задания 06_songs_list.py"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from tasks import task06_songs_list as task


def test_total_time_from_list():
    """Проверка времени трёх песен из списка."""
    task.run()
    expected = 4.9 + 4.20 + 5.83
    assert abs(task.total_time_rounded - expected) < 0.01


def test_total_time_from_dict():
    """Проверка времени трёх песен из словаря."""
    task.run()
    expected = 4.43 + 4.88 + 4.18
    assert abs(task.other_total_rounded - expected) < 0.01