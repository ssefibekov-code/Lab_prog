"""
Лабораторная работа №5
Замыкания и декораторы
"""

from functools import wraps


def log_decorator(func):
    """Декоратор для логирования вызовов"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Вызвана {func.__name__} с аргументами {args}, результат: {result}")
        return result
    return wrapper


def make_calc(operation, initial=0):
    """Создаёт калькулятор с замыканием"""
    result = initial
    
    @log_decorator
    def calc(value):
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


def call_limiter(max_calls=None):
    """Декоратор для ограничения глубины вызовов"""
    def decorator(func):
        calls = 0
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            if max_calls is not None and calls >= max_calls:
                raise RuntimeError(f"Превышен лимит вызовов ({max_calls})")
            calls += 1
            try:
                return func(*args, **kwargs)
            finally:
                calls -= 1
        return wrapper
    return decorator
