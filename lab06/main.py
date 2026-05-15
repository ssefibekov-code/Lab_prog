#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Лабораторная работа №6 - Генераторы (Вариант 12)
Демонстрация работы генератора спирального обхода матрицы
"""

from spiral_generator import spiral_from_center, spiral_values, spiral_coordinates


def demo_5x5_matrix():
    """Демонстрация работы на матрице 5x5."""
    print("\n" + "=" * 60)
    print("МАТРИЦА 5x5 (числа от 1 до 25)")
    print("=" * 60)
    
    matrix = [
        [ 1,  2,  3,  4,  5],
        [ 6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    
    # Вывод исходной матрицы
    print("\nИсходная матрица:")
    for row in matrix:
        print(f"  {row}")
    
    # Спиральный обход
    print("\nПорядок обхода (ряд, столбец) -> значение:")
    for r, c, value in spiral_from_center(matrix):
        print(f"  ({r}, {c}) -> {value:2d}")


def demo_3x3_matrix():
    """Демонстрация работы на матрице 3x3."""
    print("\n" + "=" * 60)
    print("МАТРИЦА 3x3 (числа от 1 до 9)")
    print("=" * 60)
    
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("\nИсходная матрица:")
    for row in matrix:
        print(f"  {row}")
    
    print("\nПорядок обхода:")
    result = list(spiral_from_center(matrix))
    for r, c, value in result:
        print(f"  ({r}, {c}) -> {value}")
    
    print(f"\nВсего элементов: {len(result)}")
    print(f"Ожидалось: {len(matrix) * len(matrix)}")


def demo_7x7_matrix():
    """Демонстрация работы на матрице 7x7."""
    print("\n" + "=" * 60)
    print("МАТРИЦА 7x7 (числа от 1 до 49)")
    print("=" * 60)
    
    # Создаём матрицу 7x7 с числами от 1 до 49
    matrix = [[i * 7 + j + 1 for j in range(7)] for i in range(7)]
    
    print("\nИсходная матрица:")
    for row in matrix:
        print(f"  {row}")
    
    print("\nПорядок обхода (первые 25 элементов):")
    count = 0
    for r, c, value in spiral_from_center(matrix):
        print(f"  ({r}, {c}) -> {value:2d}")
        count += 1
        if count >= 25:
            print("  ...")
            break
    
    # Вывод количества элементов
    total = len(list(spiral_from_center(matrix)))
    print(f"\nВсего элементов в матрице: 7x7 = {total}")


def demo_error_handling():
    """Демонстрация обработки ошибок."""
    print("\n" + "=" * 60)
    print("ОБРАБОТКА ОШИБОК")
    print("=" * 60)
    
    # Матрица чётного размера
    print("\n1. Матрица 4x4 (чётный размер):")
    matrix_even = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    try:
        list(spiral_from_center(matrix_even))
    except ValueError as e:
        print(f"   Ошибка: {e}")
    
    # Неквадратная матрица
    print("\n2. Неквадратная матрица:")
    matrix_rect = [[1, 2, 3], [4, 5, 6]]
    try:
        list(spiral_from_center(matrix_rect))
    except ValueError as e:
        print(f"   Ошибка: {e}")
    
    # Пустая матрица
    print("\n3. Пустая матрица:")
    matrix_empty = []
    try:
        list(spiral_from_center(matrix_empty))
    except ValueError as e:
        print(f"   Ошибка: {e}")


def demo_helper_generators():
    """Демонстрация вспомогательных генераторов."""
    print("\n" + "=" * 60)
    print("ВСПОМОГАТЕЛЬНЫЕ ГЕНЕРАТОРЫ")
    print("=" * 60)
    
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("\n1. spiral_values() - только значения:")
    values = list(spiral_values(matrix))
    print(f"   {values}")
    
    print("\n2. spiral_coordinates() - только координаты:")
    coords = list(spiral_coordinates(matrix))
    print(f"   {coords}")


def demo_custom_matrix():
    """Демонстрация на пользовательской матрице."""
    print("\n" + "=" * 60)
    print("ПОЛЬЗОВАТЕЛЬСКАЯ МАТРИЦА 5x5")
    print("=" * 60)
    
    # Пользовательская матрица с разными значениями
    matrix = [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'J'],
        ['K', 'L', 'M', 'N', 'O'],
        ['P', 'Q', 'R', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'Y']
    ]
    
    print("\nИсходная матрица:")
    for row in matrix:
        print(f"  {row}")
    
    print("\nСпиральный обход (только значения):")
    values = list(spiral_values(matrix))
    print(f"  {values}")


def main():
    """Основная функция."""
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №6 - ГЕНЕРАТОРЫ")
    print("Вариант 12: Спиральный обход матрицы от центра")
    print("=" * 60)
    
    demo_3x3_matrix()
    demo_5x5_matrix()
    demo_7x7_matrix()
    demo_custom_matrix()
    demo_error_handling()
    demo_helper_generators()
    
    print("\n" + "=" * 60)
    print("✅ Уровни Rare и Medium выполнены!")
    print("=" * 60)
    print("\nЗапуск тестов: pytest test_spiral_generator.py -v")
    print("=" * 60)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        import pytest
        pytest.main(["test_spiral_generator.py", "-v", "--tb=short"])
    else:
        main()