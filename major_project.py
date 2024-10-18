import tkinter as tk
from tkinter import messagebox
import csv
import os

# Define the CSV file name or can be taken as an input from user
csv_file = 'task.csv'

# Define the header row for the CSV file 
header = ['Title', 'Description', 'Category', 'Status']

# Create the CSV file if it doesn't exist
if not os.path.exists(csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

class TodoApp:  #ui app interface class and methods
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []
        self.create_widgets()
        self.load_tasks()
        self.is_editing = False  # Flag to track if we are editing a task or not
        self.confirm_edit_button = None  # Initialize the confirm edit button 

    def create_widgets(self):
        # Label and Entry for Task Title
        tk.Label(self.root, text="Task Title").pack(pady=(10, 0))
        self.title_entry = tk.Entry(self.root, width=50)
        self.title_entry.pack(pady=5)

        # Label and Entry for Task Description
        tk.Label(self.root, text="Task Description").pack(pady=(10, 0))
        self.description_entry = tk.Entry(self.root, width=50)
        self.description_entry.pack(pady=5)

        # Label and Entry for Task Category
        tk.Label(self.root, text="Task Category").pack(pady=(10, 0))
        self.category_entry = tk.Entry(self.root, width=50)
        self.category_entry.pack(pady=5)

        # Button to Add Task
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=10)

        # Listbox to Display Tasks
        self.tasks_listbox = tk.Listbox(self.root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)

        # Button to Delete Task
        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=10)

        # Button to Edit Task
        self.edit_task_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_task_button.pack(pady=10)

        # Button to Mark Task as Done
        self.mark_as_done_button = tk.Button(self.root, text="Mark as Done", command=self.mark_as_done)
        self.mark_as_done_button.pack(pady=10)

        # Button to Save Tasks
        self.save_tasks_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks)
        self.save_tasks_button.pack(pady=10)

    def add_task(self):  #method for adding a task
        if not self.is_editing:  # Allow adding only if not in editing mode for not miss communication
            title = self.title_entry.get()
            description = self.description_entry.get()
            category = self.category_entry.get()
            if title and description and category:
                self.tasks.append(f"{title} - {description} - {category} - Pending")  #adding the data in task 
                self.update_tasks_listbox()
                self.clear_entries()   #clearing entered data methods 
            else:
                messagebox.showwarning("Warning", "You must enter title, description, and category.")
        else:
            messagebox.showwarning("Warning", "Finish editing the current task before adding a new one.")

    def clear_entries(self):  #method to clear the entered data 
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

    def delete_task(self):   #to delete the task 
        selected_task_index = self.tasks_listbox.curselection()    #select the task to be deleted
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def edit_task(self):   #edit the task 
        selected_task_index = self.tasks_listbox.curselection()    #select the task to be edited
        if selected_task_index:
            task = self.tasks[selected_task_index[0]]
            title, description, category, status = task.rsplit(" - ", 3)

            # Populate the entry fields with the selected task details
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, title)

            self.description_entry.delete(0, tk.END)
            self.description_entry.insert(0, description)

            self.category_entry.delete(0, tk.END)
            self.category_entry.insert(0, category)

            # Remove the task from the list temporarily
            del self.tasks[selected_task_index[0]]
            self.update_tasks_listbox()

            self.is_editing = True  # Set editing flag to True
            self.add_task_button.config(state=tk.DISABLED)  # Disable the Add Task button

            # Create the Confirm Edit button if it doesn't exist
            if self.confirm_edit_button is None:
                self.confirm_edit_button = tk.Button(self.root, text="Confirm Edit", command=lambda: self.confirm_edit(selected_task_index[0]))
                self.confirm_edit_button.pack(pady=10)
            else:
                self.confirm_edit_button.config(state=tk.NORMAL)  # Enable the button if it already exists
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def confirm_edit(self, index):   #for confirmation of editing mode and edit done
        title = self.title_entry.get()
        description = self.description_entry.get()
        category = self.category_entry.get()
        
        if title and description and category:
            self.tasks.insert(index, f"{title} - {description} - {category} - Pending")
            self.update_tasks_listbox()
            self.clear_entries()
            self.is_editing = False  # Reset editing flag
            self.add_task_button.config(state=tk.NORMAL)  # Re-enable the Add Task button

            # Optionally hide or disable the confirm edit button
            if self.confirm_edit_button is not None:
                self.confirm_edit_button.config(state=tk.DISABLED)

            messagebox.showinfo("Info", "Task edited successfully.")
        else:
            messagebox.showwarning("Warning", "You must enter title, description, and category.")

    def mark_as_done(self):   #for the marking of completed task 
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task_parts = self.tasks[selected_task_index[0]].rsplit(" - ", 3)
            task_parts[-1] = "Done"
            self.tasks[selected_task_index[0]] = " - ".join(task_parts)
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_tasks_listbox(self):  
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

    def save_tasks(self):   #for saving the new tasks in csv file
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for task in self.tasks:
                title, description, category, status = task.rsplit(" - ", 3)
                writer.writerow([title, description, category, status])

        messagebox.showinfo("Info", "Tasks saved successfully.")

    def load_tasks(self):   #for loading  the old tasks from csv file
        try:
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                self.tasks = [f"{row[0]} - {row[1]} - {row[2]} - {row[3]}" for row in reader if row]
                self.update_tasks_listbox()
        except FileNotFoundError:
            messagebox.showwarning("Warning", "No tasks file found.")
            
root = tk.Tk()   # Create the main window
app = TodoApp(root)  # Initialize the TodoApp with the main window
root.mainloop()  # Start the Tkinter event loop
