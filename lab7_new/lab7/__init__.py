"""
Пакет lab7 - объединение лабораторных работ №4, №5, №6
"""

from .lab4 import *
from .lab5 import *
from .lab6 import *

__all__ = [
    'linearize_recursive',
    'linearize_iterative', 
    'a_recursive',
    'a_iterative',
    'make_calc',
    'call_limiter',
    'log_decorator',
    'spiral_from_center',
    'get_spiral_order',
]