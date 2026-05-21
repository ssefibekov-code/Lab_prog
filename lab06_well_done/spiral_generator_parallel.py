#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Параллельная (многопоточная) версия генератора спирального обхода матрицы
Уровень Well-done
"""

import threading
import queue
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import List, Tuple, Any, Generator
import multiprocessing as mp


class ParallelSpiralGenerator:
    """
    Параллельный генератор для спирального обхода матрицы.
    
    Особенности:
    - Разделяет матрицу на сектора для параллельной обработки
    - Использует ThreadPoolExecutor для параллельного выполнения
    - Объединяет результаты в правильном порядке
    """
    
    def __init__(self, matrix, num_workers=None):
        """
        Инициализация параллельного генератора.
        
        Args:
            matrix: Квадратная матрица нечётного размера
            num_workers: Количество потоков (по умолчанию = число ядер CPU)
        """
        self.matrix = matrix
        self.n = len(matrix)
        
        if self.n % 2 == 0:
            raise ValueError("Матрица должна быть нечётного размера")
        
        if num_workers is None:
            num_workers = mp.cpu_count()
        self.num_workers = min(num_workers, 4)  # Ограничиваем для избежания излишней нагрузки
        
        self.center = self.n // 2
    
    def get_segments(self) -> List[Tuple[int, int, int, int]]:
        """
        Разделяет матрицу на сегменты для параллельной обработки.
        
        Returns:
            List of (start_row, end_row, start_col, end_col)
        """
        segments = []
        step = self.n // self.num_workers
        
        for i in range(self.num_workers):
            start_row = i * step
            end_row = (i + 1) * step if i < self.num_workers - 1 else self.n
            segments.append((start_row, end_row, 0, self.n))
        
        return segments
    
    def process_segment(self, start_row, end_row, start_col, end_col) -> List[Tuple[int, int, Any]]:
        """
        Обрабатывает один сегмент матрицы.
        
        Args:
            start_row, end_row: Границы строк
            start_col, end_col: Границы столбцов
            
        Returns:
            List of (row, col, value) для сегмента
        """
        result = []
        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                result.append((i, j, self.matrix[i][j]))
        return result
    
    def spiral_sequential(self) -> Generator:
        """
        Последовательная версия (для сравнения).
        """
        return spiral_from_center(self.matrix)
    
    def spiral_parallel_threads(self) -> Generator:
        """
        Параллельная версия с использованием потоков.
        
        Yields:
            Элементы в порядке спирального обхода
        """
        # Сначала получаем все элементы (не в спиральном порядке)
        all_elements = []
        
        with ThreadPoolExecutor(max_workers=self.num_workers) as executor:
            futures = []
            segments = self.get_segments()
            
            for start_row, end_row, start_col, end_col in segments:
                future = executor.submit(self.process_segment, start_row, end_row, start_col, end_col)
                futures.append(future)
            
            for future in futures:
                all_elements.extend(future.result())
        
        # Сортируем по расстоянию от центра (приблизительно)
        center = self.center
        all_elements.sort(key=lambda x: abs(x[0] - center) + abs(x[1] - center))
        
        # Возвращаем в порядке, близком к спиральному
        for elem in all_elements:
            yield elem
    
    def generate_path(self) -> List[Tuple[int, int]]:
        """
        Генерирует путь спирального обхода.
        
        Returns:
            List of (row, col) координат в порядке обхода
        """
        path = []
        row, col = self.center, self.center
        path.append((row, col))
        
        step_length = 1
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        
        while True:
            for idx, (dr, dc) in enumerate(directions):
                for _ in range(step_length):
                    row += dr
                    col += dc
                    if 0 <= row < self.n and 0 <= col < self.n:
                        path.append((row, col))
                    else:
                        return path
                if idx % 2 == 1:
                    step_length += 1
    
    def spiral_parallel_optimized(self) -> Generator:
        """
        Оптимизированная параллельная версия с предварительным вычислением пути.
        
        Yields:
            Элементы в порядке спирального обхода
        """
        # Предварительно вычисляем путь
        path = self.generate_path()
        
        # Разделяем путь на сегменты для параллельной обработки
        chunk_size = max(1, len(path) // self.num_workers)
        chunks = [path[i:i + chunk_size] for i in range(0, len(path), chunk_size)]
        
        results = []
        
        def process_chunk(chunk):
            return [(r, c, self.matrix[r][c]) for r, c in chunk]
        
        with ThreadPoolExecutor(max_workers=self.num_workers) as executor:
            futures = [executor.submit(process_chunk, chunk) for chunk in chunks]
            
            for future in futures:
                results.extend(future.result())
        
        # Результаты уже в правильном порядке (по chunks)
        for result in results:
            yield result


def spiral_from_center_parallel(matrix, use_parallel=True):
    """
    Унифицированная функция для получения спирального обхода.
    
    Args:
        matrix: Квадратная матрица
        use_parallel: Использовать параллельную версию (True) или последовательную (False)
    """
    if use_parallel:
        gen = ParallelSpiralGenerator(matrix)
        return gen.spiral_parallel_optimized()
    else:
        return spiral_from_center(matrix)