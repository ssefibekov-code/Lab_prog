#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Лабораторная работа №5 - Замыкания (Вариант 12)
Уровень Well-done: декоратор классов вместо декоратора функций

Задачи:
1. Замыкание для получения простых чисел
2. Декоратор-класс для ограничения времени выполнения функции
"""

import time
import functools
from typing import Optional, Callable, Any, List


# ============================================================
# ЗАДАЧА 1: ЗАМЫКАНИЕ ДЛЯ ПОЛУЧЕНИЯ ПРОСТЫХ ЧИСЕЛ
# ============================================================

def make_prime_generator():
    """
    Замыкание для генерации простых чисел.
    
    Returns:
        function: Функция, которая при каждом вызове возвращает следующее простое число
    """
    primes_found: List[int] = []
    current: int = 2
    
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for p in primes_found:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True
    
    def get_next_prime() -> int:
        nonlocal current
        while not is_prime(current):
            current += 1
        result = current
        primes_found.append(result)
        current += 1
        return result
    
    return get_next_prime


# ============================================================
# ЗАДАЧА 2: ДЕКОРАТОР-КЛАСС (Well-done)
# ============================================================

class TimeoutError(Exception):
    """Исключение при превышении лимита времени."""
    pass


class timeout:
    """
    Декоратор-класс для ограничения времени выполнения функции.
    
    Примеры:
        @timeout(limit=2)
        def slow_function():
            time.sleep(3)  # Вызовет TimeoutError
        
        @timeout()  # Без ограничения
        def fast_function():
            return 42
    """
    
    def __init__(self, limit: Optional[float] = None):
        self.limit = limit
    
    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time
            
            if self.limit is not None and self.limit > 0 and elapsed > self.limit:
                raise TimeoutError(
                    f"Функция '{func.__name__}' выполнялась {elapsed:.2f} сек, "
                    f"что превышает лимит {self.limit} сек"
                )
            return result
        
        return wrapper


# ============================================================
# ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ
# ============================================================

def demo_prime_generator():
    """Демонстрация работы генератора простых чисел."""
    print("\n" + "=" * 60)
    print("ЗАМЫКАНИЕ: Генератор простых чисел")
    print("=" * 60)
    
    primes = make_prime_generator()
    
    print("\nПервые 15 простых чисел:")
    for i in range(15):
        print(f"  {i+1:2}. {primes()}")
    
    # Демонстрация независимости генераторов
    print("\nНезависимость генераторов:")
    gen1 = make_prime_generator()
    gen2 = make_prime_generator()
    
    print(f"  gen1: {gen1()}, {gen1()}, {gen1()}")
    print(f"  gen2: {gen2()}, {gen2()}")
    print(f"  gen1: {gen1()}")
    print(f"  gen2: {gen2()}")


def demo_timeout_decorator():
    """Демонстрация работы декоратора-класса timeout."""
    print("\n" + "=" * 60)
    print("ДЕКОРАТОР-КЛАСС: Ограничение времени выполнения")
    print("=" * 60)
    
    # Пример 1: Быстрая функция
    print("\n1. Быстрая функция (лимит 2 сек):")
    
    @timeout(limit=2)
    def fast_function():
        return 42
    
    result = fast_function()
    print(f"   Результат: {result}")
    
    # Пример 2: Декоратор без параметра
    print("\n2. Декоратор без ограничения:")
    
    @timeout()
    def normal_function():
        time.sleep(0.1)
        return "Готово!"
    
    result = normal_function()
    print(f"   Результат: {result}")
    
    # Пример 3: Медленная функция (превышает лимит)
    print("\n3. Медленная функция (лимит 1 сек, ожидается ошибка):")
    
    @timeout(limit=1)
    def slow_function():
        time.sleep(2)
        return "Завершено"
    
    try:
        result = slow_function()
        print(f"   Результат: {result}")
    except TimeoutError as e:
        print(f"   ⏰ Ошибка: {e}")
    
    # Пример 4: Итеративная функция (вместо рекурсивной)
    print("\n4. Итеративная функция (лимит 2 сек):")
    
    @timeout(limit=2)
    def iterative_sum(n: int) -> int:
        result = 0
        for i in range(1, n + 1):
            result += i
        return result
    
    result = iterative_sum(1000000)
    print(f"   sum(1..1000000) = {result}")
    
    # Пример 5: timeout(None) - без ограничения
    print("\n5. timeout(None) - без ограничения:")
    
    @timeout(limit=None)
    def long_function():
        time.sleep(0.3)
        return "OK"
    
    result = long_function()
    print(f"   Результат: {result}")


def demo_fibonacci_iterative():
    """Демонстрация итеративного вычисления Фибоначчи с ограничением."""
    print("\n" + "=" * 60)
    print("ДОПОЛНИТЕЛЬНО: Итеративный Фибоначчи с ограничением")
    print("=" * 60)
    
    @timeout(limit=0.5)
    def fib_iterative(n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    print("\nВычисление fib(1000000) с лимитом 0.5 секунды:")
    try:
        result = fib_iterative(1000000)
        print(f"  fib(1000000) = {result} (очень большое число)")
    except TimeoutError as e:
        print(f"  ⏰ {e}")


# ============================================================
# ГЛАВНАЯ ФУНКЦИЯ
# ============================================================

def main():
    """Основная функция для демонстрации работы."""
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №5 - ЗАМЫКАНИЯ")
    print("Вариант 12 | Уровень Well-done")
    print("Декоратор-класс вместо декоратора функции")
    print("=" * 60)
    
    demo_prime_generator()
    demo_timeout_decorator()
    demo_fibonacci_iterative()
    
    print("\n" + "=" * 60)
    print("✅ Уровни Rare, Medium и Well-done выполнены!")
    print("   - Замыкание для генерации простых чисел (Rare)")
    print("   - Декоратор с опциональным параметром (Medium)")
    print("   - Декоратор-класс вместо декоратора функции (Well-done)")
    print("=" * 60)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        import pytest
        pytest.main([__file__, "-v", "--tb=short"])
    else:
        main()