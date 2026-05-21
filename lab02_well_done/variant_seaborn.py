#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Вариант 12 с использованием Seaborn (уровень Medium)
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

os.makedirs('images', exist_ok=True)

# Настройка Seaborn
sns.set_theme(style='darkgrid', palette='viridis')
sns.set_context('talk', font_scale=0.9)


def f(x):
    """
    Кусочная функция по варианту 12.
    Работает как с числами, так и с массивами.
    """
    # Сохраняем информацию о входном типе
    scalar_input = False
    if isinstance(x, (int, float)):
        scalar_input = True
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
    
    # Если вход был скаляром, возвращаем скаляр
    if scalar_input:
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
x_vals = np.linspace(-2, 1, 1000)
y_vals = f(x_vals)
x_tan = np.linspace(-1.5, -0.5, 100)
y_tan = tangent_line(x_tan, x0, y0, slope)

# Построение
fig, ax = plt.subplots(figsize=(12, 8))

# График функции
ax.plot(x_vals, y_vals, linewidth=2.5, label='f(x)', color='#2E86AB')

# Касательная
ax.plot(x_tan, y_tan, '--', linewidth=2.5, color='#D64933',
        label=f'Касательная в x₀ = {x0}')

# Точка касания
ax.scatter(x0, y0, s=200, color='#F18F01', zorder=5,
           label=f'Точка касания ({x0}, {y0:.3f})',
           edgecolors='black', linewidth=1.5)

# Вертикальная линия разрыва
ax.axvline(x=0, color='gray', linestyle=':', alpha=0.7, linewidth=2,
           label='x = 0 (разрыв)')

# Заливка областей
ax.axvspan(-2, 0, alpha=0.15, color='#A2D7FC', label='x²·sin(∛x - 3)')
ax.axvspan(0, 1, alpha=0.15, color='#A8E6CF', label='√x·cos(2x)')

# Заголовок и подписи
ax.set_title('Вариант 12: График функции и касательной\n(Seaborn оформление)',
             fontsize=14, fontweight='bold')
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('f(x)', fontsize=12)

# Легенда
ax.legend(loc='upper left', fontsize=10, frameon=True, fancybox=True, shadow=True)

# Аннотация
ax.annotate(f'Точка касания\nx₀ = {x0}\nf(x₀) = {y0:.3f}\nk = {slope:.3f}',
            xy=(x0, y0), xytext=(x0 + 0.5, y0 + 1.2),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow',
                     edgecolor='black', alpha=0.85))

# Пределы осей
ax.set_xlim(-2.2, 1.2)
ax.set_ylim(-2, 3)
ax.grid(True, alpha=0.3, linestyle='--')

# Сохранение и показ
plt.savefig('images/variant_seaborn.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.show()

print("График сохранён в images/variant_seaborn.png")