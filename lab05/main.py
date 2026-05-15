#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Лабораторная работа №5 - Замыкания
Вариант 12

Задачи:
1. Замыкание для получения простых чисел
2. Декоратор, не позволяющий функции выполняться больше определённого времени
"""

import time
import functools
from typing import Optional, Callable, Any, List


# ============================================================================
# ЗАДАЧА 1: ЗАМЫКАНИЕ ДЛЯ ПОЛУЧЕНИЯ ПРОСТЫХ ЧИСЕЛ
# ============================================================================

def make_prime_generator():
    """
    Создаёт замыкание для генерации простых чисел.
    
    Returns:
        function: Генератор простых чисел
    """
    primes_found: List[int] = []
    current: int = 2
    
    def is_prime(n: int) -> bool:
        """Проверяет, является ли число простым."""
        if n < 2:
            return False
        for p in primes_found:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True
    
    def get_next_prime() -> int:
        """Возвращает следующее простое число."""
        nonlocal current
        while not is_prime(current):
            current += 1
        result = current
        primes_found.append(result)
        current += 1
        return result
    
    return get_next_prime


# ============================================================================
# ЗАДАЧА 2: ДЕКОРАТОР ДЛЯ ОГРАНИЧЕНИЯ ВРЕМЕНИ
# ============================================================================

class TimeoutError(Exception):
    """Исключение при превышении лимита времени."""
    pass


def timeout(limit: Optional[float] = None):
    """
    Декоратор для ограничения времени выполнения функции.
    
    Args:
        limit: Максимальное время в секундах. Если None - без ограничения.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time
            
            if limit is not None and limit > 0 and elapsed > limit:
                raise TimeoutError(
                    f"Функция '{func.__name__}' выполнялась {elapsed:.2f} сек, "
                    f"что превышает лимит {limit} сек"
                )
            return result
        
        return wrapper
    return decorator


# ============================================================================
# ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ
# ============================================================================

def demo_prime_generator():
    """Демонстрация генератора простых чисел."""
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
    """Демонстрация декоратора timeout."""
    print("\n" + "=" * 60)
    print("ДЕКОРАТОР: Ограничение времени выполнения")
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
        time.sleep(0.3)
        return "Готово!"
    
    result = normal_function()
    print(f"   Результат: {result}")
    
    # Пример 3: Медленная функция
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
    
    # Пример 4: Функция с None
    print("\n4. timeout(None) - без ограничения:")
    
    @timeout(limit=None)
    def long_function():
        time.sleep(0.2)
        return "OK"
    
    result = long_function()
    print(f"   Результат: {result}")


# ============================================================================
# ТЕСТЫ (pytest)
# ============================================================================

def test_prime_generator():
    """Тест генератора простых чисел."""
    gen = make_prime_generator()
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    for exp in expected:
        assert gen() == exp


def test_prime_generator_independence():
    """Тест независимости генераторов."""
    g1 = make_prime_generator()
    g2 = make_prime_generator()
    
    assert g1() == 2
    assert g2() == 2
    assert g1() == 3
    assert g1() == 5
    assert g2() == 3
    assert g2() == 5


def test_timeout_no_limit():
    """Тест без ограничения."""
    @timeout()
    def func():
        return 100
    
    assert func() == 100


def test_timeout_with_limit():
    """Тест с ограничением (успех)."""
    @timeout(limit=2)
    def fast_func():
        return 42
    
    assert fast_func() == 42


def test_timeout_exceeds_limit():
    """Тест превышения лимита."""
    @timeout(limit=0.1)
    def slow_func():
        time.sleep(0.2)
        return "Done"
    
    import pytest
    with pytest.raises(TimeoutError):
        slow_func()


def test_timeout_optional_none():
    """Тест с параметром None."""
    @timeout(limit=None)
    def func():
        time.sleep(0.05)
        return "OK"
    
    assert func() == "OK"


def test_timeout_preserves_metadata():
    """Тест сохранения метаданных."""
    @timeout(limit=1)
    def test_func():
        """Документация."""
        pass
    
    assert test_func.__name__ == "test_func"
    assert test_func.__doc__ == "Документация."


def test_timeout_multiple_calls():
    """Тест нескольких вызовов."""
    @timeout(limit=5)
    def counter():
        return 1
    
    total = sum(counter() for _ in range(10))
    assert total == 10


def test_timeout_decorator_optional():
    """Тест опционального параметра."""
    @timeout(limit=2)
    def f1():
        return 1
    
    @timeout()
    def f2():
        return 2
    
    @timeout(limit=None)
    def f3():
        return 3
    
    assert f1() == 1
    assert f2() == 2
    assert f3() == 3


# ============================================================================
# ГЛАВНАЯ ФУНКЦИЯ
# ============================================================================

def main():
    """Основная функция."""
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №5 - ЗАМЫКАНИЯ")
    print("Вариант 12")
    print("=" * 60)
    
    demo_prime_generator()
    demo_timeout_decorator()
    
    print("\n" + "=" * 60)
    print("✅ РАБОТА ВЫПОЛНЕНА")
    print("=" * 60)
    print("\nЗапуск тестов: pytest main.py -v")
    print("=" * 60)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        import pytest
        pytest.main([__file__, "-v", "--tb=short"])
    else:
        main()