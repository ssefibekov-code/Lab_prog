#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль из лабораторной работы №4 - Рекурсия
Вариант 12: Линеаризация списков и рекуррентная последовательность
"""


# ========== ЛИНЕАРИЗАЦИЯ СПИСКОВ ==========

def linearize_recursive(nested_list):
    """
    Рекурсивная линеаризация вложенного списка.
    
    Args:
        nested_list: Вложенный список произвольной глубины
        
    Returns:
        list: Плоский список со всеми элементами
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(linearize_recursive(item))
        else:
            result.append(item)
    return result


def linearize_iterative(nested_list):
    """
    Итеративная линеаризация вложенного списка.
    
    Args:
        nested_list: Вложенный список произвольной глубины
        
    Returns:
        list: Плоский список со всеми элементами
    """
    if not nested_list:
        return []
    
    result = []
    stack = [nested_list]
    
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            for item in reversed(current):
                stack.append(item)
        else:
            result.append(current)
    
    return list(reversed(result))


# ========== РЕКУРРЕНТНАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ ==========

def a_recursive(k):
    """
    Рекурсивное вычисление a_k.
    Формулы: a₁=1, b₁=1, a_k=2·b_{k-1}+a_{k-1}, b_k=2·a_{k-1}+b_{k-1}
    
    Args:
        k: Номер члена последовательности
        
    Returns:
        int: Значение a_k
    """
    def helper(k):
        if k == 1:
            return 1, 1
        a_prev, b_prev = helper(k - 1)
        a_k = 2 * b_prev + a_prev
        b_k = 2 * a_prev + b_prev
        return a_k, b_k
    
    return helper(k)[0]


def a_iterative(k):
    """
    Итеративное вычисление a_k.
    
    Args:
        k: Номер члена последовательности
        
    Returns:
        int: Значение a_k
    """
    if k == 1:
        return 1
    
    a_prev, b_prev = 1, 1
    
    for _ in range(2, k + 1):
        a_k = 2 * b_prev + a_prev
        b_k = 2 * a_prev + b_prev
        a_prev, b_prev = a_k, b_k
    
    return a_prev


def get_sequence(n):
    """Возвращает список первых n членов последовательности a_k."""
    return [a_iterative(i) for i in range(1, n + 1)]


# ========== ДЕМОНСТРАЦИЯ ==========

def demo():
    """Демонстрация работы модуля."""
    print("=" * 50)
    print("РЕКУРСИЯ (ЛР4)")
    print("=" * 50)
    
    print("\n1. Линеаризация списка:")
    test_list = [1, 2, [3, 4, [5, [6, []]]]]
    print(f"   Исходный: {test_list}")
    print(f"   Рекурсивно: {linearize_recursive(test_list)}")
    print(f"   Итеративно: {linearize_iterative(test_list)}")
    
    print("\n2. Рекуррентная последовательность a_k:")
    print(f"   a_k = 3^(k-1)")
    for k in range(1, 8):
        print(f"   a_{k} = {a_iterative(k)}")


if __name__ == "__main__":
    demo()