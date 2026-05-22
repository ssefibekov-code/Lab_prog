#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI интерфейс для лабораторной работы №7
На основе tkinter
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import ast

from lab7_package import (
    linearize_recursive, linearize_iterative,
    a_iterative, get_sequence_a,
    make_calc,
    spiral_from_center, get_spiral_order
)


class Lab7App:
    """Главное приложение с вкладками."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторная работа №7")
        self.root.geometry("800x700")
        self.root.minsize(700, 600)
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.create_recursion_tab()
        self.create_closure_tab()
        self.create_generator_tab()
        
        self.statusbar = ttk.Label(root, text="Готов", relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def create_recursion_tab(self):
        """Вкладка для ЛР4."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Рекурсия (ЛР4)")
        
        # Линеаризация
        frame1 = ttk.LabelFrame(tab, text="Линеаризация списков", padding=10)
        frame1.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(frame1, text="Вложенный список:").pack(anchor=tk.W)
        self.linearize_entry = ttk.Entry(frame1, width=70)
        self.linearize_entry.pack(fill=tk.X, pady=5)
        self.linearize_entry.insert(0, "[1, 2, [3, 4, [5, 6]]]")
        
        btn_frame = ttk.Frame(frame1)
        btn_frame.pack(fill=tk.X, pady=5)
        ttk.Button(btn_frame, text="Рекурсивно", command=self.on_linearize_rec).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Итеративно", command=self.on_linearize_iter).pack(side=tk.LEFT, padx=5)
        
        self.linearize_result = scrolledtext.ScrolledText(frame1, height=5)
        self.linearize_result.pack(fill=tk.X, pady=5)
        
        # Последовательность
        frame2 = ttk.LabelFrame(tab, text="Рекуррентная последовательность", padding=10)
        frame2.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(frame2, text="Количество членов (n):").pack(anchor=tk.W)
        self.seq_entry = ttk.Entry(frame2, width=10)
        self.seq_entry.pack(anchor=tk.W, pady=5)
        self.seq_entry.insert(0, "10")
        ttk.Button(frame2, text="Вычислить", command=self.on_sequence).pack(anchor=tk.W, pady=5)
        
        self.seq_result = scrolledtext.ScrolledText(frame2, height=8)
        self.seq_result.pack(fill=tk.X, pady=5)
    
    def on_linearize_rec(self):
        try:
            data = ast.literal_eval(self.linearize_entry.get())
            result = linearize_recursive(data)
            self.linearize_result.delete(1.0, tk.END)
            self.linearize_result.insert(tk.END, f"Результат (рекурсивно):\n{result}")
            self.statusbar.config(text="Линеаризация выполнена (рекурсивно)")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def on_linearize_iter(self):
        try:
            data = ast.literal_eval(self.linearize_entry.get())
            result = linearize_iterative(data)
            self.linearize_result.delete(1.0, tk.END)
            self.linearize_result.insert(tk.END, f"Результат (итеративно):\n{result}")
            self.statusbar.config(text="Линеаризация выполнена (итеративно)")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def on_sequence(self):
        try:
            n = int(self.seq_entry.get())
            values = get_sequence_a(n)
            self.seq_result.delete(1.0, tk.END)
            self.seq_result.insert(tk.END, f"Первые {n} членов a_k:\n")
            for i, val in enumerate(values, 1):
                self.seq_result.insert(tk.END, f"  a_{i} = {val}\n")
            self.statusbar.config(text=f"Вычислено {n} членов последовательности")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def create_closure_tab(self):
        """Вкладка для ЛР5."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Замыкания (ЛР5)")
        
        frame = ttk.LabelFrame(tab, text="Калькулятор с накоплением", padding=10)
        frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(frame, text="Операция:").pack(anchor=tk.W)
        self.calc_op = ttk.Combobox(frame, values=['+', '-', '*', '/'], width=5)
        self.calc_op.pack(anchor=tk.W, pady=5)
        self.calc_op.set('+')
        
        ttk.Label(frame, text="Начальное значение:").pack(anchor=tk.W)
        self.calc_initial = ttk.Entry(frame, width=10)
        self.calc_initial.pack(anchor=tk.W, pady=5)
        self.calc_initial.insert(0, "0")
        
        ttk.Label(frame, text="Значения (через запятую):").pack(anchor=tk.W)
        self.calc_values = ttk.Entry(frame, width=40)
        self.calc_values.pack(fill=tk.X, pady=5)
        self.calc_values.insert(0, "5, 3, 2, 4")
        
        ttk.Button(frame, text="Вычислить", command=self.on_calc).pack(anchor=tk.W, pady=5)
        
        self.calc_result = scrolledtext.ScrolledText(frame, height=6)
        self.calc_result.pack(fill=tk.X, pady=5)
    
    def on_calc(self):
        try:
            op = self.calc_op.get()
            initial = float(self.calc_initial.get())
            values = [float(x.strip()) for x in self.calc_values.get().split(',')]
            
            calc = make_calc(op, initial)
            
            self.calc_result.delete(1.0, tk.END)
            self.calc_result.insert(tk.END, f"Калькулятор: {op} (начально = {initial})\n\n")
            
            current = initial
            for v in values:
                current = calc(v)
                self.calc_result.insert(tk.END, f"  {v} -> {current}\n")
            
            self.statusbar.config(text="Калькулятор выполнен")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
    
    def create_generator_tab(self):
        """Вкладка для ЛР6."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Генераторы (ЛР6)")
        
        frame = ttk.LabelFrame(tab, text="Спиральный обход матрицы от центра", padding=10)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        param_frame = ttk.Frame(frame)
        param_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(param_frame, text="Размер матрицы:").pack(side=tk.LEFT, padx=5)
        self.spiral_size = ttk.Combobox(param_frame, values=[3, 5, 7, 9, 11], width=5)
        self.spiral_size.pack(side=tk.LEFT, padx=5)
        self.spiral_size.set(5)
        
        ttk.Button(param_frame, text="Обойти", command=self.on_spiral).pack(side=tk.LEFT, padx=20)
        
        ttk.Label(frame, text="Исходная матрица:").pack(anchor=tk.W, pady=(10, 5))
        self.matrix_display = scrolledtext.ScrolledText(frame, height=8)
        self.matrix_display.pack(fill=tk.X, pady=5)
        
        ttk.Label(frame, text="Порядок обхода:").pack(anchor=tk.W, pady=(10, 5))
        self.spiral_result = scrolledtext.ScrolledText(frame, height=15)
        self.spiral_result.pack(fill=tk.BOTH, expand=True, pady=5)
    
    def on_spiral(self):
        try:
            size = int(self.spiral_size.get())
            if size % 2 == 0:
                messagebox.showerror("Ошибка", "Размер матрицы должен быть нечётным!")
                return
            
            matrix = [[i * size + j + 1 for j in range(size)] for i in range(size)]
            
            self.matrix_display.delete(1.0, tk.END)
            for row in matrix:
                self.matrix_display.insert(tk.END, f"{row}\n")
            
            self.spiral_result.delete(1.0, tk.END)
            for r, c, val in spiral_from_center(matrix):
                self.spiral_result.insert(tk.END, f"({r}, {c}) -> {val}\n")
            
            self.statusbar.config(text=f"Спиральный обход матрицы {size}x{size} выполнен")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))


def main():
    root = tk.Tk()
    app = Lab7App(root)
    root.mainloop()


if __name__ == "__main__":
    main()