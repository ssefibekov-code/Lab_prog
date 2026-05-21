#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Урок 1 из книги "Библиотека Matplotlib"
Построение простого линейного графика
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# Создаём папку для изображений
os.makedirs('images', exist_ok=True)

# Создаём массив значений x от 0 до 10 с шагом 0.1
x = np.arange(0, 10, 0.1)

# Вычисляем y = sin(x) и y = cos(x)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Создаём фигуру и оси
plt.figure(figsize=(10, 6))

# Строим графики
plt.plot(x, y_sin, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y_cos, label='cos(x)', color='red', linewidth=2)

# Добавляем заголовок и подписи осей
plt.title('Графики функций sin(x) и cos(x)', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

# Добавляем сетку
plt.grid(True, alpha=0.3)

# Добавляем легенду
plt.legend(loc='upper right', fontsize=10)

# Сохраняем график
plt.savefig('images/task1_plot.png', dpi=150, bbox_inches='tight')
plt.show()

print("График сохранён в images/task1_plot.png")