# Лабораторная работа №2 - Построение графиков в Python

## Уровень сложности: Well-done

---

## 1. Цель работы

Изучение библиотек для визуализации данных в Python на трёх уровнях сложности:
- **Rare**: построение статических графиков с использованием `matplotlib`
- **Medium**: улучшенная визуализация с использованием `seaborn`
- **Well-done**: создание интерактивных графиков с использованием `plotly`

---

## 2. Задачи лабораторной работы

| Уровень | Задание | Статус |
|---------|---------|--------|
| **Rare** | Выполнение уроков 1-3 из книги "Библиотека Matplotlib" | ✅ |
| **Rare** | Построение графика кусочной функции по варианту 12 | ✅ |
| **Rare** | Построение касательной к графику функции | ✅ |
| **Rare** | Оформление графика (заголовок, подписи, легенда, сетка, аннотация) | ✅ |
| **Medium** | Построение графика с использованием `seaborn` | ✅ |
| **Well-done** | Создание интерактивного графика с помощью `plotly` | ✅ |
| **Well-done** | Сохранение графика в HTML-формате | ✅ |
| **Well-done** | Написание тестов pytest | ✅ |

---

## 3. Выполненные задания

### 3.1. Уроки из книги (Rare)

#### Урок 1. Построение линейных графиков

Построены графики функций `sin(x)` и `cos(x)` на интервале `[0, 10]`.

**Код:**
```python
x = np.arange(0, 10, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y_cos, label='cos(x)', color='red', linewidth=2)

plt.title('Графики функций sin(x) и cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('images/task1_plot.png')
```

#### Урок 2. Создание нескольких подграфиков

Создана сетка подграфиков 2×2 с графиками элементарных функций.

**Код:**
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, y1, 'g-', linewidth=2)
axes[0, 1].plot(x, y2, 'r-', linewidth=2)
axes[1, 0].plot(x, y3, 'b-', linewidth=2)
axes[1, 1].plot(x, y4, 'm-', linewidth=2)
plt.savefig('images/task2_plot.png')
```

#### Урок 3. Стили оформления

Изучены различные стили линий, маркеры, цвета и толщина линий.

**Код:**
```python
plt.style.use('seaborn-v0_8-darkgrid')
functions = [
    (np.sin, 'sin(x)', 'o-', 'blue', 2),
    (np.cos, 'cos(x)', 's--', 'red', 2),
    (np.tan, 'tan(x)', '^:', 'green', 1.5),
]
plt.savefig('images/task3_plot.png')
```

---

### 3.2. Реализация варианта 12

**Кусочная функция:**
```python
def f(x):
    scalar_input = isinstance(x, (int, float))
    if scalar_input:
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
    
    return result[0] if scalar_input else result
```

**Вычисление касательной:**
```python
def f_derivative(x):
    h = 1e-6
    return (f(x + h) - f(x - h)) / (2 * h)

def tangent_line(x, x0, y0, slope):
    return y0 + slope * (x - x0)
```

**Результаты вычислений:**

| Параметр | Значение |
|----------|----------|
| Точка касания (x₀) | -1.0 |
| f(x₀) | -0.7568 |
| Наклон касательной (k) | -0.6536 |

---

### 3.3. Версии графиков

#### Matplotlib версия (Rare)

**Особенности оформления:**
- Заголовок с математической формулой
- Подписи осей
- Легенда
- Сетка
- Аннотация точки касания
- Вертикальная линия в точке разрыва (x = 0)
- Заливка областей для наглядности

**Код:**
```python
plt.figure(figsize=(12, 8))
plt.style.use('seaborn-v0_8-darkgrid')
plt.plot(x_vals, y_vals, 'b-', linewidth=2.5, label='f(x)')
plt.plot(x_tan, y_tan, 'r--', linewidth=2, label=f'Касательная в x₀ = {x0}')
plt.plot(x0, y0, 'ro', markersize=10, label=f'Точка касания ({x0}, {y0:.3f})')
plt.axvline(x=0, color='gray', linestyle=':', alpha=0.7, label='x = 0 (разрыв)')
plt.axvspan(-2, 0, alpha=0.1, color='lightblue')
plt.axvspan(0, 1, alpha=0.1, color='lightgreen')
plt.savefig('images/variant_matplotlib.png')
```

#### Seaborn версия (Medium)

**Особенности оформления:**
- Улучшенная цветовая схема (палитра viridis)
- Современный стиль (darkgrid)
- Увеличенный размер шрифтов
- Тень и рамка у легенды

**Код:**
```python
sns.set_theme(style='darkgrid', palette='viridis')
sns.set_context('talk', font_scale=0.9)

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x_vals, y_vals, linewidth=2.5, label='f(x)', color='#2E86AB')
ax.plot(x_tan, y_tan, '--', linewidth=2.5, color='#D64933')
ax.scatter(x0, y0, s=200, color='#F18F01', zorder=5)
plt.savefig('images/variant_seaborn.png')
```

#### Plotly версия (Well-done)

**Интерактивные возможности:**
- Масштабирование (zoom) — выделение области
- Панорамирование (pan) — перемещение по графику
- Наведение (hover) — отображение координат
- Выбор линий — включение/отключение через легенду
- Сброс масштаба — двойной клик
- Сохранение в PNG — кнопка на панели инструментов

**Код:**
```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x_vals, y=y_vals,
    mode='lines', name='f(x)',
    line=dict(color='#2E86AB', width=3),
    hovertemplate='x = %{x:.3f}<br>f(x) = %{y:.3f}<extra></extra>'
))

fig.add_trace(go.Scatter(
    x=x_tan, y=y_tan,
    mode='lines', name=f'Касательная (x₀ = {x0})',
    line=dict(color='#D64933', width=2.5, dash='dash')
))

fig.add_trace(go.Scatter(
    x=[x0], y=[y0],
    mode='markers', name=f'Точка касания ({x0}, {y0:.3f})',
    marker=dict(color='#F18F01', size=12, symbol='circle')
))

fig.add_vline(x=0, line_width=2, line_dash="dot", line_color="gray")

fig.write_html("images/variant_plotly_interactive.html")
fig.write_image("images/variant_plotly.png")
```

---

## 4. Сравнение библиотек визуализации

| Характеристика | Matplotlib | Seaborn | Plotly |
|----------------|------------|---------|--------|
| Тип графиков | Статические | Статические | Интерактивные |
| Сложность использования | Средняя | Низкая | Средняя |
| Качество по умолчанию | Хорошее | Отличное | Отличное |
| Интерактивность | ❌ | ❌ | ✅ |
| Масштабирование | ❌ | ❌ | ✅ |
| Сохранение в HTML | ❌ | ❌ | ✅ |
| Hover-подсказки | ❌ | ❌ | ✅ |

---

## 5. Ход выполнения работы

### 5.1. Настройка окружения

```bash
# Создание виртуального окружения
python -m venv .venv

# Активация
.venv\Scripts\activate

# Установка пакетов
pip install matplotlib numpy seaborn plotly kaleido

# Сохранение зависимостей
pip freeze > requirements.txt
```

### 5.2. Реализация кусочной функции

Особое внимание было уделено корректной обработке как скалярных, так и векторных входных данных. Использованы маски NumPy для эффективного вычисления на массивах.

### 5.3. Построение графиков

Для каждого уровня сложности создан отдельный скрипт:
- `variant_matplotlib.py` — статический график (Rare)
- `variant_seaborn.py` — улучшенный статический график (Medium)
- `variant_plotly.py` — интерактивный график (Well-done)

## 6. Выводы

### Результаты выполнения:

| Уровень | Статус | Описание |
|---------|--------|----------|
| **Rare** | ✅ | Выполнены уроки 1-3, построен график в matplotlib |
| **Medium** | ✅ | Построен улучшенный график в seaborn |
| **Well-done** | ✅ | Создан интерактивный график в plotly с сохранением в HTML |

### Полученные навыки:
- Работа с библиотеками визуализации `matplotlib`, `seaborn`, `plotly`
- Реализация кусочных функций с использованием масок NumPy
- Численное дифференцирование для построения касательных
- Создание интерактивных HTML-графиков
- Оформление графиков (заголовки, легенды, аннотации, сетка)
- Написание тестов для проверки визуализации

### Преимущества интерактивных графиков (Well-done):
- Возможность детального анализа данных через масштабирование
- Удобство использования для презентаций и отчётов
- Доступность через любой веб-браузер
- Сохранение всех интерактивных возможностей в HTML-файле

---

## 7. Запуск программы

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск уроков
python task1_plot.py
python task2_plot.py
python task3_plot.py

# Запуск варианта 12 (Rare)
python variant_matplotlib.py

# Запуск варианта 12 (Medium)
python variant_seaborn.py

# Запуск варианта 12 (Well-done)
python variant_plotly.py

# Запуск тестов
pytest tests/ -v
```

---

## 8. Сохранённые файлы

| Файл | Описание |
|------|----------|
| `images/task1_plot.png` | График sin(x) и cos(x) |
| `images/task2_plot.png` | Четыре подграфика |
| `images/task3_plot.png` | Стили и маркеры |
| `images/variant_matplotlib.png` | График варианта (matplotlib) |
| `images/variant_seaborn.png` | График варианта (seaborn) |
| `images/variant_plotly.png` | Статический скриншот (plotly) |
| `images/variant_plotly_interactive.html` | Интерактивный график |

---

## 9. Список использованных материалов

1. **Matplotlib Documentation** — https://matplotlib.org/
2. **Seaborn Documentation** — https://seaborn.pydata.org/
3. **Plotly Documentation** — https://plotly.com/python/
4. **NumPy Documentation** — https://numpy.org/doc/stable/
5. **Devpractice Team. Библиотека Matplotlib**

