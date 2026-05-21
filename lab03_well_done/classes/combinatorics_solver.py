#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Класс для решения комбинаторных задач с использованием itertools
Вариант 12: 5-буквенные коды из букв И, В, А, Н (буква И хотя бы один раз)
"""

import itertools
from typing import List, Set


class CombinatoricsSolver:
    """
    Класс для решения комбинаторных задач.
    
    Атрибуты:
        letters (List[str]): Список допустимых букв
        code_length (int): Длина кодового слова
        required_letter (str): Буква, которая должна встречаться хотя бы раз
    """
    
    def __init__(self, letters: List[str], code_length: int, required_letter: str = None):
        """
        Инициализация решателя комбинаторных задач.
        
        Args:
            letters: Список допустимых букв
            code_length: Длина кодового слова
            required_letter: Буква, которая должна встречаться хотя бы раз (опционально)
        """
        self.letters = letters
        self.code_length = code_length
        self.required_letter = required_letter
    
    def total_combinations(self) -> int:
        """
        Вычисляет общее количество комбинаций.
        
        Returns:
            int: Количество всех возможных комбинаций
        """
        return len(self.letters) ** self.code_length
    
    def combinations_without_letter(self, letter: str) -> int:
        """
        Вычисляет количество комбинаций без указанной буквы.
        
        Args:
            letter: Буква, которая не должна встречаться
            
        Returns:
            int: Количество комбинаций без указанной буквы
        """
        filtered_letters = [l for l in self.letters if l != letter]
        return len(filtered_letters) ** self.code_length
    
    def count_codes_with_required_letter(self) -> int:
        """
        Вычисляет количество кодов, содержащих обязательную букву хотя бы один раз.
        
        Returns:
            int: Количество кодов с обязательной буквой
            
        Пример:
            >>> solver = CombinatoricsSolver(['И', 'В', 'А', 'Н'], 5, 'И')
            >>> solver.count_codes_with_required_letter()
            781
        """
        if self.required_letter is None:
            return self.total_combinations()
        
        without_required = self.combinations_without_letter(self.required_letter)
        return self.total_combinations() - without_required
    
    def generate_all_codes(self) -> List[tuple]:
        """
        Генерирует все возможные коды (для проверки).
        
        Returns:
            List[tuple]: Список всех комбинаций
        """
        return list(itertools.product(self.letters, repeat=self.code_length))
    
    def get_statistics(self) -> dict:
        """
        Возвращает статистику по комбинациям.
        
        Returns:
            dict: Словарь со статистикой
        """
        return {
            'total_combinations': self.total_combinations(),
            'code_length': self.code_length,
            'letters_count': len(self.letters),
            'required_letter': self.required_letter,
            'codes_with_required': self.count_codes_with_required_letter() if self.required_letter else None,
        }


# Специализированный класс для варианта 12
class Variant12Combinatorics(CombinatoricsSolver):
    """Специализированный решатель для варианта 12."""
    
    def __init__(self):
        super().__init__(
            letters=['И', 'В', 'А', 'Н'],
            code_length=5,
            required_letter='И'
        )
    
    def solve(self) -> int:
        """
        Решает задачу варианта 12.
        
        Returns:
            int: Количество кодов
        
        >>> solver = Variant12Combinatorics()
        >>> solver.solve()
        781
        """
        return self.count_codes_with_required_letter()


if __name__ == "__main__":
    # Тестирование
    solver = Variant12Combinatorics()
    print(f"Всего комбинаций: {solver.total_combinations()}")
    print(f"Комбинаций без 'И': {solver.combinations_without_letter('И')}")
    print(f"Кодов с буквой 'И': {solver.solve()}")