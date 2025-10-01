# To-Do List Desktop Application
# CPSC 8740 - Assignment 1

import tkinter as tk
from tkinter import ttk, messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("500x400")

        # Data storage
        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Title
        title_label = ttk.Label(main_frame, text="To-Do List", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        # Task entry
        ttk.Label(main_frame, text="New Task:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.task_entry = ttk.Entry(main_frame, width=40)
        self.task_entry.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        self.task_entry.bind('<Return>', lambda e: self.add_task())

        add_button = ttk.Button(main_frame, text="Add Task", command=self.add_task)
        add_button.grid(row=1, column=2, padx=5, pady=5)

        # Task list frame
        list_frame = ttk.Frame(main_frame)
        list_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)

        # Scrollable task list
        self.task_listbox = tk.Listbox(list_frame, height=15, selectmode=tk.SINGLE)
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.task_listbox.configure(yscrollcommand=scrollbar.set)

        self.task_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=3, pady=10)

        ttk.Button(button_frame, text="Mark Complete", command=self.mark_complete).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Delete Task", command=self.delete_task).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Edit Task", command=self.edit_task).grid(row=0, column=2, padx=5)
        ttk.Button(button_frame, text="Clear All", command=self.clear_all).grid(row=0, column=3, padx=5)

        # Status bar
        self.status_label = ttk.Label(main_frame, text="Ready")
        self.status_label.grid(row=4, column=0, columnspan=3, sticky=tk.W, pady=(10, 0))

        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        list_frame.grid_rowconfigure(0, weight=1)
        list_frame.grid_columnconfigure(0, weight=1)

        self.update_status()

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            task = {'text': task_text, 'completed': False}
            self.tasks.append(task)
            self.refresh_task_list()
            self.task_entry.delete(0, tk.END)
            self.update_status()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def mark_complete(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            if index < len(self.tasks):
                self.tasks[index]['completed'] = not self.tasks[index]['completed']
                self.refresh_task_list()
                self.update_status()
        else:
            messagebox.showinfo("Info", "Please select a task to mark complete!")

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            if index < len(self.tasks):
                task_text = self.tasks[index]['text']
                if messagebox.askyesno("Confirm Delete", f"Delete task: '{task_text}'?"):
                    del self.tasks[index]
                    self.refresh_task_list()
                    self.update_status()
        else:
            messagebox.showinfo("Info", "Please select a task to delete!")

    def edit_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            if index < len(self.tasks):
                current_text = self.tasks[index]['text']

                # Create edit dialog
                edit_window = tk.Toplevel(self.root)
                edit_window.title("Edit Task")
                edit_window.geometry("400x150")
                edit_window.transient(self.root)
                edit_window.grab_set()

                ttk.Label(edit_window, text="Edit Task:").pack(pady=10)
                edit_entry = ttk.Entry(edit_window, width=50)
                edit_entry.pack(pady=5)
                edit_entry.insert(0, current_text)
                edit_entry.select_range(0, tk.END)
                edit_entry.focus()

                def save_edit():
                    new_text = edit_entry.get().strip()
                    if new_text:
                        self.tasks[index]['text'] = new_text
                        self.refresh_task_list()
                        edit_window.destroy()
                    else:
                        messagebox.showwarning("Warning", "Task cannot be empty!")

                button_frame = ttk.Frame(edit_window)
                button_frame.pack(pady=10)
                ttk.Button(button_frame, text="Save", command=save_edit).pack(side=tk.LEFT, padx=5)
                ttk.Button(button_frame, text="Cancel", command=edit_window.destroy).pack(side=tk.LEFT, padx=5)

                edit_entry.bind('<Return>', lambda e: save_edit())
        else:
            messagebox.showinfo("Info", "Please select a task to edit!")

    def clear_all(self):
        if self.tasks and messagebox.askyesno("Confirm Clear", "Delete all tasks?"):
            self.tasks.clear()
            self.refresh_task_list()
            self.update_status()

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = "✓" if task['completed'] else "○"
            text = f"{status} {task['text']}"
            self.task_listbox.insert(tk.END, text)

            # Change color for completed tasks
            if task['completed']:
                self.task_listbox.itemconfig(i, {'fg': 'gray'})

    def update_status(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task['completed'])
        pending_tasks = total_tasks - completed_tasks

        self.status_label.config(text=f"Total: {total_tasks} | Completed: {completed_tasks} | Pending: {pending_tasks}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()