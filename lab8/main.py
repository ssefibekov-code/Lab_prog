import tkinter as tk
from tkinter import messagebox, ttk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Система учета задач (ToDo)")
        self.root.geometry("550x500")
        self.root.resizable(False, False)

        # Список для хранения задач (каждая задача: {"text": str, "done": bool})
        self.tasks = []

        # Цветовая схема
        self.bg_color = "#2c3e50"
        self.fg_color = "#ecf0f1"
        self.button_color = "#3498db"
        self.completed_color = "#7f8c8d"

        self.root.configure(bg=self.bg_color)

        # Заголовок
        title_label = tk.Label(
            root,
            text="📝 Мой ToDo-лист",
            font=("Arial", 20, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
        )
        title_label.pack(pady=10)

        # Верхняя панель: поле ввода + кнопка "Добавить"
        input_frame = tk.Frame(root, bg=self.bg_color)
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
        )
        add_button.pack(side=tk.LEFT, padx=5)

        # Фрейм для списка задач (с прокруткой)
        list_frame = tk.Frame(root, bg=self.bg_color)
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
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.task_listbox.yview)

        # Кнопки управления задачами
        button_frame = tk.Frame(root, bg=self.bg_color)
        button_frame.pack(pady=10)

        complete_button = tk.Button(
            button_frame,
            text="✅ Отметить выполненной",
            command=self.mark_completed,
            bg="#2ecc71",
            fg="white",
            font=("Arial", 10),
            width=20,
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
        )
        delete_button.pack(side=tk.LEFT, padx=5)

        # Нижняя панель с кнопкой "Очистить всё"
        clear_button = tk.Button(
            root,
            text="Очистить все задачи",
            command=self.clear_all,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 10),
            width=30,
        )
        clear_button.pack(pady=5)

        # Обновляем отображение списка
        self.refresh_listbox()

        # Привязка клавиши Enter к добавлению задачи
        self.task_entry.bind("<Return>", lambda event: self.add_task())

    def add_task(self):
        """Добавляет новую задачу."""
        task_text = self.task_entry.get().strip()
        if task_text == "":
            messagebox.showwarning("Предупреждение", "Вы не ввели текст задачи!")
            return

        self.tasks.append({"text": task_text, "done": False})
        self.task_entry.delete(0, tk.END)
        self.refresh_listbox()

    def refresh_listbox(self):
        """Обновляет отображение задач в Listbox."""
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, start=1):
            status = "[✓] " if task["done"] else "[ ] "
            display_text = f"{idx}. {status}{task['text']}"
            self.task_listbox.insert(tk.END, display_text)

            # Если задача выполнена — красим серым цветом
            if task["done"]:
                self.task_listbox.itemconfig(tk.END, fg=self.completed_color)

    def mark_completed(self):
        """Отмечает выбранную задачу как выполненную."""
        try:
            selection = self.task_listbox.curselection()[0]
            if not self.tasks[selection]["done"]:
                self.tasks[selection]["done"] = True
                self.refresh_listbox()
            else:
                messagebox.showinfo("Информация", "Эта задача уже выполнена!")
        except IndexError:
            messagebox.showwarning(
                "Предупреждение", "Сначала выберите задачу для отметки!"
            )

    def delete_task(self):
        """Удаляет выбранную задачу."""
        try:
            selection = self.task_listbox.curselection()[0]
            del self.tasks[selection]
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning(
                "Предупреждение", "Сначала выберите задачу для удаления!"
            )

    def clear_all(self):
        """Удаляет все задачи после подтверждения."""
        if messagebox.askyesno("Подтверждение", "Вы уверены, что хотите удалить все задачи?"):
            self.tasks.clear()
            self.refresh_listbox()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()