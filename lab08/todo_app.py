#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Система учета задач (ToDo) с интеграцией с БД SQLite
Лабораторная работа №8 - Вариант 1
Уровень сложности: Medium (GUI + База данных)
"""

import tkinter as tk
from tkinter import messagebox, ttk
from database import init_db


class TodoApp:
    """Главное приложение ToDo-листа с базой данных."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Система учета задач (ToDo)")
        self.root.geometry("650x600")
        self.root.resizable(True, True)
        
        # Инициализация базы данных
        self.db = init_db("tasks.db")
        
        # Цветовая схема
        self.bg_color = "#2c3e50"
        self.fg_color = "#ecf0f1"
        self.button_color = "#3498db"
        self.completed_color = "#7f8c8d"
        
        self.root.configure(bg=self.bg_color)
        
        # Создание интерфейса
        self.create_widgets()
        
        # Загрузка задач из базы данных
        self.load_tasks_from_db()
        
        # Привязка клавиши Enter
        self.task_entry.bind("<Return>", lambda event: self.add_task())
        
        # Обновление статистики при закрытии
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def create_widgets(self):
        """Создаёт все элементы интерфейса."""
        
        # Заголовок
        title_label = tk.Label(
            self.root,
            text="📝 Мой ToDo-лист",
            font=("Arial", 20, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
        )
        title_label.pack(pady=10)
        
        # Статистика
        self.stats_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 10),
            bg=self.bg_color,
            fg="#95a5a6",
        )
        self.stats_label.pack()
        
        # Верхняя панель: поле ввода + кнопка "Добавить"
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(pady=10)
        
        self.task_entry = tk.Entry(
            input_frame, width=40, font=("Arial", 12), relief=tk.GROOVE
        )
        self.task_entry.pack(side=tk.LEFT, padx=5)
        
        add_button = tk.Button(
            input_frame,
            text="➕ Добавить",
            command=self.add_task,
            bg=self.button_color,
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.RAISED,
            cursor="hand2",
        )
        add_button.pack(side=tk.LEFT, padx=5)
        
        # Фрейм для списка задач (с прокруткой)
        list_frame = tk.Frame(self.root, bg=self.bg_color)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            font=("Arial", 11),
            height=15,
            selectmode=tk.SINGLE,
            bg="#ecf0f1",
            fg="#2c3e50",
            selectbackground="#3498db",
            selectforeground="white",
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=self.task_listbox.yview)
        
        # Кнопки управления задачами
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=10)
        
        complete_button = tk.Button(
            button_frame,
            text="✅ Отметить выполненной",
            command=self.mark_completed,
            bg="#2ecc71",
            fg="white",
            font=("Arial", 10),
            width=20,
            cursor="hand2",
        )
        complete_button.pack(side=tk.LEFT, padx=5)
        
        delete_button = tk.Button(
            button_frame,
            text="🗑 Удалить задачу",
            command=self.delete_task,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 10),
            width=20,
            cursor="hand2",
        )
        delete_button.pack(side=tk.LEFT, padx=5)
        
        # Нижняя панель с кнопками
        bottom_frame = tk.Frame(self.root, bg=self.bg_color)
        bottom_frame.pack(pady=10)
        
        clear_button = tk.Button(
            bottom_frame,
            text="🗑 Очистить все задачи",
            command=self.clear_all,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10),
            width=20,
            cursor="hand2",
        )
        clear_button.pack(side=tk.LEFT, padx=5)
        
        stats_button = tk.Button(
            bottom_frame,
            text="📊 Статистика",
            command=self.show_statistics,
            bg="#9b59b6",
            fg="white",
            font=("Arial", 10),
            width=20,
            cursor="hand2",
        )
        stats_button.pack(side=tk.LEFT, padx=5)
    
    def load_tasks_from_db(self):
        """Загружает задачи из базы данных."""
        self.tasks = self.db.get_all_tasks()
        self.refresh_listbox()
        self.update_stats_display()
    
    def update_stats_display(self):
        """Обновляет отображение статистики."""
        stats = self.db.get_statistics()
        self.stats_label.config(
            text=f"📊 Всего: {stats['total']} | ✅ Выполнено: {stats['completed']} | ⏳ В работе: {stats['pending']}"
        )
    
    def refresh_listbox(self):
        """Обновляет отображение задач в Listbox."""
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task["done"] else "○"
            display_text = f"{idx:2}. [{status}] {task['text']}"
            self.task_listbox.insert(tk.END, display_text)
            
            # Если задача выполнена — красим серым цветом
            if task["done"]:
                self.task_listbox.itemconfig(tk.END, fg=self.completed_color)
    
    def add_task(self):
        """Добавляет новую задачу в базу данных."""
        task_text = self.task_entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Предупреждение", "Вы не ввели текст задачи!")
            return
        
        # Добавляем в базу данных
        task_id = self.db.add_task(task_text)
        
        # Обновляем локальный список
        self.tasks = self.db.get_all_tasks()
        
        # Очищаем поле ввода
        self.task_entry.delete(0, tk.END)
        
        # Обновляем интерфейс
        self.refresh_listbox()
        self.update_stats_display()
        
        messagebox.showinfo("Успех", f"Задача добавлена! ID: {task_id}")
    
    def get_selected_task_id(self):
        """Возвращает ID выбранной задачи."""
        try:
            selection = self.task_listbox.curselection()[0]
            return self.tasks[selection]["id"]
        except IndexError:
            return None
    
    def mark_completed(self):
        """Отмечает выбранную задачу как выполненную."""
        task_id = self.get_selected_task_id()
        if task_id is None:
            messagebox.showwarning("Предупреждение", "Сначала выберите задачу для отметки!")
            return
        
        # Находим задачу и проверяем статус
        task = next((t for t in self.tasks if t["id"] == task_id), None)
        if task and task["done"]:
            messagebox.showinfo("Информация", "Эта задача уже выполнена!")
            return
        
        # Обновляем статус в базе данных
        self.db.update_task_status(task_id, True)
        
        # Обновляем локальный список
        self.tasks = self.db.get_all_tasks()
        
        # Обновляем интерфейс
        self.refresh_listbox()
        self.update_stats_display()
        
        messagebox.showinfo("Успех", "Задача отмечена как выполненная!")
    
    def delete_task(self):
        """Удаляет выбранную задачу."""
        task_id = self.get_selected_task_id()
        if task_id is None:
            messagebox.showwarning("Предупреждение", "Сначала выберите задачу для удаления!")
            return
        
        if messagebox.askyesno("Подтверждение", "Вы уверены, что хотите удалить эту задачу?"):
            # Удаляем из базы данных
            self.db.delete_task(task_id)
            
            # Обновляем локальный список
            self.tasks = self.db.get_all_tasks()
            
            # Обновляем интерфейс
            self.refresh_listbox()
            self.update_stats_display()
            
            messagebox.showinfo("Успех", "Задача удалена!")
    
    def clear_all(self):
        """Удаляет все задачи после подтверждения."""
        if messagebox.askyesno("Подтверждение", "Вы уверены, что хотите удалить ВСЕ задачи?"):
            # Удаляем все из базы данных
            self.db.delete_all_tasks()
            
            # Обновляем локальный список
            self.tasks = self.db.get_all_tasks()
            
            # Обновляем интерфейс
            self.refresh_listbox()
            self.update_stats_display()
            
            messagebox.showinfo("Успех", "Все задачи удалены!")
    
    def show_statistics(self):
        """Показывает подробную статистику в отдельном окне."""
        stats = self.db.get_statistics()
        
        stats_window = tk.Toplevel(self.root)
        stats_window.title("📊 Статистика задач")
        stats_window.geometry("400x250")
        stats_window.configure(bg=self.bg_color)
        stats_window.resizable(False, False)
        
        # Центрируем окно
        stats_window.transient(self.root)
        stats_window.grab_set()
        
        # Заголовок
        tk.Label(
            stats_window,
            text="Статистика задач",
            font=("Arial", 16, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
        ).pack(pady=15)
        
        # Данные статистики
        stats_frame = tk.Frame(stats_window, bg=self.bg_color)
        stats_frame.pack(pady=20)
        
        tk.Label(
            stats_frame,
            text=f"📋 Всего задач: {stats['total']}",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.fg_color,
        ).pack(anchor=tk.W, pady=5)
        
        tk.Label(
            stats_frame,
            text=f"✅ Выполнено: {stats['completed']}",
            font=("Arial", 12),
            bg=self.bg_color,
            fg="#2ecc71",
        ).pack(anchor=tk.W, pady=5)
        
        tk.Label(
            stats_frame,
            text=f"⏳ В работе: {stats['pending']}",
            font=("Arial", 12),
            bg=self.bg_color,
            fg="#e74c3c",
        ).pack(anchor=tk.W, pady=5)
        
        # Прогресс-бар
        if stats['total'] > 0:
            progress = stats['completed'] / stats['total'] * 100
            tk.Label(
                stats_window,
                text=f"Прогресс: {progress:.1f}%",
                font=("Arial", 10),
                bg=self.bg_color,
                fg=self.fg_color,
            ).pack()
            
            progress_bar = ttk.Progressbar(
                stats_window,
                length=300,
                maximum=100,
                value=progress
            )
            progress_bar.pack(pady=10)
        
        # Кнопка закрытия
        tk.Button(
            stats_window,
            text="Закрыть",
            command=stats_window.destroy,
            bg=self.button_color,
            fg="white",
            font=("Arial", 10),
            cursor="hand2",
        ).pack(pady=15)
    
    def on_closing(self):
        """Обработчик закрытия окна."""
        self.db.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()