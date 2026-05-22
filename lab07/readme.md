# Прог. Лабораторная работа №7

Генераторы

## Задания для самостоятельного выполнения

### **Сложность**:    *Rare*

1. Создайте пакет, содержащий 3 модуля на основе лабораторных работ №№ 4-6

2. Напишите запускающий модуль на основе Typer, который позволит выбирать и настраивать параметры запуска логики из пакета.

2. Оформите отчёт в README.md. Отчёт должен содержать:
- Условия задач
- Описание проделанной работы
- Скриншоты результатов
- Ссылки на используемые материалы

### **Сложность**:      *Medium*

- Реализуйте GUI приложение на одном из актуальных фреймворков

## Ход работы:

### 1. Написание программ 

- отчёт выполнен в lab7

### 2 Изменения в лабораторных работах при переходе на новый уровень сложности

Лабораторная работа №7 - Пакеты и модули
Общая концепция
Лабораторная работа №7 объединяет результаты предыдущих работ (№4, №5, №6) в единый пакет, добавляя CLI и GUI интерфейсы.

#### 1. Лабораторная работа №4 → Модуль recursion_module.py

Было (ЛР4 - Rare):
```python
# Код был просто скриптом
def linearize_recursive(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(linearize_recursive(item))
        else:
            result.append(item)
    return result

if __name__ == "__main__":
    print(linearize_recursive([1, 2, [3, 4]]))
```

Стало (ЛР7 - модуль):
```python
# Код обёрнут в модуль с экспортируемыми функциями
def linearize_recursive(nested_list):
    """Рекурсивная линеаризация вложенного списка."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(linearize_recursive(item))
        else:
            result.append(item)
    return result

def linearize_iterative(nested_list):
    """Итеративная линеаризация вложенного списка."""
    if not nested_list:
        return []
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

# Добавлены вспомогательные функции
def get_sequence_values(n):
    return [a_iterative(k) for k in range(1, n + 1)]

# Демонстрационные функции
def demo_linearize():
    test_list = [1, 2, [3, 4, [5, [6, []]]]]
    return {
        'original': test_list,
        'recursive': linearize_recursive(test_list),
        'iterative': linearize_iterative(test_list)
    }
```

#### Основные изменения:
|Аспект          |	ЛР4 (Rare)  |	ЛР7 (модуль) |
|----------------|--------------|----------------|
|Назначение|	Самостоятельный скрипт|	Импортируемый модуль|
|Функции|	Только основные|	+ вспомогательные, + демо|
|Документация|	Минимальная|	Полные docstring|
|Экспорт|	Не требуется|	Все функции доступны|

### 2. Лабораторная работа №5 → Модуль closure_module.py

Было (ЛР5 - Rare):
```python
def make_calc(operation, initial=0):
    result = initial
    def calc(value):
        nonlocal result
        if operation == '+':
            result += value
        # ...
        return result
    return calc

def call_limiter(max_calls=None):
    def decorator(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls
            if max_calls is not None and calls >= max_calls:
                raise Exception("Превышено максимальное количество вызовов")
            calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

Стало (ЛР7 - модуль):
```python
# Добавлено пользовательское исключение
class CallLimitError(Exception):
    """Исключение при превышении лимита вызовов."""
    pass

def call_limiter(max_calls=None):
    def decorator(func):
        calls = 0
        def wrapper(*args, **kwargs):
            nonlocal calls
            if max_calls is not None and calls >= max_calls:
                raise CallLimitError(
                    f"Превышено максимальное количество вызовов ({max_calls}) "
                    f"для функции '{func.__name__}'"
                )
            calls += 1
            try:
                return func(*args, **kwargs)
            finally:
                calls -= 1
        return wrapper
    return decorator

# Добавлена обработка деления на ноль
def make_calc(operation, initial=0):
    # ...
    def calc(value):
        nonlocal result
        if operation == '/':
            if value == 0:
                raise ValueError("Деление на ноль!")
        # ...

# Добавлены демонстрационные функции
def demo_calculator():
    calc_add = make_calc("+", initial=10)
    return [calc_add(5), calc_add(3)]
```

#### Основные изменения:

|Аспект|	ЛР5 (Rare)|	ЛР7 (модуль)|
|----------------|--------------|----------------|
|Исключения|	Общее Exception|	Специфичное CallLimitError|
|Обработка ошибок|	Отсутствует|	Добавлена проверка деления на 0|
|Информативность|	Минимальная|	Подробные сообщения об ошибках|
|Тестирование|	Встроенное|	Отдельные демо-функции|

### 3. Лабораторная работа №6 → Модуль generator_module.py

Было (ЛР6 - Rare):
```python
def spiral_from_center(matrix):
    n = len(matrix)
    if n % 2 == 0:
        raise ValueError("Матрица должна быть нечётного размера")
    # ... генератор
```

Стало (ЛР7 - модуль):
```python
def spiral_from_center(matrix):
    # Добавлена проверка на квадратность матрицы
    if not matrix or not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("Матрица должна быть квадратной")
    
    n = len(matrix)
    if n % 2 == 0:
        raise ValueError("Матрица должна быть нечётного размера")
    # ...

# Добавлены вспомогательные генераторы
def spiral_values(matrix):
    """Возвращает только значения элементов."""
    for _, _, value in spiral_from_center(matrix):
        yield value

def spiral_coordinates(matrix):
    """Возвращает только координаты элементов."""
    for row, col, _ in spiral_from_center(matrix):
        yield row, col

# Добавлена функция создания матриц
def create_matrix(n, fill_type='numbers'):
    """Создаёт квадратную матрицу нечётного размера."""
    if n % 2 == 0:
        raise ValueError("Размер матрицы должен быть нечётным")
    
    if fill_type == 'numbers':
        return [[i * n + j + 1 for j in range(n)] for i in range(n)]
    elif fill_type == 'letters':
        import string
        letters = string.ascii_uppercase
        return [[letters[(i * n + j) % len(letters)] for j in range(n)] for i in range(n)]
    # ...

# Добавлена демонстрационная функция
def demo_spiral(matrix_size=5):
    matrix = create_matrix(matrix_size, 'numbers')
    return list(spiral_from_center(matrix))
```

#### Основные изменения:

|Аспект |	ЛР6 (Rare)| 	ЛР7 (модуль)|
|----------------|--------------|----------------|
|Валидация|	Только размер|	+ квадратность, + пустая матрица|
|Вспомогательные генераторы|	Нет	|spiral_values, spiral_coordinates|
|Создание матриц|	Ручное|	Автоматическое (create_matrix)|
|Типы данных|	Только числа|	Числа, буквы|


### 4. Создание CLI интерфейса (Typer) - Новый уровень

Было (ЛР4-6):
```python
# Только консольный вывод
if __name__ == "__main__":
    print(linearize_recursive([1, 2, [3, 4]]))
```
Стало (ЛР7 - CLI):
```python
# Полноценный CLI с аргументами
import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer()

@app.command()
def linearize(data: str = typer.Argument("[1,2,[3,4]]")):
    """Линеаризация вложенного списка."""
    nested_list = eval(data)
    result = recursion_module.linearize_recursive(nested_list)
    console.print(f"[green]Результат:[/green] {result}")

@app.command()
def sequence(n: int = typer.Argument(10)):
    """Вычисление последовательности a_k."""
    table = Table(title="Значения a_k")
    table.add_column("k", style="cyan")
    table.add_column("a_k", style="green")
    # ...
    console.print(table)

if __name__ == "__main__":
    app()
```

### Создание GUI интерфейса (tkinter) - Уровень MediumБыло (ЛР4-6):

```python
# Только консоль
print(f"Результат: {result}")
```
Стало (ЛР7 - GUI):
```python
# Полноценное графическое приложение
import tkinter as tk
from tkinter import ttk, scrolledtext

class Lab7App:
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторная работа №7")
        
        # Создание вкладок
        self.notebook = ttk.Notebook(root)
        self.create_recursion_tab()
        self.create_closure_tab()
        self.create_generator_tab()
        
    def create_recursion_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Рекурсия")
        
        # Поле ввода
        self.linearize_entry = ttk.Entry(tab, width=80)
        self.linearize_entry.pack()
        
        # Кнопка
        ttk.Button(tab, text="Вычислить", 
                   command=self.on_linearize).pack()
        
        # Поле вывода
        self.result_text = scrolledtext.ScrolledText(tab, height=10)
        self.result_text.pack()
    
    def on_linearize(self):
        data = eval(self.linearize_entry.get())
        result = recursion_module.linearize_recursive(data)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, str(result))
```

Новые возможности:

|Функция|	Описание|
|----------------|--------------|
|Графический интерфейс|	Окна, кнопки, поля ввода|
|Вкладки|	Организация по темам|
|Статусбар|	Отображение состояния|
|Обработка ошибок|	Диалоговые окна с сообщениями|
|Интерактивность|	Реальный ввод/вывод без перезапуска|


### 6. Итоговая структура пакета
До (отдельные скрипты):
```text
lab04/
├── main.py

lab05/
├── main.py

lab06/
├── main.py
├── spiral_generator.py
```

После (единый пакет):
```text
lab07/
├── lab7_package/              # ПАКЕТ
│   ├── __init__.py
│   ├── recursion_module.py    # из ЛР4
│   ├── closure_module.py      # из ЛР5
│   └── generator_module.py    # из ЛР6
├── cli.py                     # CLI на Typer (Rare)
├── gui.py                     # GUI на tkinter (Medium)
└── requirements.txt
```

### 8. Ключевые изменения в коде

8.1. Импорт модулей

Было:

```python
# Внутри каждого скрипта - всё своё
def linearize_recursive(...):
    ...
```
Стало:

```python
# В пакете - импорт из модулей
from lab7_package import recursion_module, closure_module, generator_module

# Использование
recursion_module.linearize_recursive([1, 2, [3, 4]])
```

8.2. Обработка ошибок

Было:

```python
raise ValueError("Ошибка")
```
Стало:

```python
class CallLimitError(Exception):
    pass

raise CallLimitError("Превышено максимальное количество вызовов (3) для функции 'test_func'")
```

8.3. Ввод данных

Было:

```python
# Жёстко заданные данные
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Стало:

```python
# В GUI - пользовательский ввод
self.matrix_size = ttk.Combobox(frame, values=[3, 5, 7, 9, 11])
size = int(self.matrix_size.get())
matrix = create_matrix(size, fill_type)
```