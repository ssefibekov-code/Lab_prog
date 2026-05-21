#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Тесты для замыкания генератора простых чисел."""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import make_prime_generator


class TestPrimeGenerator:
    """Тесты для генератора простых чисел."""
    
    def test_first_primes(self):
        """Проверка первых простых чисел."""
        gen = make_prime_generator()
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        
        for exp in expected:
            assert gen() == exp
    
    def test_independence(self):
        """Проверка независимости разных генераторов."""
        g1 = make_prime_generator()
        g2 = make_prime_generator()
        
        assert g1() == 2
        assert g2() == 2
        assert g1() == 3
        assert g2() == 3
        assert g1() == 5
        assert g2() == 5
    
    def test_state_preservation(self):
        """Проверка сохранения состояния между вызовами."""
        gen = make_prime_generator()
        
        primes = [gen() for _ in range(10)]
        
        # Проверяем, что все числа простые
        for prime in primes:
            assert all(prime % i != 0 for i in range(2, int(prime ** 0.5) + 1))
    
    def test_generator_reset(self):
        """Проверка, что новый генератор начинает с начала."""
        gen1 = make_prime_generator()
        gen2 = make_prime_generator()
        
        # Берём несколько чисел из первого генератора
        for _ in range(5):
            gen1()
        
        # Второй генератор должен начать с 2
        assert gen2() == 2
        assert gen2() == 3
    
    def test_large_prime(self):
        """Проверка получения большого простого числа."""
        gen = make_prime_generator()
        
        # Пропускаем первые 100 простых чисел
        for _ in range(100):
            prime = gen()
        
        # 100-е простое число - 541
        assert prime == 541


if __name__ == "__main__":
    pytest.main([__file__, "-v"])