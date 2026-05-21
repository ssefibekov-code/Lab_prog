#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Лабораторная работа №3 - Расчётные задачи. Itertools
Вариант 12
Уровень Well-done: обобщение алгоритмов и обёртывание в классы
"""

from classes import (
    Variant12Combinatorics,
    Variant12NumSystem,
    Variant12Divisors
)


def print_header(title: str):
    """Выводит красивый заголовок."""
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)


def main():
    """Основная функция."""
    print("=" * 60)
    print(" ЛАБОРАТОРНАЯ РАБОТА №3 - ВАРИАНТ 12")
    print(" Уровень Well-done: классы")
    print("=" * 60)
    
    # Задача 1: Комбинаторика
    print_header("Задача 1: Комбинаторика")
    print("Условие: 5-буквенные коды из букв И, В, А, Н")
    print("Требование: буква И используется хотя бы один раз")
    print("-" * 40)
    
    combinatorics = Variant12Combinatorics()
    result1 = combinatorics.solve()
    
    print(f"Всего комбинаций: {combinatorics.total_combinations()}")
    print(f"Комбинаций без 'И': {combinatorics.combinations_without_letter('И')}")
    print(f"✅ Кодов с буквой 'И': {result1}")
    print(f"Проверка: 4^5 - 3^5 = 1024 - 243 = {result1}")
    
    # Задача 2: Системы счисления
    print_header("Задача 2: Системы счисления")
    print("Выражение: 7·512^120 − 6·64^100 + 8^210 − 255")
    print("Система счисления: восьмеричная")
    print("Требование: найти количество цифр 0")
    print("-" * 40)
    
    num_system = Variant12NumSystem()
    result2 = num_system.solve()
    info = num_system.get_result_info()
    
    print(f"Значение выражения (десятичное): {info['decimal_value']}")
    print(f"Восьмеричная запись (первые 50 символов): {info['base_8_representation'][:50]}...")
    print(f"Длина записи: {info['length']} цифр")
    print(f"Статистика по цифрам: {info['digit_statistics']}")
    print(f"✅ Количество нулей: {result2}")
    
    # Задача 3: Делители чисел
    print_header("Задача 3: Делители чисел")
    print("Диапазон: [84052; 84130]")
    print("Требование: найти число с максимальным количеством делителей")
    print("-" * 40)
    
    divisors = Variant12Divisors()
    result3_count, result3_number = divisors.solve()
    range_info = divisors.get_range_info()
    
    print(f"Диапазон: {range_info['range']}")
    print(f"Всего чисел в диапазоне: {range_info['size']}")
    print(f"✅ Число с максимальным количеством делителей: {result3_number}")
    print(f"✅ Количество делителей: {result3_count}")
    print(f"Разложение на множители: {range_info['max_divisors_factorization']}")
    
    # Проверка через формулу
    factors = divisors.prime_factorization(result3_number)
    check_count = divisors.divisors_count_from_factors(factors)
    print(f"Проверка: (2+1)·(1+1)·(2+1)·(1+1)·(1+1) = 3·2·3·2·2 = {check_count}")
    
    print_header("ВСЕ ЗАДАЧИ РЕШЕНЫ")
    print(f"Результаты:")
    print(f"  Задача 1: {result1} кодов")
    print(f"  Задача 2: {result2} нулей")
    print(f"  Задача 3: число {result3_number} имеет {result3_count} делителей")
    print("=" * 60)


if __name__ == "__main__":
    main()