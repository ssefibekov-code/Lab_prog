#!/usr/bin/env python3
"""
Запускающий модуль для лабораторных работ №4, №5, №6
"""

import typer
from typing import Optional, List
from enum import Enum

# Импортируем функции из нашего пакета
from lab7 import (
    linearize_recursive,
    linearize_iterative,
    a_recursive,
    a_iterative,
    make_calc,
    call_limiter,
    spiral_from_center,
    get_spiral_order,
)
from lab7 import get_sequence_a, get_sequence_b

# Создаём приложение
app = typer.Typer(help="CLI для лабораторных работ №4-6")


# ========== Команда 1: Линеаризация списка ==========
@app.command()
def linearize(
    list_str: str = typer.Argument(..., help="Список в формате JSON, например '[1,2,[3,4]]'"),
    iterative: bool = typer.Option(False, "--iterative", "-i", help="Использовать итеративный метод"),
):
    """Линеаризация вложенного списка (ЛР4)"""
    import json
    
    try:
        data = json.loads(list_str)
        if iterative:
            result = linearize_iterative(data)
            method = "итеративно"
        else:
            result = linearize_recursive(data)
            method = "рекурсивно"
        
        typer.echo(f"\n📋 Линеаризация ({method}):")
        typer.echo(f"   Вход: {data}")
        typer.echo(f"   Результат: {result}")
    except json.JSONDecodeError:
        typer.echo("Ошибка: Неверный JSON!")
        raise typer.Exit(1)


# ========== Команда 2: Вычисление a_k ==========
@app.command()
def sequence(
    k: int = typer.Argument(..., help="Номер члена последовательности (k >= 1)"),
    iterative: bool = typer.Option(False, "--iterative", "-i", help="Использовать итеративный метод"),
    show_b: bool = typer.Option(False, "--show-b", "-b", help="Показать b_k"),
):
    """Вычисление a_k рекуррентной последовательности (ЛР4)"""
    if k < 1:
        typer.echo("Ошибка: k должно быть >= 1")
        raise typer.Exit(1)
    
    if iterative:
        value = a_iterative(k)
        method = "итеративно"
    else:
        value = a_recursive(k)
        method = "рекурсивно"
    
    typer.echo(f"\n📊 a_{k} = {value} (метод: {method})")
    
    if show_b:
        b_values = get_sequence_b(k)
        typer.echo(f"   b_{k} = {b_values[-1]}")
        typer.echo(f"   a_1..a_{k} = {get_sequence_a(k)}")
        typer.echo(f"   b_1..b_{k} = {b_values}")


# ========== Команда 3: Сравнение методов ==========
@app.command()
def compare(
    k: int = typer.Argument(..., help="Номер члена последовательности"),
):
    """Сравнение рекурсивного и итеративного методов (ЛР4)"""
    import time
    
    # Итеративный метод
    start = time.perf_counter()
    iter_result = a_iterative(k)
    iter_time = time.perf_counter() - start
    
    # Рекурсивный метод
    start = time.perf_counter()
    rec_result = a_recursive(k)
    rec_time = time.perf_counter() - start
    
    typer.echo(f"\n⚖️ Сравнение методов для a_{k}:")
    typer.echo(f"   Итеративный: {iter_result} ({iter_time:.6f} сек)")
    typer.echo(f"   Рекурсивный: {rec_result} ({rec_time:.6f} сек)")
    
    if iter_result == rec_result:
        typer.echo("   ✓ Результаты совпадают")
    else:
        typer.echo("   ✗ Результаты НЕ совпадают!")


# ========== Команда 4: Калькулятор ==========
class Operation(str, Enum):
    add = "+"
    subtract = "-"
    multiply = "*"
    divide = "/"


@app.command()
def calc(
    operation: Operation = typer.Argument(..., help="Операция (+, -, *, /)"),
    initial: float = typer.Option(0.0, "--initial", "-i", help="Начальное значение"),
    values: List[float] = typer.Argument(..., help="Значения для вычислений"),
    quiet: bool = typer.Option(False, "--quiet", "-q", help="Отключить логирование"),
):
    """Последовательный калькулятор с замыканием (ЛР5)"""
    import sys
    from io import StringIO
    
    orig_stdout = sys.stdout
    if quiet:
        sys.stdout = StringIO()
    
    try:
        calc_func = make_calc(operation.value, initial=initial)
        for v in values:
            calc_func(v)
        
        if quiet:
            sys.stdout = orig_stdout
        
        typer.echo(f"\n🧮 Результат: {calc_func(0)}")
    except Exception as e:
        sys.stdout = orig_stdout
        typer.echo(f"Ошибка: {e}")
        raise typer.Exit(1)


# ========== Команда 5: Спиральный обход ==========
@app.command()
def spiral(
    rows: int = typer.Option(5, "--rows", "-r", help="Количество строк"),
    cols: int = typer.Option(5, "--cols", "-c", help="Количество столбцов"),
):
    """Спиральный обход матрицы от центра (ЛР6)"""
    # Создаём матрицу с числами
    matrix = [[i * cols + j + 1 for j in range(cols)] for i in range(rows)]
    
    typer.echo(f"\n🔄 Спиральный обход матрицы {rows}x{cols}:")
    
    for i, (r, c, val) in enumerate(spiral_from_center(matrix), 1):
        typer.echo(f"   {i:3d}. ({r}, {c}) -> {val:3d}")


# ========== Интерактивный режим ==========
@app.command()
def interactive():
    """Интерактивный режим с меню"""
    typer.echo("\n" + "=" * 50)
    typer.echo("   Лабораторные работы №4, №5, №6")
    typer.echo("   Рекурсия | Замыкания | Генераторы")
    typer.echo("=" * 50)
    
    while True:
        typer.echo("\nВыберите действие:")
        typer.echo("  1. Линеаризация списка")
        typer.echo("  2. Вычисление a_k")
        typer.echo("  3. Сравнение методов")
        typer.echo("  4. Калькулятор")
        typer.echo("  5. Спиральный обход")
        typer.echo("  0. Выход")
        
        choice = typer.prompt("Ваш выбор", default="0")
        
        if choice == "0":
            typer.echo("До свидания!")
            break
        elif choice == "1":
            lst = typer.prompt("Введите список (JSON)", default="[1,2,[3,4,5]]")
            use_iter = typer.confirm("Использовать итеративный метод?", default=False)
            linearize(lst, iterative=use_iter)
        elif choice == "2":
            k = typer.prompt("Введите k", type=int)
            use_iter = typer.confirm("Использовать итеративный метод?", default=False)
            show = typer.confirm("Показать b_k?", default=False)
            sequence(k, iterative=use_iter, show_b=show)
        elif choice == "3":
            k = typer.prompt("Введите k", type=int)
            compare(k)
        elif choice == "4":
            op = typer.prompt("Операция (+, -, *, /)", default="+")
            init = typer.prompt("Начальное значение", type=float, default=0)
            vals = typer.prompt("Значения через запятую", default="1,2,3")
            values = [float(x.strip()) for x in vals.split(",")]
            calc(op, initial=init, values=values, quiet=True)
        elif choice == "5":
            rows = typer.prompt("Количество строк", type=int, default=5)
            cols = typer.prompt("Количество столбцов", type=int, default=5)
            spiral(rows=rows, cols=cols)
        else:
            typer.echo("Неверный выбор!")


# ========== Главная функция ==========
def main():
    app()


if __name__ == "__main__":
    main()