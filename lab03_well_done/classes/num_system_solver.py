#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Класс для решения задач с системами счисления
Вариант 12: 7·512^120 − 6·64^100 + 8^210 − 255 в восьмеричной системе
"""

from typing import Dict, List, Tuple


class NumSystemSolver:
    """
    Класс для работы с системами счисления.
    
    Атрибуты:
        expression (str): Строковое представление выражения
        base (int): Основание системы счисления
    """
    
    def __init__(self, expression: str, base: int):
        """
        Инициализация решателя задач с системами счисления.
        
        Args:
            expression: Строковое представление выражения
            base: Основание системы счисления
        """
        self.expression = expression
        self.base = base
        self._result = None
    
    def evaluate(self) -> int:
        """
        Вычисляет значение выражения.
        
        Returns:
            int: Числовое значение выражения
        """
        # Заменяем ^ на ** для Python
        expr = self.expression.replace('^', '**')
        self._result = eval(expr)
        return self._result
    
    def to_base(self, number: int = None) -> str:
        """
        Переводит число в заданную систему счисления.
        
        Args:
            number: Число для перевода (если None, используется вычисленное)
            
        Returns:
            str: Строковое представление числа в заданной системе
        """
        if number is None:
            number = self.evaluate()
        
        if number == 0:
            return "0"
        
        digits = []
        n = abs(number)
        while n > 0:
            digits.append(str(n % self.base))
            n //= self.base
        
        result = ''.join(reversed(digits))
        return result
    
    def count_digit(self, digit: str) -> int:
        """
        Подсчитывает количество указанной цифры в записи числа.
        
        Args:
            digit: Искомая цифра (в виде строки)
            
        Returns:
            int: Количество вхождений цифры
        """
        representation = self.to_base()
        return representation.count(digit)
    
    def count_zeros(self) -> int:
        """
        Подсчитывает количество нулей в записи числа.
        
        Returns:
            int: Количество нулей
            
        Пример:
            >>> solver = NumSystemSolver("7*512**120 - 6*64**100 + 8**210 - 255", 8)
            >>> solver.count_zeros()
            151
        """
        return self.count_digit('0')
    
    def get_digit_statistics(self) -> Dict[str, int]:
        """
        Возвращает статистику по всем цифрам в записи числа.
        
        Returns:
            dict: Словарь {цифра: количество}
        """
        representation = self.to_base()
        stats = {}
        for digit in set(representation):
            stats[digit] = representation.count(digit)
        return stats
    
    def get_result_info(self) -> dict:
        """
        Возвращает полную информацию о результате.
        
        Returns:
            dict: Словарь с информацией
        """
        value = self.evaluate()
        representation = self.to_base(value)
        return {
            'decimal_value': value,
            f'base_{self.base}_representation': representation,
            'length': len(representation),
            'zero_count': representation.count('0'),
            'digit_statistics': self.get_digit_statistics(),
        }


# Специализированный класс для варианта 12
class Variant12NumSystem(NumSystemSolver):
    """Специализированный решатель для варианта 12."""
    
    def __init__(self):
        super().__init__(
            expression="7*512**120 - 6*64**100 + 8**210 - 255",
            base=8
        )
    
    def solve(self) -> int:
        """
        Решает задачу варианта 12.
        
        Returns:
            int: Количество нулей в восьмеричной записи
        
        >>> solver = Variant12NumSystem()
        >>> solver.solve()
        151
        """
        return self.count_zeros()


if __name__ == "__main__":
    # Тестирование
    solver = Variant12NumSystem()
    print(f"Значение выражения: {solver.evaluate()}")
    print(f"Восьмеричная запись: {solver.to_base()}")
    print(f"Количество нулей: {solver.solve()}")
    print(f"Статистика по цифрам: {solver.get_digit_statistics()}")