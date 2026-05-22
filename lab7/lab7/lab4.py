"""
Лабораторная работа №4
Рекурсия и итерация
"""

def linearize_recursive(nested_list):
    """Рекурсивная линеаризация списка"""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(linearize_recursive(item))
        else:
            result.append(item)
    return result


def linearize_iterative(nested_list):
    """Итеративная линеаризация списка через стек"""
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


def a_recursive(k):
    """Рекурсивное вычисление a_k"""
    if k == 1:
        return 1
    
    def helper(n):
        if n == 1:
            return 1, 1
        a_prev, b_prev = helper(n - 1)
        a_n = 2 * b_prev + a_prev
        b_n = 2 * a_prev + b_prev
        return a_n, b_n
    
    return helper(k)[0]


def a_iterative(k):
    """Итеративное вычисление a_k"""
    if k == 1:
        return 1
    
    a, b = 1, 1
    for _ in range(2, k + 1):
        new_a = 2 * b + a
        new_b = 2 * a + b
        a, b = new_a, new_b
    
    return a


def get_sequence_a(n):
    """Получить первые n членов a_k"""
    return [a_iterative(i) for i in range(1, n + 1)]


def get_sequence_b(n):
    """Получить первые n членов b_k"""
    if n == 0:
        return []
    
    result = [1]
    a, b = 1, 1
    
    for _ in range(2, n + 1):
        new_a = 2 * b + a
        new_b = 2 * a + b
        result.append(new_b)
        a, b = new_a, new_b
    
    return result