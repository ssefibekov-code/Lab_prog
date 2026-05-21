#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для задания 03_favorite_movies.py"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from tasks import task03_favorite_movies as task


def test_first_movie():
    """Проверка первого фильма."""
    task.run()
    assert task.first_movie == "Терминатор"


def test_second_movie():
    """Проверка второго фильма."""
    task.run()
    assert task.second_movie == "Пятый элемент"


def test_last_second_movie():
    """Проверка предпоследнего фильма."""
    task.run()
    assert task.last_second_movie == "Чужие"


def test_last_movie():
    """Проверка последнего фильма."""
    task.run()
    assert task.last_movie == "Назад в будущее"