#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Вариант 12 с использованием Plotly (уровень Well-done)
Интерактивный график функции и касательной
"""

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

os.makedirs('images', exist_ok=True)


def f(x):
    """Кусочная функция по варианту 12."""
    x = np.asarray(x)
    result = np.zeros_like(x, dtype=float)
    
    mask1 = (x >= -2) & (x <= 0)
    x1 = x[mask1]
    result[mask1] = (x1 ** 2) * np.sin(np.cbrt(x1) - 3)
    
    mask2 = (x > 0) & (x <= 1)
    x2 = x[mask2]
    result[mask2] = np.sqrt(x2) * np.cos(2 * x2)
    
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
y0 = float(f(x0))
slope = float(f_derivative(x0))

print(f"Точка касания: x₀ = {x0}, f(x₀) = {y0:.4f}")
print(f"Наклон касательной: {slope:.4f}")

# Данные для графика
x_vals = np.linspace(-2, 1, 1000)
y_vals = f(x_vals)

x_tan = np.linspace(-1.5, -0.5, 100)
y_tan = tangent_line(x_tan, x0, y0, slope)

# Создаём интерактивный график
fig = make_subplots(
    rows=1, cols=1,
    subplot_titles=(f'Вариант 12: f(x) = {{ x²·sin(∛x - 3) при -2≤x≤0; √x·cos(2x) при 0<x≤1 }}',)
)

# График функции
fig.add_trace(
    go.Scatter(
        x=x_vals,
        y=y_vals,
        mode='lines',
        name='f(x)',
        line=dict(color='#2E86AB', width=3),
        hovertemplate='x = %{x:.3f}<br>f(x) = %{y:.3f}<extra></extra>'
    )
)

# Касательная
fig.add_trace(
    go.Scatter(
        x=x_tan,
        y=y_tan,
        mode='lines',
        name=f'Касательная (x₀ = {x0})',
        line=dict(color='#D64933', width=2.5, dash='dash'),
        hovertemplate='x = %{x:.3f}<br>y = %{y:.3f}<extra></extra>'
    )
)

# Точка касания
fig.add_trace(
    go.Scatter(
        x=[x0],
        y=[y0],
        mode='markers',
        name=f'Точка касания ({x0}, {y0:.3f})',
        marker=dict(color='#F18F01', size=12, symbol='circle', line=dict(color='black', width=2)),
        hovertemplate=f'x₀ = {x0}<br>f(x₀) = {y0:.4f}<br>k = {slope:.4f}<extra></extra>'
    )
)

# Вертикальная линия разрыва
fig.add_vline(
    x=0, line_width=2, line_dash="dot", line_color="gray",
    annotation_text="x = 0 (разрыв)", annotation_position="top"
)

# Заливка областей (через добавление прозрачных областей)
fig.add_hrect(
    y0=-2, y1=3, x0=-2, x1=0,
    fillcolor="#A2D7FC", opacity=0.15, line_width=0,
    annotation_text="x²·sin(∛x - 3)", annotation_position="bottom left"
)

fig.add_hrect(
    y0=-2, y1=3, x0=0, x1=1,
    fillcolor="#A8E6CF", opacity=0.15, line_width=0,
    annotation_text="√x·cos(2x)", annotation_position="bottom right"
)

# Настройка осей и заголовков
fig.update_layout(
    title={
        'text': "Вариант 12: Интерактивный график функции и касательной",
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20, 'family': 'Arial'}
    },
    xaxis_title="x",
    yaxis_title="f(x)",
    hovermode="closest",
    width=1000,
    height=700,
    legend=dict(
        x=0.01,
        y=0.99,
        bgcolor='rgba(255, 255, 255, 0.8)',
        bordercolor='black',
        borderwidth=1
    ),
    template='plotly_white'
)

# Настройка осей
fig.update_xaxes(range=[-2.2, 1.2], gridcolor='lightgray', showgrid=True)
fig.update_yaxes(range=[-2, 3], gridcolor='lightgray', showgrid=True)

# Добавляем сетку
fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray')
fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='lightgray')

# Сохраняем в HTML (интерактивный файл)
fig.write_html("images/variant_plotly_interactive.html")
print("Интерактивный график сохранён в images/variant_plotly_interactive.html")

# Сохраняем как PNG (статическое изображение)
fig.write_image("images/variant_plotly.png", width=1000, height=700, scale=2)
print("Статическое изображение сохранено в images/variant_plotly.png")

# Показываем график
fig.show()