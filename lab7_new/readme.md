# Прог. Лабораторная работа №7
Пакеты и модули

## Задания для самостоятельного выполнения

Сложность:    Rare

1. Создайте пакет, содержащий 3 модуля на основе лабораторных работ №№ 4-6
2. Напишите запускающий модуль на основе Typer, который позволит выбирать и настраивать параметры запуска логики из пакета.
3. Оформите отчёт в README.md. Отчёт должен содержать:
    - Условия задач
    - Описание проделанной работы
    - Скриншоты результатов
    - Ссылки на используемые материалы

## 1. Условия задач

### Задача 1 (на основе ЛР №4)
Создать модуль, реализующий:

- Рекурсивную линеаризацию вложенного списка произвольной глубины
- Итеративную линеаризацию вложенного списка с использованием стека
- Вычисление рекуррентной последовательности двумя способами (рекурсивно и итеративно):

a₁ = 1, b₁ = 1
aₖ = 2·bₖ₋₁ + aₖ₋₁
bₖ = 2·aₖ₋₁ + bₖ₋₁

### Задача 2 (на основе ЛР №5)
Создать модуль, реализующий:

- Замыкание для последовательных вычислений (аналог калькулятора с накоплением результата)
- Декоратор логирования, выводящий информацию о вызове функции
- Декоратор-ограничитель, контролирующий глубину рекурсивных вызовов

### Задача 3 (на основе ЛР №6)
Создать модуль с генератором для обхода матрицы по спирали, начиная с центрального элемента.

### Задача 4 (итоговая)
Объединить все три модуля в единый пакет и разработать CLI-интерфейс на основе библиотеки Typer для удобного запуска всех функций.

## 2. Описание проделанной работы

### 2.1 Разработка структуры пакета

lab7_new/
│
├── main.py                 # Запускающий модуль (CLI)
│
└── lab7/                   # Основной пакет
    ├── __init__.py         # Инициализация пакета
    ├── lab4.py             # Рекурсия и итерация
    ├── lab5.py             # Замыкания и декораторы
    └── lab6.py             # Спиральный обход матрицы

### 2.2 Реализация модуля lab4.py

Линеаризация списков:

```py
def linearize_recursive(nested_list):
    """Рекурсивная линеаризация"""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(linearize_recursive(item))
        else:
            result.append(item)
    return result

def linearize_iterative(nested_list):
    """Итеративная линеаризация через стек"""
    result = []
    stack = [nested_list]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            for item in reversed(current):
                stack.append(item)
        else:
            result.append(current)
    return list(reversed(result))
```

Вычисление последовательности:

```py
def a_iterative(k):
    """Итеративное вычисление a_k"""
    if k == 1:
        return 1
    a, b = 1, 1
    for _ in range(2, k + 1):
        new_a = 2 * b + a
        new_b = 2 * a + b
        a, b = new_a, new_b
    return a
```

### 2.3 Реализация модуля lab5.py
Замыкание-калькулятор:

```py
python
def make_calc(operation, initial=0):
    """Создаёт калькулятор с замыканием"""
    result = initial
    
    @log_decorator
    def calc(value):
        nonlocal result
        if operation == '+':
            result += value
        elif operation == '-':
            result -= value
        elif operation == '*':
            result *= value
        elif operation == '/':
            result /= value
        return result
    return calc
```

Декоратор-ограничитель:

```py
def call_limiter(max_calls=None):
    """Ограничивает глубину рекурсивных вызовов"""
    def decorator(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls
            if max_calls and calls >= max_calls:
                raise RuntimeError(f"Превышен лимит ({max_calls})")
            calls += 1
            try:
                return func(*args, **kwargs)
            finally:
                calls -= 1
        return wrapper
    return decorator
```

### 2.4 Реализация модуля lab6.py
Спиральный обход от центра:

```py
def spiral_from_center(matrix):
    """Генератор спирального обхода от центра"""
    rows, cols = len(matrix), len(matrix[0])
    center_r, center_c = rows // 2, cols // 2
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    r, c = center_r, center_c
    yield r, c, matrix[r][c]
    
    step_size = 1
    dir_index = 0
    visited = [[False] * cols for _ in range(rows)]
    visited[r][c] = True
    
    while True:
        for _ in range(2):
            dr, dc = directions[dir_index]
            for _ in range(step_size):
                r, c = r + dr, c + dc
                if 0 <= r < rows and 0 <= c < cols and not visited[r][c]:
                    visited[r][c] = True
                    yield r, c, matrix[r][c]
                else:
                    return
            dir_index = (dir_index + 1) % 4
        step_size += 1
```

### 2.5 Разработка CLI-интерфейса (main.py)
Создано приложение на Typer с командами:

|  Команда     |  Описание                                     |
|--------------|-----------------------------------------------|
| linearize    | Линеаризация вложенного списка                |
| sequence     | Вычисление aₖ                                 |
| compare      | Сравнение рекурсивного и итеративного методов |
| calc         | Калькулятор с замыканием                      |
| spiral       | Спиральный обход матрицы                      |
| interactive  | Интерактивный режим с меню                    |

Основной код приложения:

```py
import typer
from typing import Optional, List
from lab7 import *

app = typer.Typer(help="CLI для ЛР №4-6")

@app.command()
def linearize(list_str: str, iterative: bool = False):
    """Линеаризация списка"""
    import json
    data = json.loads(list_str)
    result = linearize_iterative(data) if iterative else linearize_recursive(data)
    typer.echo(f"Результат: {result}")

# ... остальные команды

if __name__ == "__main__":
    app()
```

## 3. Скриншоты результатов

### 3.1 Справка по командам



### 3.2 Линеаризация списка