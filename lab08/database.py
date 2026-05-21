#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль для работы с базой данных SQLite
Лабораторная работа №8 - Система учета задач (ToDo)
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional


class Database:
    """Класс для работы с базой данных задач."""
    
    def __init__(self, db_name: str = "tasks.db"):
        """
        Инициализация подключения к базе данных.
        
        Args:
            db_name: Имя файла базы данных
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.connect()
        self.create_table()
    
    def connect(self):
        """Устанавливает соединение с базой данных."""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
    
    def close(self):
        """Закрывает соединение с базой данных."""
        if self.conn:
            self.conn.close()
    
    def create_table(self):
        """Создаёт таблицу задач, если она не существует."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                done INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                completed_at TEXT
            )
        ''')
        self.conn.commit()
    
    def add_task(self, text: str) -> int:
        """
        Добавляет новую задачу в базу данных.
        
        Args:
            text: Текст задачи
            
        Returns:
            int: ID добавленной задачи
        """
        self.cursor.execute(
            "INSERT INTO tasks (text, done) VALUES (?, ?)",
            (text, 0)
        )
        self.conn.commit()
        return self.cursor.lastrowid
    
    def get_all_tasks(self) -> List[Dict]:
        """
        Получает все задачи из базы данных.
        
        Returns:
            list: Список словарей с задачами
        """
        self.cursor.execute(
            "SELECT id, text, done, created_at, completed_at FROM tasks ORDER BY id"
        )
        rows = self.cursor.fetchall()
        
        tasks = []
        for row in rows:
            tasks.append({
                "id": row[0],
                "text": row[1],
                "done": bool(row[2]),
                "created_at": row[3],
                "completed_at": row[4]
            })
        return tasks
    
    def update_task_status(self, task_id: int, done: bool):
        """
        Обновляет статус выполнения задачи.
        
        Args:
            task_id: ID задачи
            done: Новый статус (True - выполнена, False - не выполнена)
        """
        completed_at = datetime.now().isoformat() if done else None
        self.cursor.execute(
            "UPDATE tasks SET done = ?, completed_at = ? WHERE id = ?",
            (1 if done else 0, completed_at, task_id)
        )
        self.conn.commit()
    
    def delete_task(self, task_id: int):
        """
        Удаляет задачу из базы данных.
        
        Args:
            task_id: ID задачи
        """
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()
    
    def delete_all_tasks(self):
        """Удаляет все задачи из базы данных."""
        self.cursor.execute("DELETE FROM tasks")
        self.conn.commit()
    
    def get_statistics(self) -> Dict:
        """
        Получает статистику по задачам.
        
        Returns:
            dict: Статистика (всего, выполнено, не выполнено)
        """
        self.cursor.execute("SELECT COUNT(*) FROM tasks")
        total = self.cursor.fetchone()[0]
        
        self.cursor.execute("SELECT COUNT(*) FROM tasks WHERE done = 1")
        completed = self.cursor.fetchone()[0]
        
        return {
            "total": total,
            "completed": completed,
            "pending": total - completed
        }


# Функции для удобного импорта в main.py
def init_db(db_name: str = "tasks.db") -> Database:
    """Инициализирует базу данных и возвращает объект для работы."""
    return Database(db_name)