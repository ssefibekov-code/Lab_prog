#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse

from database import db

app = FastAPI(title="ToDo - Система учёта задач")

# HTML шаблон (с экранированными фигурными скобками)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ToDo - Система учёта задач</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{ max-width: 1000px; margin: 0 auto; }}
        h1 {{ text-align: center; color: white; margin-bottom: 10px; }}
        .subtitle {{ text-align: center; color: rgba(255,255,255,0.8); margin-bottom: 30px; }}
        
        .stats {{
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: white;
            padding: 20px 40px;
            border-radius: 16px;
            text-align: center;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }}
        .stat-number {{ font-size: 36px; font-weight: bold; color: #667eea; }}
        .stat-label {{ color: #666; margin-top: 5px; }}
        
        .add-form {{
            background: white;
            border-radius: 16px;
            padding: 20px;
            margin-bottom: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }}
        .add-form h3 {{ margin-bottom: 15px; color: #333; }}
        .form-row {{ display: flex; gap: 10px; flex-wrap: wrap; }}
        .form-row input, .form-row select {{ padding: 10px; border: 1px solid #ddd; border-radius: 8px; font-size: 14px; }}
        .form-row input {{ flex: 2; }}
        .form-row select {{ width: 120px; }}
        .form-row button {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
        }}
        
        .filters {{ display: flex; gap: 10px; margin-bottom: 20px; }}
        .filter-btn {{
            background: rgba(255,255,255,0.2);
            color: white;
            border: none;
            padding: 8px 20px;
            border-radius: 20px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
        }}
        .filter-btn.active {{ background: white; color: #667eea; }}
        
        .tasks {{
            background: white;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }}
        .task {{
            display: flex;
            align-items: center;
            padding: 15px 20px;
            border-bottom: 1px solid #eee;
            transition: background 0.2s;
        }}
        .task:hover {{ background: #f8f9fa; }}
        .task.completed .task-title {{ text-decoration: line-through; color: #aaa; }}
        .task-checkbox {{ margin-right: 15px; width: 20px; height: 20px; cursor: pointer; background: none; border: none; font-size: 18px; }}
        .task-info {{ flex: 1; }}
        .task-title {{ font-weight: bold; margin-bottom: 5px; }}
        .task-desc {{ font-size: 12px; color: #666; }}
        .task-meta {{ font-size: 11px; color: #999; margin-top: 5px; }}
        .priority {{
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: bold;
            margin-left: 15px;
        }}
        .priority-high {{ background: #fee; color: #e74c3c; }}
        .priority-medium {{ background: #ffd; color: #f39c12; }}
        .priority-low {{ background: #efe; color: #27ae60; }}
        .task-actions button {{
            background: none;
            border: none;
            cursor: pointer;
            font-size: 18px;
            padding: 5px;
            margin-left: 10px;
        }}
        .task-actions button:hover {{ transform: scale(1.1); }}
        
        .empty {{ text-align: center; padding: 40px; color: #999; }}
        a {{ text-decoration: none; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📝 ToDo - Система учёта задач</h1>
        <div class="subtitle">Управляйте своими задачами эффективно</div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">{stats_total}</div>
                <div class="stat-label">Всего задач</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{stats_active}</div>
                <div class="stat-label">Активных</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">{stats_completed}</div>
                <div class="stat-label">Выполнено</div>
            </div>
        </div>
        
        <div class="add-form">
            <h3>➕ Добавить новую задачу</h3>
            <form action="/add" method="post" class="form-row">
                <input type="text" name="title" placeholder="Название задачи" required>
                <input type="text" name="description" placeholder="Описание (необязательно)">
                <select name="priority">
                    <option value="high">🔴 Высокий</option>
                    <option value="medium" selected>🟡 Средний</option>
                    <option value="low">🟢 Низкий</option>
                </select>
                <button type="submit">Добавить</button>
            </form>
        </div>
        
        <div class="filters">
            <a href="/?filter=all" class="filter-btn {filter_all_active}">📋 Все</a>
            <a href="/?filter=active" class="filter-btn {filter_active_active}">🟢 Активные</a>
            <a href="/?filter=completed" class="filter-btn {filter_completed_active}">✅ Выполненные</a>
        </div>
        
        <div class="tasks">
            {tasks_list}
        </div>
    </div>
</body>
</html>
"""


def render_task(task):
    """Рендерит одну задачу в HTML."""
    completed_class = "completed" if task['status'] == 'completed' else ""
    checkbox_icon = "✅" if task['status'] == 'completed' else "⬜"
    
    priority_class = ""
    priority_text = ""
    if task['priority'] == 'high':
        priority_class = "priority-high"
        priority_text = "🔴 Высокий"
    elif task['priority'] == 'medium':
        priority_class = "priority-medium"
        priority_text = "🟡 Средний"
    else:
        priority_class = "priority-low"
        priority_text = "🟢 Низкий"
    
    created_at = task['created_at'][:16] if task['created_at'] else ""
    desc_html = f'<div class="task-desc">{task["description"][:80]}</div>' if task['description'] else ''
    
    return f'''
    <div class="task {completed_class}">
        <form action="/toggle/{task['id']}" method="post" style="margin:0">
            <button type="submit" class="task-checkbox">{checkbox_icon}</button>
        </form>
        <div class="task-info">
            <div class="task-title">{task['title']}</div>
            {desc_html}
            <div class="task-meta">Создана: {created_at}</div>
        </div>
        <div class="priority {priority_class}">{priority_text}</div>
        <div class="task-actions">
            <a href="/edit/{task['id']}"><button title="Редактировать">✏️</button></a>
            <a href="/delete/{task['id']}" onclick="return confirm('Удалить задачу?')"><button title="Удалить">🗑️</button></a>
        </div>
    </div>
    '''


@app.get("/", response_class=HTMLResponse)
async def index(request: Request, filter: str = "all"):
    """Главная страница."""
    if filter == "active":
        tasks = db.get_active_tasks()
    elif filter == "completed":
        tasks = db.get_completed_tasks()
    else:
        tasks = db.get_all_tasks()
    
    stats = db.get_statistics()
    
    # Рендерим список задач
    tasks_html = ""
    if tasks:
        for task in tasks:
            tasks_html += render_task(task)
    else:
        tasks_html = '<div class="empty">📭 Нет задач. Добавьте первую задачу!</div>'
    
    # Определяем активные фильтры
    filter_all_active = "active" if filter == "all" else ""
    filter_active_active = "active" if filter == "active" else ""
    filter_completed_active = "active" if filter == "completed" else ""
    
    # Формируем HTML
    html = HTML_TEMPLATE.format(
        stats_total=stats['total'],
        stats_active=stats['active'],
        stats_completed=stats['completed'],
        tasks_list=tasks_html,
        filter_all_active=filter_all_active,
        filter_active_active=filter_active_active,
        filter_completed_active=filter_completed_active
    )
    
    return HTMLResponse(content=html)


@app.post("/add")
async def add_task(title: str = Form(...), description: str = Form(""), priority: str = Form("medium")):
    """Добавляет новую задачу."""
    db.add_task(title, description, priority)
    return RedirectResponse(url="/", status_code=303)


@app.post("/toggle/{task_id}")
async def toggle_task(task_id: int):
    """Переключает статус задачи."""
    task = db.get_task(task_id)
    if task:
        new_status = "completed" if task['status'] == "pending" else "pending"
        db.update_task_status(task_id, new_status)
    return RedirectResponse(url="/", status_code=303)


@app.get("/edit/{task_id}", response_class=HTMLResponse)
async def edit_form(request: Request, task_id: int):
    """Страница редактирования задачи."""
    task = db.get_task(task_id)
    if not task:
        return RedirectResponse(url="/")
    
    high_selected = 'selected' if task['priority'] == 'high' else ''
    medium_selected = 'selected' if task['priority'] == 'medium' else ''
    low_selected = 'selected' if task['priority'] == 'low' else ''
    
    edit_html = f'''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Редактирование задачи - ToDo</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .container {{
                max-width: 500px;
                width: 100%;
                background: white;
                border-radius: 16px;
                padding: 30px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            }}
            h1 {{ margin-bottom: 20px; color: #333; }}
            .form-group {{ margin-bottom: 20px; }}
            label {{ display: block; margin-bottom: 5px; font-weight: bold; color: #555; }}
            input, textarea, select {{
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 8px;
                font-size: 14px;
            }}
            textarea {{ resize: vertical; min-height: 80px; }}
            .buttons {{ display: flex; gap: 10px; margin-top: 20px; }}
            button {{
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-size: 14px;
            }}
            .save {{ background: #667eea; color: white; }}
            .cancel {{ background: #ddd; color: #333; }}
            a {{ text-decoration: none; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>✏️ Редактирование задачи</h1>
            <form action="/edit/{task_id}" method="post">
                <div class="form-group">
                    <label>Название:</label>
                    <input type="text" name="title" value="{task['title']}" required>
                </div>
                <div class="form-group">
                    <label>Описание:</label>
                    <textarea name="description">{task['description'] or ''}</textarea>
                </div>
                <div class="form-group">
                    <label>Приоритет:</label>
                    <select name="priority">
                        <option value="high" {high_selected}>🔴 Высокий</option>
                        <option value="medium" {medium_selected}>🟡 Средний</option>
                        <option value="low" {low_selected}>🟢 Низкий</option>
                    </select>
                </div>
                <div class="buttons">
                    <button type="submit" class="save">💾 Сохранить</button>
                    <a href="/"><button type="button" class="cancel">❌ Отмена</button></a>
                </div>
            </form>
        </div>
    </body>
    </html>
    '''
    
    return HTMLResponse(content=edit_html)


@app.post("/edit/{task_id}")
async def edit_task(task_id: int, title: str = Form(...), description: str = Form(""), priority: str = Form("medium")):
    """Сохраняет изменения задачи."""
    db.update_task(task_id, title, description, priority)
    return RedirectResponse(url="/", status_code=303)


@app.get("/delete/{task_id}")
async def delete_task(task_id: int):
    """Удаляет задачу."""
    db.delete_task(task_id)
    return RedirectResponse(url="/", status_code=303)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)