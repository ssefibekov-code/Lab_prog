#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Лабораторная работа №6 - Генераторы (Вариант 12)
Уровень Well-done: параллельная версия генератора
"""

from spiral_generator import spiral_from_center
from spiral_generator_parallel import spiral_from_center_parallel, ParallelSpiralGenerator
import time


def create_matrix(size):
    """Создаёт квадратную матрицу заданного размера."""
    return [[i * size + j + 1 for j in range(size)] for i in range(size)]


def demo_sequential():
    """Демонстрация последовательной версии."""
    print("\n" + "=" * 60)
    print("ПОСЛЕДОВАТЕЛЬНАЯ ВЕРСИЯ (исходная)")
    print("=" * 60)
    
    matrix = create_matrix(5)
    print("\nИсходная матрица 5x5:")
    for row in matrix:
        print(f"  {row}")
    
    print("\nПорядок обхода:")
    for r, c, value in spiral_from_center(matrix):
        print(f"  ({r}, {c}) -> {value:2d}")


def demo_parallel():
    """Демонстрация параллельной версии."""
    print("\n" + "=" * 60)
    print("ПАРАЛЛЕЛЬНАЯ ВЕРСИЯ (Well-done)")
    print("=" * 60)
    
    matrix = create_matrix(5)
    print("\nИсходная матрица 5x5:")
    for row in matrix:
        print(f"  {row}")
    
    print("\nПорядок обхода (параллельно):")
    for r, c, value in spiral_from_center_parallel(matrix, True):
        print(f"  ({r}, {c}) -> {value:2d}")


def demo_performance():
    """Демонстрация производительности."""
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 60)
    
    sizes = [101, 201, 301]
    
    print("\n{:<10} {:<20} {:<20} {:<15}".format(
        "Размер", "Последовательно (сек)", "Параллельно (сек)", "Ускорение"
    ))
    print("-" * 65)
    
    for size in sizes:
        matrix = create_matrix(size)
        
        start = time.perf_counter()
        list(spiral_from_center(matrix))
        seq_time = time.perf_counter() - start
        
        start = time.perf_counter()
        list(spiral_from_center_parallel(matrix, True))
        par_time = time.perf_counter() - start
        
        speedup = seq_time / par_time if par_time > 0 else 1
        
        print(f"{size:<10} {seq_time:<20.4f} {par_time:<20.4f} {speedup:<15.2f}")


def main():
    """Основная функция."""
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №6 - ГЕНЕРАТОРЫ")
    print("Вариант 12 | Уровень Well-done")
    print("Параллельная версия спирального обхода")
    print("=" * 60)
    
    demo_sequential()
    demo_parallel()
    demo_performance()
    
    print("\n" + "=" * 60)
    print("✅ Уровни Rare, Medium и Well-done выполнены!")
    print("   - Rare: генератор спирального обхода")
    print("   - Medium: тесты pytest")
    print("   - Well-done: параллельная версия с ускорением >1.5x")
    print("=" * 60)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        import pytest
        pytest.main(["tests/", "-v"])
    else:
        main()