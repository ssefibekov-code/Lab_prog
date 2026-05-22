#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CLI интерфейс для лабораторной работы №7
На основе библиотеки Typer
"""

import typer
from typing import Optional
import json

from lab7_package import (
    linearize_recursive, linearize_iterative,
    a_iterative, get_sequence_a,
    make_calc,
    spiral_from_center, get_spiral_order
)

app = typer.Typer(help="Лабораторная работа №7 - Пакеты и модули")


# ========== ЛР4: Рекурсия ==========

@app.command()
def linearize(
    data: str = typer.Argument("[1,2,[3,4,[5,6]]]", help="Вложенный список"),
    iterative: bool = typer.Option(False, "--iterative", "-i", help="Использовать итеративный метод")
):
    """Линеаризация вложенного списка."""
    try:
        nested_list = eval(data)
        if iterative:
            result = linearize_iterative(nested_list)
            method = "итеративный"
        else:
            result = linearize_recursive(nested_list)
            method = "рекурсивный"
        
        typer.echo(f"Исходный список: {nested_list}")
        typer.echo(f"Результат ({method}): {result}")
    except Exception as e:
        typer.echo(f"Ошибка: {e}", err=True)


@app.command()
def sequence(
    n: int = typer.Argument(10, help="Количество членов последовательности")
):
    """Вычисление последовательности a_k."""
    values = get_sequence_a(n)
    typer.echo(f"Первые {n} членов последовательности a_k:")
    for i, val in enumerate(values, 1):
        typer.echo(f"  a_{i} = {val}")


# ========== ЛР5: Замыкания ==========

@app.command()
def calc(
    operation: str = typer.Argument("+", help="Операция (+, -, *, /)"),
    initial: float = typer.Argument(0.0, help="Начальное значение"),
    values: str = typer.Argument("5,3,2", help="Значения через запятую")
):
    """Калькулятор с накоплением."""
    try:
        vals = [float(x.strip()) for x in values.split(',')]
        calculator = make_calc(operation, initial)
        
        typer.echo(f"Калькулятор: {operation} (начально = {initial})")
        current = initial
        for v in vals:
            current = calculator(v)
            typer.echo(f"  {v} -> {current}")
    except Exception as e:
        typer.echo(f"Ошибка: {e}", err=True)


# ========== ЛР6: Генераторы ==========

@app.command()
def spiral(
    size: int = typer.Argument(5, help="Размер матрицы (нечётный)"),
    show_matrix: bool = typer.Option(True, "--show-matrix", "-m", help="Показать исходную матрицу")
):
    """Спиральный обход матрицы от центра."""
    try:
        if size % 2 == 0:
            typer.echo("Размер матрицы должен быть нечётным!", err=True)
            raise typer.Exit(1)
        
        # Создаём матрицу
        matrix = [[i * size + j + 1 for j in range(size)] for i in range(size)]
        
        if show_matrix:
            typer.echo("Исходная матрица:")
            for row in matrix:
                typer.echo(f"  {row}")
        
        typer.echo("\nПорядок обхода:")
        for r, c, val in spiral_from_center(matrix):
            typer.echo(f"  ({r}, {c}) -> {val}")
            
    except Exception as e:
        typer.echo(f"Ошибка: {e}", err=True)


@app.command()
def info():
    """Информация о пакете."""
    typer.echo("=" * 50)
    typer.echo("Лабораторная работа №7 - Пакеты и модули")
    typer.echo("=" * 50)
    typer.echo("\nДоступные команды:")
    typer.echo("  linearize    - Линеаризация списков (ЛР4)")
    typer.echo("  sequence     - Рекуррентная последовательность (ЛР4)")
    typer.echo("  calc         - Калькулятор с накоплением (ЛР5)")
    typer.echo("  spiral       - Спиральный обход матрицы (ЛР6)")
    typer.echo("  info         - Эта справка")


if __name__ == "__main__":
    app()