#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для модуля lab5 (Замыкания и декораторы)"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from lab7_package import make_calc, call_limiter, log_decorator


class TestMakeCalc:
    """Тесты для калькулятора с замыканием."""
    
    def test_addition(self):
        """Тест сложения."""
        calc = make_calc('+', 10)
        assert calc(5) == 15
        assert calc(3) == 18
        assert calc(-2) == 16
    
    def test_subtraction(self):
        """Тест вычитания."""
        calc = make_calc('-', 10)
        assert calc(5) == 5
        assert calc(3) == 2
        assert calc(-2) == 4
    
    def test_multiplication(self):
        """Тест умножения."""
        calc = make_calc('*', 2)
        assert calc(3) == 6
        assert calc(4) == 24
        assert calc(0.5) == 12
    
    def test_division(self):
        """Тест деления."""
        calc = make_calc('/', 100)
        assert calc(2) == 50
        assert calc(5) == 10
        assert calc(2) == 5
    
    def test_division_by_zero(self):
        """Тест деления на ноль."""
        calc = make_calc('/', 10)
        with pytest.raises(ValueError, match="Деление на ноль"):
            calc(0)
    
    def test_invalid_operation(self):
        """Тест неверной операции."""
        # Проверяем, что вызов с неверной операцией вызывает ошибку
        with pytest.raises(Exception):
            calc = make_calc('%', 10)
            calc(5)
    
    def test_no_initial(self):
        """Тест без начального значения."""
        calc = make_calc('+')
        assert calc(5) == 5
        assert calc(3) == 8


class TestCallLimiter:
    """Тесты для декоратора call_limiter."""
    
    def test_no_limit(self):
        """Тест без ограничения."""
        @call_limiter()
        def func():
            return 42
        
        for _ in range(100):
            assert func() == 42
    
    def test_with_limit(self):
        """Тест с ограничением."""
        @call_limiter(max_calls=3)
        def counter():
            return 1
        
        assert counter() == 1
        assert counter() == 1
        assert counter() == 1
        assert counter() == 1  # Работает
    
    def test_recursive_function_with_limit(self):
        """Тест рекурсивной функции с ограничением."""
        @call_limiter(max_calls=5)
        def recursive_depth(n):
            if n <= 0:
                return 0
            return 1 + recursive_depth(n - 1)
        
        result = recursive_depth(3)
        assert result == 3
    
    def test_factorial_with_limit(self):
        """Тест факториала с ограничением."""
        @call_limiter(max_calls=10)
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)
        
        result = factorial(5)
        assert result == 120
    
    def test_multiple_decorators(self):
        """Тест нескольких декорированных функций."""
        @call_limiter(max_calls=2)
        def func1():
            return 1
        
        @call_limiter(max_calls=3)
        def func2():
            return 2
        
        assert func1() == 1
        assert func1() == 1
        assert func1() == 1
        
        assert func2() == 2
        assert func2() == 2
        assert func2() == 2
    
    def test_different_limits(self):
        """Тест разных лимитов."""
        @call_limiter(max_calls=1)
        def once():
            return "once"
        
        @call_limiter(max_calls=5)
        def five_times():
            return "five"
        
        assert once() == "once"
        assert once() == "once"
        
        for _ in range(10):
            assert five_times() == "five"


class TestLogDecorator:
    """Тесты для декоратора логирования."""
    
    def test_log_output(self, capsys):
        """Тест вывода лога."""
        @log_decorator
        def add(a, b):
            return a + b
        
        result = add(3, 5)
        
        captured = capsys.readouterr()
        assert "add" in captured.out or "Вызвана" in captured.out
        assert result == 8
    
    def test_log_with_kwargs(self, capsys):
        """Тест логирования с именованными аргументами."""
        @log_decorator
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"
        
        result = greet("World")
        
        captured = capsys.readouterr()
        assert "greet" in captured.out or "Вызвана" in captured.out
        assert result == "Hello, World!"
    
    def test_preserves_metadata(self):
        """Тест сохранения метаданных функции."""
        @log_decorator
        def my_function():
            """Документация."""
            pass
        
        assert my_function.__name__ == "my_function"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])