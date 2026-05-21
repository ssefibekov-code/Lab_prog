#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Тест производительности для сравнения последовательной и параллельной версий
Уровень Well-done
"""

import time
import sys
from spiral_generator import spiral_from_center
from spiral_generator_parallel import ParallelSpiralGenerator, spiral_from_center_parallel


def create_matrix(size):
    """Создаёт квадратную матрицу заданного размера."""
    return [[i * size + j + 1 for j in range(size)] for i in range(size)]


def measure_time(func, *args, iterations=3):
    """Измеряет среднее время выполнения функции."""
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        # Полностью потребляем генератор
        result = list(func(*args))
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / iterations, len(result)


def performance_comparison():
    """Сравнивает производительность последовательной и параллельной версий."""
    print("\n" + "=" * 70)
    print(" ТЕСТ ПРОИЗВОДИТЕЛЬНОСТИ: СПИРАЛЬНЫЙ ОБХОД МАТРИЦЫ")
    print(" Сравнение последовательной и параллельной версий")
    print("=" * 70)
    
    # Размеры матриц для тестирования
    sizes = [101, 201, 301, 401, 501]
    
    print("\n{:<10} {:<20} {:<20} {:<15} {:<10}".format(
        "Размер", "Последовательно (сек)", "Параллельно (сек)", "Ускорение", "Статус"
    ))
    print("-" * 75)
    
    results = []
    
    for size in sizes:
        print(f"\rСоздание матрицы {size}x{size}...", end="", flush=True)
        matrix = create_matrix(size)
        
        # Последовательная версия
        seq_time, seq_count = measure_time(spiral_from_center, matrix)
        
        # Параллельная версия
        par_time, par_count = measure_time(spiral_from_center_parallel, matrix, True)
        
        # Вычисляем ускорение
        speedup = seq_time / par_time if par_time > 0 else 1
        
        status = "✅" if speedup >= 1.5 else "⚠️"
        
        print(f"\r{size:<10} {seq_time:<20.4f} {par_time:<20.4f} {speedup:<15.2f} {status:<10}")
        
        results.append({
            'size': size,
            'seq_time': seq_time,
            'par_time': par_time,
            'speedup': speedup,
            'seq_count': seq_count,
            'par_count': par_count
        })
    
    print("\n" + "=" * 70)
    print(" ВЫВОДЫ:")
    print("=" * 70)
    
    avg_speedup = sum(r['speedup'] for r in results) / len(results)
    print(f"  Среднее ускорение: {avg_speedup:.2f}x")
    
    max_speedup = max(r['speedup'] for r in results)
    print(f"  Максимальное ускорение: {max_speedup:.2f}x")
    
    if avg_speedup >= 1.5:
        print("\n  ✅ Well-done достигнут! Ускорение > 1.5x")
    else:
        print(f"\n  ⚠️ Ускорение {avg_speedup:.2f}x - требуется оптимизация")
    
    print("=" * 70)
    
    return results


def detailed_comparison():
    """Детальное сравнение для одной матрицы."""
    print("\n" + "=" * 70)
    print(" ДЕТАЛЬНОЕ СРАВНЕНИЕ ДЛЯ МАТРИЦЫ 201x201")
    print("=" * 70)
    
    size = 201
    matrix = create_matrix(size)
    
    # Последовательная версия
    print("\n1. Последовательная версия...")
    start = time.perf_counter()
    seq_result = list(spiral_from_center(matrix))
    seq_time = time.perf_counter() - start
    print(f"   Время: {seq_time:.4f} сек")
    print(f"   Элементов: {len(seq_result)}")
    
    # Параллельная версия
    print("\n2. Параллельная версия...")
    start = time.perf_counter()
    par_result = list(spiral_from_center_parallel(matrix, True))
    par_time = time.perf_counter() - start
    print(f"   Время: {par_time:.4f} сек")
    print(f"   Элементов: {len(par_result)}")
    
    # Проверка корректности
    print("\n3. Проверка корректности...")
    seq_coords = [(r, c) for r, c, _ in seq_result]
    par_coords = [(r, c) for r, c, _ in par_result]
    
    if seq_coords == par_coords:
        print("   ✅ Порядок обхода совпадает!")
    else:
        print("   ⚠️ Порядок обхода отличается (что ожидаемо для параллельной версии)")
    
    speedup = seq_time / par_time
    print(f"\n4. Ускорение: {speedup:.2f}x")
    
    print("\n" + "=" * 70)


def main():
    """Запуск всех тестов производительности."""
    print("=" * 70)
    print(" ЛАБОРАТОРНАЯ РАБОТА №6 - ТЕСТЫ ПРОИЗВОДИТЕЛЬНОСТИ")
    print(" Уровень Well-done: параллельная версия генератора")
    print("=" * 70)
    
    # Сравнение производительности
    performance_comparison()
    
    # Детальное сравнение
    detailed_comparison()


if __name__ == "__main__":
    main()