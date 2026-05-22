#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI приложение для системы учёта задач (ToDo)
На основе tkinter
Уровень Rare
"""

import tkinter as tk
from tkinter import ttk, messagebox
from database import db


class TodoApp:
    """Главное приложение ToDo."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo - Система учёта задач")
        self.root.geometry("800x600")
        self.root.minsize(700, 500)
        
        # Переменные
        self.current_filter = "all"
        
        # Создание интерфейса
        self.create_widgets()
        
        # Загрузка задач
        self.refresh_tasks()
    
    def create_widgets(self):
        """Создание виджетов."""
        # Верхняя панель
        top_frame = ttk.Frame(self.root, padding="10")
        top_frame.pack(fill=tk.X)
        
        ttk.Label(top_frame, text="Новая задача:", font=('Arial', 10, 'bold')).pack(side=tk.LEFT)
        
        self.title_entry = ttk.Entry(top_frame, width=40)
        self.title_entry.pack(side=tk.LEFT, padx=10)
        
        ttk.Button(top_frame, text="➕ Добавить", command=self.add_task).pack(side=tk.LEFT)
        
        # Панель фильтров
        filter_frame = ttk.Frame(self.root, padding="10")
        filter_frame.pack(fill=tk.X)
        
        ttk.Button(filter_frame, text="📋 Все", command=lambda: self.set_filter("all")).pack(side=tk.LEFT, padx=5)
        ttk.Button(filter_frame, text="🟢 Активные", command=lambda: self.set_filter("active")).pack(side=tk.LEFT, padx=5)
        ttk.Button(filter_frame, text="✅ Выполненные", command=lambda: self.set_filter("completed")).pack(side=tk.LEFT, padx=5)
        
        # Статистика
        self.stats_label = ttk.Label(filter_frame, text="", font=('Arial', 9))
        self.stats_label.pack(side=tk.RIGHT, padx=10)
        
        # Список задач
        list_frame = ttk.Frame(self.root, padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Создание Treeview
        columns = ("ID", "Статус", "Приоритет", "Название", "Описание", "Дата")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=15)
        
        # Настройка колонок
        self.tree.heading("ID", text="ID")
        self.tree.heading("Статус", text="Статус")
        self.tree.heading("Приоритет", text="Приоритет")
        self.tree.heading("Название", text="Название")
        self.tree.heading("Описание", text="Описание")
        self.tree.heading("Дата", text="Дата")
        
        self.tree.column("ID", width=40)
        self.tree.column("Статус", width=100)
        self.tree.column("Приоритет", width=80)
        self.tree.column("Название", width=200)
        self.tree.column("Описание", width=200)
        self.tree.column("Дата", width=150)
        
        # Скроллбар
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Привязка событий
        self.tree.bind('<Double-Button-1>', self.on_task_double_click)
        
        # Нижняя панель
        bottom_frame = ttk.Frame(self.root, padding="10")
        bottom_frame.pack(fill=tk.X)
        
        ttk.Button(bottom_frame, text="✅ Выполнить", command=self.complete_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(bottom_frame, text="✏️ Редактировать", command=self.edit_task).pack(side=tk.LEFT, padx=5)
        ttk.Button(bottom_frame, text="🗑 Удалить", command=self.delete_task).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(bottom_frame, text="🔄 Обновить", command=self.refresh_tasks).pack(side=tk.RIGHT, padx=5)
    
    def set_filter(self, filter_type):
        """Устанавливает фильтр и обновляет список."""
        self.current_filter = filter_type
        self.refresh_tasks()
    
    def refresh_tasks(self):
        """Обновляет список задач."""
        # Очищаем список
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Получаем задачи в зависимости от фильтра
        if self.current_filter == "all":
            tasks = db.get_all_tasks()
        elif self.current_filter == "active":
            tasks = db.get_active_tasks()
        else:
            tasks = db.get_completed_tasks()
        
        # Добавляем задачи в список
        for task in tasks:
            status_text = "✅ Выполнена" if task['status'] == 'completed' else "🟢 Активна"
            priority_text = self.get_priority_text(task['priority'])
            
            self.tree.insert("", tk.END, values=(
                task['id'],
                status_text,
                priority_text,
                task['title'],
                task['description'][:50] if task['description'] else "",
                task['created_at'][:16] if task['created_at'] else ""
            ))
        
        # Обновляем статистику
        stats = db.get_statistics()
        self.stats_label.config(text=f"📊 Всего: {stats['total']} | Активных: {stats['active']} | Выполнено: {stats['completed']}")
    
    def get_priority_text(self, priority):
        """Возвращает текст приоритета."""
        priority_map = {
            'high': '🔴 Высокий',
            'medium': '🟡 Средний',
            'low': '🟢 Низкий'
        }
        return priority_map.get(priority, '🟡 Средний')
    
    def add_task(self):
        """Добавляет новую задачу."""
        title = self.title_entry.get().strip()
        if not title:
            messagebox.showwarning("Предупреждение", "Введите название задачи!")
            return
        
        # Диалог для описания и приоритета
        dialog = tk.Toplevel(self.root)
        dialog.title("Новая задача")
        dialog.geometry("400x300")
        dialog.transient(self.root)
        dialog.grab_set()
        
        ttk.Label(dialog, text="Название:").pack(pady=5)
        title_var = tk.StringVar(value=title)
        title_entry = ttk.Entry(dialog, textvariable=title_var, width=40)
        title_entry.pack(pady=5)
        
        ttk.Label(dialog, text="Описание:").pack(pady=5)
        desc_text = tk.Text(dialog, height=5, width=40)
        desc_text.pack(pady=5)
        
        ttk.Label(dialog, text="Приоритет:").pack(pady=5)
        priority_var = tk.StringVar(value="medium")
        priority_frame = ttk.Frame(dialog)
        priority_frame.pack(pady=5)
        ttk.Radiobutton(priority_frame, text="Высокий", variable=priority_var, value="high").pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(priority_frame, text="Средний", variable=priority_var, value="medium").pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(priority_frame, text="Низкий", variable=priority_var, value="low").pack(side=tk.LEFT, padx=10)
        
        def save():
            db.add_task(title_var.get(), desc_text.get("1.0", tk.END).strip(), priority_var.get())
            dialog.destroy()
            self.title_entry.delete(0, tk.END)
            self.refresh_tasks()
        
        ttk.Button(dialog, text="Сохранить", command=save).pack(pady=20)
    
    def complete_task(self):
        """Отмечает задачу как выполненную."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Предупреждение", "Выберите задачу!")
            return
        
        task_id = self.tree.item(selected[0])['values'][0]
        db.update_task_status(task_id, 'completed')
        self.refresh_tasks()
    
    def edit_task(self):
        """Редактирует выбранную задачу."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Предупреждение", "Выберите задачу!")
            return
        
        task_id = self.tree.item(selected[0])['values'][0]
        task = db.get_task(task_id)
        if not task:
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Редактирование задачи")
        dialog.geometry("400x350")
        dialog.transient(self.root)
        dialog.grab_set()
        
        ttk.Label(dialog, text="Название:").pack(pady=5)
        title_var = tk.StringVar(value=task['title'])
        title_entry = ttk.Entry(dialog, textvariable=title_var, width=40)
        title_entry.pack(pady=5)
        
        ttk.Label(dialog, text="Описание:").pack(pady=5)
        desc_text = tk.Text(dialog, height=5, width=40)
        desc_text.insert("1.0", task['description'] or "")
        desc_text.pack(pady=5)
        
        ttk.Label(dialog, text="Приоритет:").pack(pady=5)
        priority_var = tk.StringVar(value=task['priority'])
        priority_frame = ttk.Frame(dialog)
        priority_frame.pack(pady=5)
        ttk.Radiobutton(priority_frame, text="Высокий", variable=priority_var, value="high").pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(priority_frame, text="Средний", variable=priority_var, value="medium").pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(priority_frame, text="Низкий", variable=priority_var, value="low").pack(side=tk.LEFT, padx=10)
        
        def save():
            db.update_task(task_id, title_var.get(), desc_text.get("1.0", tk.END).strip(), priority_var.get())
            dialog.destroy()
            self.refresh_tasks()
        
        ttk.Button(dialog, text="Сохранить", command=save).pack(pady=20)
    
    def delete_task(self):
        """Удаляет задачу."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Предупреждение", "Выберите задачу!")
            return
        
        if messagebox.askyesno("Подтверждение", "Вы уверены, что хотите удалить задачу?"):
            task_id = self.tree.item(selected[0])['values'][0]
            db.delete_task(task_id)
            self.refresh_tasks()
    
    def on_task_double_click(self, event):
        """Обработчик двойного клика."""
        self.edit_task()


def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()