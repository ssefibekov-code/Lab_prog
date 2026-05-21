#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI интерфейс для лабораторных работ №4-6
Использует библиотеку tkinter для создания графического приложения
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import json

from lab7_package import recursion_module, closure_module, generator_module


class LabApp:
    """Главное приложение с вкладками для каждой лабораторной работы."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторные работы №4-6")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Создаём вкладки
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Вкладки для каждой ЛР
        self.create_recursion_tab()   # ЛР4 - Рекурсия
        self.create_closure_tab()     # ЛР5 - Замыкания
        self.create_generator_tab()   # ЛР6 - Генераторы
        
        # Статусная строка
        self.status = ttk.Label(root, text="Готов к работе", relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(fill=tk.X, padx=5, pady=5)
    
    # ========== ВКЛАДКА РЕКУРСИЯ (ЛР4) ==========
    
    def create_recursion_tab(self):
        """Создаёт вкладку для лабораторной работы №4."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="ЛР4 - Рекурсия")
        
        # Фрейм для линеаризации
        linearize_frame = ttk.LabelFrame(tab, text="Линеаризация списка", padding=10)
        linearize_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(linearize_frame, text="Вложенный список (JSON формат):").pack(anchor=tk.W)
        
        self.list_entry = ttk.Entry(linearize_frame, width=70)
        self.list_entry.pack(fill=tk.X, pady=5)
        self.list_entry.insert(0, "[1, 2, [3, 4, [5, [6, []]]]]")
        
        btn_frame = ttk.Frame(linearize_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(btn_frame, text="Рекурсивно", 
                   command=self.linearize_recursive).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Итеративно", 
                   command=self.linearize_iterative).pack(side=tk.LEFT, padx=5)
        
        self.list_result = scrolledtext.ScrolledText(linearize_frame, height=4, width=80)
        self.list_result.pack(fill=tk.X, pady=5)
        
        # Фрейм для последовательности
        seq_frame = ttk.LabelFrame(tab, text="Рекуррентная последовательность a_k", padding=10)
        seq_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(seq_frame, text="Количество членов (k):").pack(anchor=tk.W)
        
        self.k_entry = ttk.Entry(seq_frame, width=10)
        self.k_entry.pack(anchor=tk.W, pady=5)
        self.k_entry.insert(0, "10")
        
        btn_seq_frame = ttk.Frame(seq_frame)
        btn_seq_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(btn_seq_frame, text="Рекурсивно", 
                   command=self.sequence_recursive).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_seq_frame, text="Итеративно", 
                   command=self.sequence_iterative).pack(side=tk.LEFT, padx=5)
        
        self.seq_result = scrolledtext.ScrolledText(seq_frame, height=8, width=80)
        self.seq_result.pack(fill=tk.X, pady=5)
    
    def linearize_recursive(self):
        """Рекурсивная линеаризация."""
        try:
            data = json.loads(self.list_entry.get().replace("'", '"'))
            result = recursion_module.linearize_recursive(data)
            self.list_result.delete(1.0, tk.END)
            self.list_result.insert(tk.END, str(result))
            self.status.config(text="Рекурсивная линеаризация выполнена")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Неверный формат списка: {e}")
    
    def linearize_iterative(self):
        """Итеративная линеаризация."""
        try:
            data = json.loads(self.list_entry.get().replace("'", '"'))
            result = recursion_module.linearize_iterative(data)
            self.list_result.delete(1.0, tk.END)
            self.list_result.insert(tk.END, str(result))
            self.status.config(text="Итеративная линеаризация выполнена")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Неверный формат списка: {e}")
    
    def sequence_recursive(self):
        """Рекурсивное вычисление последовательности."""
        try:
            k = int(self.k_entry.get())
            self.seq_result.delete(1.0, tk.END)
            for i in range(1, k + 1):
                value = recursion_module.a_recursive(i)
                self.seq_result.insert(tk.END, f"a_{i:2d} = {value:8d}\n")
            self.seq_result.insert(tk.END, f"\nЗакономерность: a_k = 3^(k-1)")
            self.status.config(text="Рекурсивное вычисление последовательности выполнено")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число")
    
    def sequence_iterative(self):
        """Итеративное вычисление последовательности."""
        try:
            k = int(self.k_entry.get())
            self.seq_result.delete(1.0, tk.END)
            for i in range(1, k + 1):
                value = recursion_module.a_iterative(i)
                self.seq_result.insert(tk.END, f"a_{i:2d} = {value:8d}\n")
            self.seq_result.insert(tk.END, f"\nЗакономерность: a_k = 3^(k-1)")
            self.status.config(text="Итеративное вычисление последовательности выполнено")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число")
    
    # ========== ВКЛАДКА ЗАМЫКАНИЯ (ЛР5) ==========
    
    def create_closure_tab(self):
        """Создаёт вкладку для лабораторной работы №5."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="ЛР5 - Замыкания")
        
        # Калькулятор
        calc_frame = ttk.LabelFrame(tab, text="Калькулятор с накоплением", padding=10)
        calc_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(calc_frame, text="Операция (+, -, *, /):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.calc_op = ttk.Combobox(calc_frame, values=["+", "-", "*", "/"], width=5)
        self.calc_op.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        self.calc_op.set("+")
        
        ttk.Label(calc_frame, text="Начальное значение:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.calc_initial = ttk.Entry(calc_frame, width=10)
        self.calc_initial.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        self.calc_initial.insert(0, "0")
        
        ttk.Label(calc_frame, text="Значения (через запятую):").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.calc_values = ttk.Entry(calc_frame, width=40)
        self.calc_values.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        self.calc_values.insert(0, "5, 3, 2")
        
        ttk.Button(calc_frame, text="Вычислить", command=self.calculate).grid(row=3, column=0, columnspan=2, pady=10)
        
        self.calc_result = scrolledtext.ScrolledText(calc_frame, height=6, width=60)
        self.calc_result.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Декоратор call_limiter
        limiter_frame = ttk.LabelFrame(tab, text="Декоратор call_limiter", padding=10)
        limiter_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(limiter_frame, text="Максимум вызовов:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.max_calls = ttk.Entry(limiter_frame, width=10)
        self.max_calls.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        self.max_calls.insert(0, "3")
        
        self.limit_btn = ttk.Button(limiter_frame, text="Тестировать", command=self.test_limiter)
        self.limit_btn.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.limit_result = scrolledtext.ScrolledText(limiter_frame, height=6, width=60)
        self.limit_result.grid(row=2, column=0, columnspan=2, pady=5)
    
    def calculate(self):
        """Вычисление через калькулятор."""
        try:
            op = self.calc_op.get()
            initial = float(self.calc_initial.get())
            values = [float(x.strip()) for x in self.calc_values.get().split(",")]
            
            calc_func = closure_module.make_calc(op, initial)
            
            self.calc_result.delete(1.0, tk.END)
            result = initial
            self.calc_result.insert(tk.END, f"Начальное значение: {initial}\n")
            self.calc_result.insert(tk.END, f"Операция: '{op}'\n\n")
            
            for val in values:
                result = calc_func(val)
                self.calc_result.insert(tk.END, f"  {val} -> {result}\n")
            
            self.status.config(text="Калькулятор выполнен")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def test_limiter(self):
        """Тестирование декоратора call_limiter."""
        try:
            max_calls = int(self.max_calls.get())
            
            from lab7_package.closure_module import call_limiter, CallLimitError
            
            @call_limiter(max_calls=max_calls)
            def test_func(name):
                return f"Вызов {name} выполнен"
            
            self.limit_result.delete(1.0, tk.END)
            self.limit_result.insert(tk.END, f"Тестирование call_limiter (максимум {max_calls} вызовов):\n\n")
            
            for i in range(max_calls + 2):
                try:
                    result = test_func(f"№{i+1}")
                    self.limit_result.insert(tk.END, f"  {result}\n")
                except CallLimitError as e:
                    self.limit_result.insert(tk.END, f"  Ошибка: {e}\n")
            
            self.status.config(text="Тест call_limiter выполнен")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число")
    
    # ========== ВКЛАДКА ГЕНЕРАТОРЫ (ЛР6) ==========
    
    def create_generator_tab(self):
        """Создаёт вкладку для лабораторной работы №6."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="ЛР6 - Генераторы")
        
        frame = ttk.LabelFrame(tab, text="Спиральный обход матрицы", padding=10)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        ttk.Label(frame, text="Размер матрицы (нечётный):").pack(anchor=tk.W)
        self.size_entry = ttk.Entry(frame, width=10)
        self.size_entry.pack(anchor=tk.W, pady=5)
        self.size_entry.insert(0, "5")
        
        ttk.Button(frame, text="Показать матрицу", command=self.show_matrix).pack(anchor=tk.W, pady=5)
        ttk.Button(frame, text="Спиральный обход", command=self.spiral_traverse).pack(anchor=tk.W, pady=5)
        
        self.matrix_display = scrolledtext.ScrolledText(frame, height=8, width=80)
        self.matrix_display.pack(fill=tk.X, pady=5)
        
        self.spiral_display = scrolledtext.ScrolledText(frame, height=15, width=80)
        self.spiral_display.pack(fill=tk.BOTH, expand=True, pady=5)
    
    def show_matrix(self):
        """Показывает матрицу."""
        try:
            size = int(self.size_entry.get())
            if size % 2 == 0:
                messagebox.showerror("Ошибка", "Размер матрицы должен быть нечётным!")
                return
            
            matrix = generator_module.create_matrix(size)
            
            self.matrix_display.delete(1.0, tk.END)
            for row in matrix:
                self.matrix_display.insert(tk.END, f"  {row}\n")
            
            self.status.config(text=f"Матрица {size}x{size} создана")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число")
    
    def spiral_traverse(self):
        """Спиральный обход матрицы."""
        try:
            size = int(self.size_entry.get())
            if size % 2 == 0:
                messagebox.showerror("Ошибка", "Размер матрицы должен быть нечётным!")
                return
            
            matrix = generator_module.create_matrix(size)
            
            self.spiral_display.delete(1.0, tk.END)
            self.spiral_display.insert(tk.END, f"Спиральный обход матрицы {size}x{size} (от центра):\n\n")
            
            count = 0
            for r, c, v in generator_module.spiral_from_center(matrix):
                self.spiral_display.insert(tk.END, f"  ({r}, {c}) -> {v:2d}\n")
                count += 1
            
            self.spiral_display.insert(tk.END, f"\nВсего элементов: {count}")
            self.status.config(text=f"Спиральный обход выполнен, {count} элементов")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число")


# ========== ЗАПУСК ==========

def main():
    root = tk.Tk()
    app = LabApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()