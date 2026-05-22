#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль для работы с базой данных SQLite
Система учета задач (ToDo)
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Optional


class TodoDatabase:
    """Класс для работы с базой данных задач."""
    
    def __init__(self, db_name: str = "todo.db"):
        self.db_name = db_name
        self._init_db()
    
    def _init_db(self):
        """Инициализация базы данных и создание таблицы."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'pending',
                    priority TEXT DEFAULT 'medium',
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    completed_at TEXT
                )
            """)
            conn.commit()
    
    def add_task(self, title: str, description: str = "", priority: str = "medium") -> int:
        """Добавляет новую задачу."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tasks (title, description, priority)
                VALUES (?, ?, ?)
            """, (title, description, priority))
            conn.commit()
            return cursor.lastrowid
    
    def get_all_tasks(self) -> List[Dict]:
        """Возвращает все задачи."""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM tasks 
                ORDER BY 
                    CASE priority 
                        WHEN 'high' THEN 1 
                        WHEN 'medium' THEN 2 
                        WHEN 'low' THEN 3 
                    END, 
                    created_at DESC
            """)
            return [dict(row) for row in cursor.fetchall()]
    
    def get_active_tasks(self) -> List[Dict]:
        """Возвращает активные задачи."""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM tasks 
                WHERE status = 'pending' 
                ORDER BY 
                    CASE priority 
                        WHEN 'high' THEN 1 
                        WHEN 'medium' THEN 2 
                        WHEN 'low' THEN 3 
                    END, 
                    created_at DESC
            """)
            return [dict(row) for row in cursor.fetchall()]
    
    def get_completed_tasks(self) -> List[Dict]:
        """Возвращает выполненные задачи."""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM tasks 
                WHERE status = 'completed' 
                ORDER BY completed_at DESC
            """)
            return [dict(row) for row in cursor.fetchall()]
    
    def update_task_status(self, task_id: int, status: str):
        """Обновляет статус задачи."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            completed_at = datetime.now().isoformat() if status == 'completed' else None
            cursor.execute("""
                UPDATE tasks 
                SET status = ?, completed_at = ?
                WHERE id = ?
            """, (status, completed_at, task_id))
            conn.commit()
    
    def update_task(self, task_id: int, title: str, description: str, priority: str):
        """Обновляет задачу."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE tasks 
                SET title = ?, description = ?, priority = ?
                WHERE id = ?
            """, (title, description, priority, task_id))
            conn.commit()
    
    def delete_task(self, task_id: int):
        """Удаляет задачу."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
    
    def get_task(self, task_id: int) -> Optional[Dict]:
        """Возвращает задачу по ID."""
        with sqlite3.connect(self.db_name) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def get_statistics(self) -> Dict:
        """Возвращает статистику по задачам."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM tasks")
            total = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM tasks WHERE status = 'pending'")
            active = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM tasks WHERE status = 'completed'")
            completed = cursor.fetchone()[0]
            
            return {
                'total': total,
                'active': active,
                'completed': completed
            }


# Создаём экземпляр БД для использования в других модулях
db = TodoDatabase()