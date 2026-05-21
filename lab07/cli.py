#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CLI интерфейс для лабораторных работ №4-6
Использует библиотеку Typer для создания командной строки
"""

import typer
from typing import Optional
import json

from lab7_package import recursion_module, closure_module, generator_module

app = typer.Typer(help="Лабораторные работы №4-6 - Рекурсия, Замыкания, Генераторы")


# ========== КОМАНДЫ ДЛЯ РЕКУРСИИ (ЛР4) ==========

@app.command()
def linearize(
    data: str = typer.Argument("[1,2,[3,4]]", help="Вложенный список в формате JSON"),
    iterative: bool = typer.Option(False, "--iterative", "-i", help="Использовать итеративную версию")
):
    """
    Линеаризация вложенного списка (ЛР4)
    
    Пример:
        python cli.py linearize "[1,2,[3,4]]"
        python cli.py linearize "[1,[2,[3,[4]]]]" --iterative
    """
    try:
        nested_list = json.loads(data.replace("'", '"'))
        if iterative:
            result = recursion_module.linearize_iterative(nested_list)
            print(f"Итеративная линеаризация: {result}")
        else:
            result = recursion_module.linearize_recursive(nested_list)
            print(f"Рекурсивная линеаризация: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
        typer.echo("Используйте формат JSON, например: [1,2,[3,4]]")


@app.command()
def sequence(
    n: int = typer.Argument(5, help="Количество членов последовательности"),
    recursive: bool = typer.Option(False, "--recursive", "-r", help="Использовать рекурсивную версию")
):
    """
    Вычисление рекуррентной последовательности a_k (ЛР4)
    
    Пример:
        python cli.py sequence 10
        python cli.py sequence 7 --recursive
    """
    if recursive:
        print(f"Рекурсивное вычисление a_k для k=1..{n}:")
        for k in range(1, n + 1):
            print(f"  a_{k} = {recursion_module.a_recursive(k)}")
    else:
        print(f"Итеративное вычисление a_k для k=1..{n}:")
        for k in range(1, n + 1):
            print(f"  a_{k} = {recursion_module.a_iterative(k)}")
    
    print(f"\nЗакономерность: a_k = 3^(k-1)")


# ========== КОМАНДЫ ДЛЯ ЗАМЫКАНИЙ (ЛР5) ==========

@app.command()
def calc(
    operation: str = typer.Argument("+", help="Операция (+, -, *, /)"),
    initial: float = typer.Option(0, "--initial", "-i", help="Начальное значение"),
    values: str = typer.Option("5,3,2", help="Значения через запятую")
):
    """
    Калькулятор с накоплением (ЛР5)
    
    Пример:
        python cli.py calc "+" --initial 10 --values "5,3,2"
        python cli.py calc "*" --initial 2 --values "3,4,5"
    """
    calc_func = closure_module.make_calc(operation, initial)
    
    print(f"Калькулятор: начальное значение = {initial}, операция = '{operation}'")
    
    for val_str in values.split(','):
        val = float(val_str.strip())
        result = calc_func(val)
        print(f"  {val} -> {result}")


@app.command()
def limit_test(
    max_calls: int = typer.Argument(3, help="Максимальное количество вызовов"),
    calls: int = typer.Option(5, help="Количество попыток вызова")
):
    """
    Тестирование декоратора call_limiter (ЛР5)
    
    Пример:
        python cli.py limit-test 3 --calls 5
    """
    from lab7_package.closure_module import call_limiter, CallLimitError
    
    @call_limiter(max_calls=max_calls)
    def test_func(msg: str) -> str:
        return f"Успешно: {msg}"
    
    print(f"Декоратор call_limiter: максимум {max_calls} одновременных вызовов")
    
    for i in range(calls):
        try:
            result = test_func(f"вызов {i+1}")
            print(f"  {result}")
        except CallLimitError as e:
            print(f"  Ошибка: {e}")


# ========== КОМАНДЫ ДЛЯ ГЕНЕРАТОРОВ (ЛР6) ==========

@app.command()
def spiral(
    size: int = typer.Argument(5, help="Размер матрицы (нечётный)"),
    max_items: int = typer.Option(25, help="Максимальное количество выводимых элементов")
):
    """
    Спиральный обход матрицы от центра (ЛР6)
    
    Пример:
        python cli.py spiral 5
        python cli.py spiral 3 --max-items 9
    """
    try:
        matrix = generator_module.create_matrix(size)
        
        print(f"Спиральный обход матрицы {size}x{size} (от центра):")
        
        count = 0
        for r, c, v in generator_module.spiral_from_center(matrix):
            if count < max_items:
                print(f"  ({r}, {c}) -> {v:2d}")
            count += 1
        
        if count > max_items:
            print(f"  ... и ещё {count - max_items} элементов")
        
        print(f"\nВсего элементов: {count}")
        
    except ValueError as e:
        print(f"Ошибка: {e}")


@app.command()
def matrix_info(size: int = typer.Argument(5, help="Размер матрицы (нечётный)")):
    """
    Информация о матрице и спиральном обходе (ЛР6)
    
    Пример:
        python cli.py matrix-info 5
    """
    try:
        matrix = generator_module.create_matrix(size)
        
        print(f"Матрица {size}x{size}:")
        for row in matrix:
            print(f"  {row}")
        
        values = list(generator_module.spiral_values(matrix))
        coords = list(generator_module.spiral_coordinates(matrix))
        
        print(f"\nПорядок обхода (координаты):")
        for i, (r, c) in enumerate(coords[:10]):
            print(f"  {i+1:2}. ({r}, {c})")
        if len(coords) > 10:
            print(f"  ... и ещё {len(coords) - 10} координат")
        
        print(f"\nЗначения в порядке обхода:")
        print(f"  {values[:10]}{'...' if len(values) > 10 else ''}")
        
    except ValueError as e:
        print(f"Ошибка: {e}")


# ========== ИНФОРМАЦИОННЫЕ КОМАНДЫ ==========

@app.command()
def info():
    """Информация о доступных командах."""
    print("=" * 60)
    print("ЛАБОРАТОРНЫЕ РАБОТЫ №4-6")
    print("=" * 60)
    print("\nДоступные команды:")
    print("  linearize    - Линеаризация вложенного списка (ЛР4)")
    print("  sequence     - Рекуррентная последовательность a_k (ЛР4)")
    print("  calc         - Калькулятор с накоплением (ЛР5)")
    print("  limit-test   - Тестирование декоратора call_limiter (ЛР5)")
    print("  spiral       - Спиральный обход матрицы (ЛР6)")
    print("  matrix-info  - Информация о матрице (ЛР6)")
    print("  info         - Показать эту справку")
    print("\nПримеры:")
    print("  python cli.py linearize '[1,2,[3,4]]'")
    print("  python cli.py sequence 10")
    print("  python cli.py calc '+' --initial 10 --values '5,3,2'")
    print("  python cli.py spiral 5")
    print("=" * 60)


@app.command()
def version():
    """Версия пакета."""
    print("Лабораторные работы №4-6 v1.0.0")


# ========== ГЛАВНАЯ ФУНКЦИЯ ==========

def main():
    app()

if __name__ == "__main__":
    main()