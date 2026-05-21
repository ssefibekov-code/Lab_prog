#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для задания 09_shopping.py"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from tasks import task09_shopping as task


def test_sweets_structure():
    """Проверка структуры словаря sweets."""
    assert 'печенье' in task.sweets
    assert 'конфеты' in task.sweets
    assert 'карамель' in task.sweets
    assert 'пирожное' in task.sweets


def test_cookie_prices():
    """Проверка цен на печенье."""
    for item in task.sweets['печенье']:
        if item['shop'] == 'пятёрочка':
            assert item['price'] == 9.99