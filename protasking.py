
import tkinter as tk  # Importing tkinter for GUI
from tkinter import messagebox  # Importing messagebox for displaying messages

class Task:  # Defining a class named Task
    def __init__(self, title, is_completed):  # Constructor method for Task class
        self.title = title  # Task title
        self.is_completed = is_completed  # Task status

    def display(self):  # Method to display task details
        status = "Done" if self.is_completed else "Not Done"  # Determine task status
        return f"Task: {self.title}, Status: {status}"  # Return task details

def create_task_window():  # Function to create a new task window
    window = tk.Toplevel(root)  # Create a new window
    tk.Label(window, text="Enter task title: ").grid(row=0)  # Label for task title
    title_entry = tk.Entry(window)  # Entry field for task title
    title_entry.grid(row=0, column=1)  # Position of entry field
    tk.Label(window, text="Is the task completed? (yes/no): ").grid(row=1)  # Label for task status
    status_entry = tk.Entry(window)  # Entry field for task status
    status_entry.grid(row=1, column=1)  # Position of status field
    tk.Button(window, text="Save task", command=lambda: save_task(Task(title_entry.get(), status_entry.get().lower() == 'yes'))).grid(row=2)  # Button to save task

def save_task(task):  # Function to save a task
    try:
        with open('tasks.txt', 'a') as file:  # Open the file in append mode
            file.write(f"{task.title},{task.is_completed}\n")  # Write task details to file
        messagebox.showinfo("Success", "Task saved successfully.")  # Display success message
    except Exception as e:  # Catch any exceptions
        messagebox.showerror("Error", "An error occurred while saving the task.")  # Display error message

def load_tasks_window():  # Function to load tasks
    window = tk.Toplevel(root)  # Create a new window
    try:
        with open('tasks.txt', 'r') as file:  # Open the file in read mode
            lines = file.readlines()  # Read all lines from file
            for i, line in enumerate(lines):  # Loop through each line
                title, is_completed = line.strip().split(',')  # Split line into title and status
                is_completed = True if is_completed == 'True' else False  # Convert status to boolean
                task = Task(title, is_completed)  # Create a Task object
                tk.Label(window, text=task.display()).grid(row=i)  # Display task details
                if not task.is_completed:  # If task is not completed
                    tk.Button(window, text="Close task", command=lambda: close_task(i)).grid(row=i, column=1)  # Add a button to close task
    except Exception as e:  # Catch any exceptions
        messagebox.showerror("Error", "An error occurred while loading the tasks.")  # Display error message

def close_task(index):  # Function to close a task
    try:
        with open('tasks.txt', 'r') as file:  # Open the file in read mode
            lines = file.readlines()  # Read all lines from file
        lines[index] = lines[index].replace('False', 'True')  # Change task status to True
        with open('tasks.txt', 'w') as file:  # Open the file in write mode
            file.writelines(lines)  # Write all lines back to file
        messagebox.showinfo("Success", "Task closed successfully.")  # Display success message
    except Exception as e:  # Catch any exceptions
        messagebox.showerror("Error", "An error occurred while closing the task.")  # Display error message

root = tk.Tk()  # Create a root window
tk.Button(root, text="Create task", command=create_task_window).grid(row=0)  # Button to create a new task
tk.Button(root, text="View tasks", command=load_tasks_window).grid(row=1)  # Button to view tasks
tk.Button(root, text="Exit", command=root.quit).grid(row=2)  # Button to exit the application

root.mainloop()  # Start the application


