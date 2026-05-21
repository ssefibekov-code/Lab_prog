#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Урок 3 из книги "Библиотека Matplotlib"
Стили оформления, маркеры, цвета, толщина линий
"""

import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('images', exist_ok=True)

# Выбираем стиль
plt.style.use('seaborn-v0_8-darkgrid')

# Создаём данные
x = np.linspace(0, 10, 50)

# Разные функции с разными стилями
functions = [
    (np.sin, 'sin(x)', 'o-', 'blue', 2),
    (np.cos, 'cos(x)', 's--', 'red', 2),
    (np.tan, 'tan(x)', '^:', 'green', 1.5),
    (lambda x: np.sin(x) * np.cos(x), 'sin(x)*cos(x)', 'D-.', 'purple', 2),
]

plt.figure(figsize=(12, 7))

for func, label, marker, color, linewidth in functions:
    y = func(x)
    if label == 'tan(x)':
        y = np.clip(y, -5, 5)
    plt.plot(x, y, marker, label=label, color=color,
             linewidth=linewidth, markersize=4)

plt.title('Графики тригонометрических функций\nс различными стилями', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, alpha=0.3)
plt.ylim(-2, 2)

plt.savefig('images/task3_plot.png', dpi=150, bbox_inches='tight')
plt.show()

print("График сохранён в images/task3_plot.png")