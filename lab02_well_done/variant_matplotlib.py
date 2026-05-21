#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Вариант 12: 
f(x) = { x²·sin(∛x - 3), при -2 ≤ x ≤ 0
       { √x·cos(2x),      при 0 < x ≤ 1

Построение графика функции и касательной (matplotlib)
"""

import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('images', exist_ok=True)


def f(x):
    """
    Кусочная функция по варианту 12.
    Работает как с числами, так и с массивами.
    """
    # Если x - число (скаляр), преобразуем в массив
    was_scalar = np.isscalar(x)
    if was_scalar:
        x = np.array([x])
    
    result = np.zeros_like(x, dtype=float)
    
    # Первая часть: x ∈ [-2, 0]
    mask1 = (x >= -2) & (x <= 0)
    if np.any(mask1):
        x1 = x[mask1]
        result[mask1] = (x1 ** 2) * np.sin(np.cbrt(x1) - 3)
    
    # Вторая часть: x ∈ (0, 1]
    mask2 = (x > 0) & (x <= 1)
    if np.any(mask2):
        x2 = x[mask2]
        result[mask2] = np.sqrt(x2) * np.cos(2 * x2)
    
    # Если на вход было число, возвращаем число
    if was_scalar:
        return result[0]
    return result


def f_derivative(x):
    """Численное вычисление производной."""
    h = 1e-6
    return (f(x + h) - f(x - h)) / (2 * h)


def tangent_line(x, x0, y0, slope):
    """Уравнение касательной."""
    return y0 + slope * (x - x0)


# Точка касания
x0 = -1.0
y0 = f(x0)
slope = f_derivative(x0)

print(f"Точка касания: x₀ = {x0}, f(x₀) = {y0:.4f}")
print(f"Наклон касательной: {slope:.4f}")

# Данные для графика
x = np.linspace(-2, 1, 1000)
y = f(x)
x_tan = np.linspace(-1.5, -0.5, 100)
y_tan = tangent_line(x_tan, x0, y0, slope)

# Построение
plt.figure(figsize=(12, 8))
plt.style.use('seaborn-v0_8-darkgrid')

# Основной график
plt.plot(x, y, 'b-', linewidth=2.5, label='f(x)')

# Касательная
plt.plot(x_tan, y_tan, 'r--', linewidth=2, label=f'Касательная в x₀ = {x0}')

# Точка касания
plt.plot(x0, y0, 'ro', markersize=10, label=f'Точка касания ({x0}, {y0:.3f})')

# Вертикальная линия разрыва
plt.axvline(x=0, color='gray', linestyle=':', alpha=0.7, label='x = 0 (разрыв)')

# Заливка областей
plt.axvspan(-2, 0, alpha=0.1, color='lightblue', label='x²·sin(∛x - 3)')
plt.axvspan(0, 1, alpha=0.1, color='lightgreen', label='√x·cos(2x)')

plt.title('Вариант 12: f(x) = { x²·sin(∛x - 3) при -2≤x≤0; √x·cos(2x) при 0<x≤1 }', fontsize=12)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.legend(loc='best', fontsize=10)
plt.grid(True, alpha=0.3)

plt.annotate(f'x₀ = {x0}\nf(x₀) = {y0:.3f}\nk = {slope:.3f}',
             xy=(x0, y0), xytext=(x0 + 0.5, y0 + 1.2),
             arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
             bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

plt.xlim(-2.2, 1.2)
plt.ylim(-2, 3)

plt.savefig('images/variant_matplotlib.png', dpi=150, bbox_inches='tight')
plt.show()

print("График сохранён в images/variant_matplotlib.png")