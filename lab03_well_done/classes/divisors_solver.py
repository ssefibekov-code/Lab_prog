#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Класс для решения задач с делителями чисел
Вариант 12: поиск числа с максимальным количеством делителей в диапазоне [84052; 84130]
"""

from typing import List, Tuple, Dict, Optional
import math


class DivisorsSolver:
    """
    Класс для работы с делителями чисел.
    
    Атрибуты:
        range_start (int): Начало диапазона
        range_end (int): Конец диапазона
    """
    
    def __init__(self, range_start: int, range_end: int):
        """
        Инициализация решателя задач с делителями.
        
        Args:
            range_start: Начало диапазона (включительно)
            range_end: Конец диапазона (включительно)
        """
        self.range_start = range_start
        self.range_end = range_end
    
    @staticmethod
    def count_divisors(n: int) -> int:
        """
        Подсчитывает количество делителей числа.
        
        Args:
            n: Натуральное число
            
        Returns:
            int: Количество делителей
            
        Пример:
            >>> DivisorsSolver.count_divisors(12)
            6
            >>> DivisorsSolver.count_divisors(48)
            10
        """
        if n <= 0:
            return 0
        
        count = 0
        sqrt_n = int(math.sqrt(n))
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                count += 1
                if i != n // i:
                    count += 1
        return count
    
    @staticmethod
    def get_divisors(n: int) -> List[int]:
        """
        Возвращает список всех делителей числа.
        
        Args:
            n: Натуральное число
            
        Returns:
            List[int]: Список делителей в порядке возрастания
        """
        divisors = []
        sqrt_n = int(math.sqrt(n))
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sorted(divisors)
    
    @staticmethod
    def prime_factorization(n: int) -> Dict[int, int]:
        """
        Разлагает число на простые множители.
        
        Args:
            n: Натуральное число
            
        Returns:
            dict: Словарь {простой_множитель: степень}
        """
        factors = {}
        num = n
        d = 2
        while d * d <= num:
            while num % d == 0:
                factors[d] = factors.get(d, 0) + 1
                num //= d
            d += 1
        if num > 1:
            factors[num] = factors.get(num, 0) + 1
        return factors
    
    @staticmethod
    def divisors_count_from_factors(factors: Dict[int, int]) -> int:
        """
        Вычисляет количество делителей из разложения на простые множители.
        
        Args:
            factors: Словарь {простой_множитель: степень}
            
        Returns:
            int: Количество делителей
        """
        count = 1
        for exp in factors.values():
            count *= (exp + 1)
        return count
    
    def find_max_divisors_number(self) -> Tuple[int, int]:
        """
        Находит число с максимальным количеством делителей в заданном диапазоне.
        
        Returns:
            tuple: (количество_делителей, число)
            
        Пример:
            >>> solver = DivisorsSolver(2, 48)
            >>> solver.find_max_divisors_number()
            (10, 48)
        """
        max_divisors = 0
        number_with_max = 0
        
        for num in range(self.range_start, self.range_end + 1):
            current_divisors = self.count_divisors(num)
            if current_divisors > max_divisors:
                max_divisors = current_divisors
                number_with_max = num
        
        return (max_divisors, number_with_max)
    
    def analyze_range(self) -> List[Tuple[int, int, Dict[int, int]]]:
        """
        Анализирует весь диапазон и возвращает информацию о числах.
        
        Returns:
            list: Список кортежей (число, количество_делителей, разложение)
        """
        results = []
        for num in range(self.range_start, self.range_end + 1):
            divisors_count = self.count_divisors(num)
            factorization = self.prime_factorization(num)
            results.append((num, divisors_count, factorization))
        return results
    
    def get_range_info(self) -> dict:
        """
        Возвращает полную информацию о диапазоне.
        
        Returns:
            dict: Словарь с информацией
        """
        max_div, max_num = self.find_max_divisors_number()
        
        return {
            'range': f"[{self.range_start}; {self.range_end}]",
            'size': self.range_end - self.range_start + 1,
            'max_divisors': max_div,
            'max_divisors_number': max_num,
            'max_divisors_factorization': self.prime_factorization(max_num),
        }


# Специализированный класс для варианта 12
class Variant12Divisors(DivisorsSolver):
    """Специализированный решатель для варианта 12."""
    
    def __init__(self):
        super().__init__(range_start=84052, range_end=84130)
    
    def solve(self) -> Tuple[int, int]:
        """
        Решает задачу варианта 12.
        
        Returns:
            tuple: (количество_делителей, число)
        
        Пример:
            >>> solver = Variant12Divisors()
            >>> solver.solve()
            (72, 84084)
        """
        return self.find_max_divisors_number()


if __name__ == "__main__":
    # Тестирование
    solver = Variant12Divisors()
    count, number = solver.solve()
    print(f"Число с максимальным количеством делителей: {number}")
    print(f"Количество делителей: {count}")
    print(f"Разложение на множители: {solver.prime_factorization(number)}")
    print(f"Проверка: {solver.divisors_count_from_factors(solver.prime_factorization(number))} = {count}")