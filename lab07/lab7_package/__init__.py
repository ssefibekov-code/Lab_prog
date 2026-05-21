#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Пакет, объединяющий лабораторные работы №4, №5, №6

Модули:
    - recursion_module: рекурсивные и итеративные функции (ЛР4)
    - closure_module: замыкания и декораторы (ЛР5)
    - generator_module: генератор спирального обхода матрицы (ЛР6)
"""

from . import recursion_module
from . import closure_module
from . import generator_module

__all__ = ['recursion_module', 'closure_module', 'generator_module']