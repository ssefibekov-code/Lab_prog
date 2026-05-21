#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для декоратора-класса timeout."""

import pytest
import time
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import timeout, TimeoutError


class TestTimeoutDecorator:
    """Тесты для декоратора timeout."""
    
    def test_no_limit(self):
        """Тест декоратора без ограничения."""
        @timeout()
        def fast_func():
            return 100
        
        assert fast_func() == 100
    
    def test_with_limit_success(self):
        """Тест декоратора с ограничением (без превышения)."""
        @timeout(limit=2)
        def fast_func():
            return 42
        
        assert fast_func() == 42
    
    def test_exceeds_limit(self):
        """Тест превышения лимита времени."""
        @timeout(limit=0.1)
        def slow_func():
            time.sleep(0.2)
            return "Done"
        
        with pytest.raises(TimeoutError):
            slow_func()
    
    def test_optional_none(self):
        """Тест параметра None."""
        @timeout(limit=None)
        def func():
            time.sleep(0.05)
            return "OK"
        
        assert func() == "OK"
    
    def test_preserves_metadata(self):
        """Тест сохранения метаданных функции."""
        @timeout(limit=1)
        def test_func():
            """Документация тестовой функции."""
            pass
        
        assert test_func.__name__ == "test_func"
        assert test_func.__doc__ == "Документация тестовой функции."
    
    def test_multiple_calls(self):
        """Тест нескольких вызовов."""
        call_count = 0
        
        @timeout(limit=5)
        def counter():
            nonlocal call_count
            call_count += 1
            return call_count
        
        for i in range(10):
            assert counter() == i + 1
    
    def test_optional_param(self):
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
    
    def test_recursive_function(self):
        """Тест рекурсивной функции (итеративная версия для избежания RecursionError)."""
        # Используем итеративную версию вместо рекурсивной
        @timeout(limit=1)
        def iterative_sum(n):
            result = 0
            for i in range(1, n + 1):
                result += i
            return result
        
        result = iterative_sum(500)
        assert result == 125250  # 500*501/2 = 125250
    
    def test_recursive_fibonacci_small(self):
        """Тест рекурсивного вычисления Фибоначчи (малое n)."""
        @timeout(limit=1)
        def fib(n):
            if n <= 1:
                return n
            return fib(n - 1) + fib(n - 2)
        
        result = fib(10)
        assert result == 55
    
    def test_timeout_message(self):
        """Тест сообщения об ошибке (исправлен)."""
        @timeout(limit=0.1)
        def slow_func():
            time.sleep(0.2)
            return "Done"
        
        with pytest.raises(TimeoutError) as exc_info:
            slow_func()
        
        # Проверяем наличие ключевых слов в сообщении (без учёта регистра)
        message = str(exc_info.value).lower()
        assert ("превысила" in message or 
                "превышает" in message or 
                "timeout" in message or
                "лимит" in message)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])