#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Лабораторная работа №4 - Рекурсия
Вариант 12

Задачи:
1. Линеаризация вложенных списков (Rare)
2. Вычисление рекуррентной последовательности a_k (Rare)
3. Pytest тесты (Medium)
"""


# ============================================================
# ЗАДАЧА 1: ЛИНЕАРИЗАЦИЯ СПИСКОВ (Rare)
# ============================================================

def linearize_recursive(nested_list):
    """
    Рекурсивная линеаризация вложенного списка.
    
    Args:
        nested_list: Вложенный список произвольной глубины
        
    Returns:
        Плоский список со всеми элементами
        
    Примеры:
        >>> linearize_recursive([1, 2, [3, 4]])
        [1, 2, 3, 4]
        >>> linearize_recursive([1, [2, [3, [4, [5]]]]])
        [1, 2, 3, 4, 5]
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(linearize_recursive(item))
        else:
            result.append(item)
    return result


def linearize_iterative(nested_list):
    """Итеративная линеаризация вложенного списка."""
    result = []
    stack = [nested_list]
    while stack:
        current = stack.pop(0)  # Берём первый элемент (не последний)
        if isinstance(current, list):
            stack = current + stack  # Добавляем в начало
        else:
            result.append(current)
    return result


# ============================================================
# ЗАДАЧА 2: РЕКУРРЕНТНАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ (Rare)
# ============================================================

def a_recursive(k):
    """
    Рекурсивное вычисление a_k.
    
    Формулы:
        a₁ = 1, b₁ = 1
        a_k = 2 * b_{k-1} + a_{k-1}
        b_k = 2 * a_{k-1} + b_{k-1}
    
    Args:
        k: Номер члена последовательности (k >= 1)
        
    Returns:
        Значение a_k
        
    Примеры:
        >>> a_recursive(1)
        1
        >>> a_recursive(2)
        3
        >>> a_recursive(3)
        9
        >>> a_recursive(4)
        27
    """
    def helper(n):
        if n == 1:
            return 1, 1  # (a₁, b₁)
        a_prev, b_prev = helper(n - 1)
        a_n = 2 * b_prev + a_prev
        b_n = 2 * a_prev + b_prev
        return a_n, b_n
    
    return helper(k)[0]


def a_iterative(k):
    """
    Итеративное вычисление a_k.
    
    Args:
        k: Номер члена последовательности (k >= 1)
        
    Returns:
        Значение a_k
        
    Примеры:
        >>> a_iterative(1)
        1
        >>> a_iterative(2)
        3
        >>> a_iterative(3)
        9
        >>> a_iterative(4)
        27
    """
    if k == 1:
        return 1
    
    a_prev, b_prev = 1, 1
    
    for _ in range(2, k + 1):
        a_curr = 2 * b_prev + a_prev
        b_curr = 2 * a_prev + b_prev
        a_prev, b_prev = a_curr, b_curr
    
    return a_prev


def get_sequence(n):
    """
    Возвращает список первых n членов последовательности a_k.
    
    Args:
        n: Количество членов последовательности
        
    Returns:
        Список значений [a₁, a₂, ..., a_n]
        
    Пример:
        >>> get_sequence(5)
        [1, 3, 9, 27, 81]
    """
    return [a_iterative(i) for i in range(1, n + 1)]


# ============================================================
# PYTEST ТЕСТЫ (Medium)
# ============================================================

import pytest


# Тесты для линеаризации списков
def test_linearize_empty():
    """Пустой список"""
    assert linearize_recursive([]) == []
    assert linearize_iterative([]) == []


def test_linearize_flat():
    """Плоский список"""
    assert linearize_recursive([1, 2, 3]) == [1, 2, 3]
    assert linearize_iterative([1, 2, 3]) == [1, 2, 3]


def test_linearize_single_nested():
    """Одноуровневая вложенность"""
    assert linearize_recursive([1, [2, 3], 4]) == [1, 2, 3, 4]
    assert linearize_iterative([1, [2, 3], 4]) == [1, 2, 3, 4]


def test_linearize_multi_nested():
    """Многоуровневая вложенность"""
    nested = [1, 2, [3, 4, [5, [6, []]]]]
    expected = [1, 2, 3, 4, 5, 6]
    assert linearize_recursive(nested) == expected
    assert linearize_iterative(nested) == expected


def test_linearize_deep_nested():
    """Глубокая вложенность"""
    nested = [1, [2, [3, [4, [5, [6, [7]]]]]]]
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert linearize_recursive(nested) == expected
    assert linearize_iterative(nested) == expected


def test_linearize_strings():
    """Строковые элементы"""
    nested = ['a', ['b', 'c'], ['d', ['e', 'f']]]
    expected = ['a', 'b', 'c', 'd', 'e', 'f']
    assert linearize_recursive(nested) == expected
    assert linearize_iterative(nested) == expected


def test_linearize_mixed_types():
    """Смешанные типы данных"""
    nested = [1, 'hello', [3.14, [True, None], [False]]]
    expected = [1, 'hello', 3.14, True, None, False]
    assert linearize_recursive(nested) == expected
    assert linearize_iterative(nested) == expected


# Тесты для рекуррентной последовательности
def test_a_base():
    """Базовые случаи"""
    assert a_recursive(1) == 1
    assert a_iterative(1) == 1


def test_a_values():
    """Проверка значений (a_k = 3^(k-1))"""
    expected = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683]
    
    for k, exp in enumerate(expected, start=1):
        assert a_recursive(k) == exp, f"a_{k} = {a_recursive(k)}, expected {exp}"
        assert a_iterative(k) == exp, f"a_{k} = {a_iterative(k)}, expected {exp}"


def test_a_consistency():
    """Согласованность рекурсивной и итеративной версий"""
    for k in range(1, 20):
        assert a_recursive(k) == a_iterative(k), f"k={k}"


def test_sequence():
    """Получение последовательности"""
    assert get_sequence(1) == [1]
    assert get_sequence(3) == [1, 3, 9]
    assert get_sequence(5) == [1, 3, 9, 27, 81]


def test_performance():
    """Тест производительности (итеративная версия быстрее)"""
    import time
    
    k = 25
    
    start = time.time()
    a_recursive(k)
    rec_time = time.time() - start
    
    start = time.time()
    a_iterative(k)
    it_time = time.time() - start
    
    assert it_time <= rec_time * 1.2, f"Рекурсивно: {rec_time}, Итеративно: {it_time}"


# ============================================================
# ГЛАВНАЯ ФУНКЦИЯ ДЛЯ ДЕМОНСТРАЦИИ
# ============================================================

def main():
    """Демонстрация работы функций"""
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №4 - РЕКУРСИЯ (Вариант 12)")
    print("=" * 60)
    
    # Задача 1
    print("\n📌 Задача 1: Линеаризация списков")
    print("-" * 40)
    
    test_list = [1, 2, [3, 4, [5, [6, []]]]]
    print(f"Исходный список:                 {test_list}")
    print(f"Рекурсивная линеаризация:        {linearize_recursive(test_list)}")
    print(f"Итеративная линеаризация:        {linearize_iterative(test_list)}")
    
    # Дополнительные примеры
    print("\nДополнительные примеры:")
    examples = [
        ([1, [2, 3], 4], "Одноуровневый"),
        (['x', ['y', 'z']], "Строковый"),
        ([1, 'a', [True, [None]]], "Смешанный тип"),
    ]
    
    for ex, desc in examples:
        print(f"  {desc:15}: {ex} -> {linearize_iterative(ex)}")
    
    # Задача 2
    print("\n📌 Задача 2: Рекуррентная последовательность")
    print("-" * 40)
    print("Формулы:")
    print("  a₁ = 1, b₁ = 1")
    print("  a_k = 2·b_{k-1} + a_{k-1}")
    print("  b_k = 2·a_{k-1} + b_{k-1}")
    
    print("\nЗначения a_k (первые 10 членов):")
    print(f"  {'k':>3} | {'a_k (рекурс.)':>12} | {'a_k (итерат.)':>12} | {'3^(k-1)':>10}")
    print("  " + "-" * 45)
    
    for k in range(1, 11):
        rec = a_recursive(k)
        it = a_iterative(k)
        formula = 3 ** (k - 1)
        print(f"  {k:3} | {rec:12} | {it:12} | {formula:10}")
    
    # Закономерность
    print("\n📊 Обнаруженная закономерность:")
    print("  a_k = 3^(k-1)")
    print("  Доказательство: при k=1: 3^0 = 1 ✓, при k=2: 3^1 = 3 ✓")
    
    print("\n" + "=" * 60)
    print("✅ Уровни Rare и Medium выполнены!")
    print("📝 Запуск тестов: pytest main.py -v")
    print("=" * 60)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        pytest.main([__file__, "-v", "-s"])
    elif len(sys.argv) > 1 and sys.argv[1] == "--quick":
        # Быстрая проверка без графики
        print("Быстрая проверка:")
        print(f"  linearize_iterative([1,2,[3,4]]) = {linearize_iterative([1,2,[3,4]])}")
        print(f"  a_iterative(5) = {a_iterative(5)}")
    else:
        main()