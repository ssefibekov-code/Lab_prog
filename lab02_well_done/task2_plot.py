#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Урок 2 из книги "Библиотека Matplotlib"
Создание нескольких подграфиков (subplots)
"""

import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('images', exist_ok=True)

# Создаём данные
x = np.linspace(-5, 5, 100)
y1 = x ** 2
y2 = x ** 3
y3 = np.exp(x)
y4 = np.log(np.abs(x) + 0.1)

# Создаём фигуру с сеткой 2x2
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Первый подграфик: парабола
axes[0, 0].plot(x, y1, 'g-', linewidth=2)
axes[0, 0].set_title('y = x²', fontsize=12)
axes[0, 0].set_xlabel('x')
axes[0, 0].set_ylabel('y')
axes[0, 0].grid(True, alpha=0.3)

# Второй подграфик: кубическая парабола
axes[0, 1].plot(x, y2, 'r-', linewidth=2)
axes[0, 1].set_title('y = x³', fontsize=12)
axes[0, 1].set_xlabel('x')
axes[0, 1].set_ylabel('y')
axes[0, 1].grid(True, alpha=0.3)

# Третий подграфик: экспонента
axes[1, 0].plot(x, y3, 'b-', linewidth=2)
axes[1, 0].set_title('y = e^x', fontsize=12)
axes[1, 0].set_xlabel('x')
axes[1, 0].set_ylabel('y')
axes[1, 0].grid(True, alpha=0.3)

# Четвёртый подграфик: логарифм
axes[1, 1].plot(x, y4, 'm-', linewidth=2)
axes[1, 1].set_title('y = ln(|x| + 0.1)', fontsize=12)
axes[1, 1].set_xlabel('x')
axes[1, 1].set_ylabel('y')
axes[1, 1].grid(True, alpha=0.3)

# Общий заголовок
fig.suptitle('Графики элементарных функций', fontsize=16)

plt.tight_layout()
plt.savefig('images/task2_plot.png', dpi=150, bbox_inches='tight')
plt.show()

print("График сохранён в images/task2_plot.png")