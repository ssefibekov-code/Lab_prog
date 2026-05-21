#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль из лабораторной работы №5 - Замыкания
Вариант 12: Калькулятор с накоплением и декоратор call_limiter
"""

import time
import functools
from typing import Optional, Callable, Any


# ========== ЗАМЫКАНИЕ-КАЛЬКУЛЯТОР ==========

def make_calc(operation: str, initial: float = 0):
    """
    Создаёт замыкание-калькулятор с накоплением результата.
    
    Args:
        operation: Операция ('+', '-', '*', '/')
        initial: Начальное значение
        
    Returns:
        function: Калькулятор, накапливающий результат
        
    Пример:
        >>> calc = make_calc('+', initial=10)
        >>> calc(5)
        15
        >>> calc(3)
        18
    """
    result = initial
    
    def calc(value: float) -> float:
        nonlocal result
        if operation == '+':
            result += value
        elif operation == '-':
            result -= value
        elif operation == '*':
            result *= value
        elif operation == '/':
            if value == 0:
                raise ValueError("Деление на ноль!")
            result /= value
        else:
            raise ValueError(f"Неизвестная операция: {operation}")
        return result
    
    return calc


# ========== ДЕКОРАТОР ДЛЯ ОГРАНИЧЕНИЯ ВЫЗОВОВ ==========

class CallLimitError(Exception):
    """Исключение при превышении лимита вызовов."""
    pass


def call_limiter(max_calls: Optional[int] = None):
    """
    Декоратор, ограничивающий количество одновременных вызовов функции.
    
    Args:
        max_calls: Максимальное количество одновременных вызовов
        
    Returns:
        Декоратор функции
        
    Пример:
        @call_limiter(max_calls=3)
        def test_function():
            print("Функция вызвана")
    """
    def decorator(func: Callable) -> Callable:
        calls = 0
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            nonlocal calls
            if max_calls is not None and calls >= max_calls:
                raise CallLimitError(
                    f"Превышено максимальное количество вызовов ({max_calls})"
                )
            calls += 1
            try:
                return func(*args, **kwargs)
            finally:
                calls -= 1
        
        return wrapper
    return decorator


# ========== ПРИМЕРЫ ДЛЯ ДЕМОНСТРАЦИИ ==========

@call_limiter(max_calls=3)
def limited_function(msg: str) -> str:
    """Функция с ограничением вызовов."""
    return f"Вызов: {msg}"


@call_limiter(max_calls=5)
def factorial(n: int) -> int:
    """Рекурсивная функция с ограничением."""
    if n == 0:
        return 1
    return n * factorial(n - 1)


# ========== ДЕМОНСТРАЦИЯ ==========

def demo():
    """Демонстрация работы модуля."""
    print("=" * 50)
    print("ЗАМЫКАНИЯ (ЛР5)")
    print("=" * 50)
    
    print("\n1. Замыкание-калькулятор:")
    calc_add = make_calc('+', initial=10)
    print(f"   calc = make_calc('+', 10)")
    print(f"   calc(5) = {calc_add(5)}")
    print(f"   calc(3) = {calc_add(3)}")
    
    calc_mul = make_calc('*', initial=2)
    print(f"\n   calc_mul = make_calc('*', 2)")
    print(f"   calc_mul(3) = {calc_mul(3)}")
    print(f"   calc_mul(4) = {calc_mul(4)}")
    
    print("\n2. Декоратор call_limiter:")
    print("   @call_limiter(max_calls=3)")
    
    for i in range(3):
        print(f"   Вызов {i+1}: {limited_function(f'раз {i+1}')}")
    
    try:
        print(f"   Вызов 4: {limited_function('раз 4')}")
    except CallLimitError as e:
        print(f"   Ошибка: {e}")


if __name__ == "__main__":
    demo()