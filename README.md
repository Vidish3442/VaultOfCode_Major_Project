# To-Do List Application
This is a simple graphical user interface (GUI) application developed using Python's Tkinter module. The application allows users to manage tasks by adding, editing, deleting, and marking tasks as completed. Tasks are saved in a CSV file for persistence.


## Features
Add Task: Enter a task's title, description, and category to add it to the task list.\
Delete Task: Select a task from the list and delete it.\
Edit Task: Modify the details of an existing task.\
Mark Task as Done: Mark a selected task as done.\
Save Tasks: Save all tasks in a CSV file (task.csv), so they can be reloaded later.\
Load Tasks: Load tasks from the CSV file on application startup
## Code Details

### Code Explanation

#### Key Components
- **CSV File Handling**: Tasks are stored in `task.csv` using Python's `csv` module. The file is created if it doesn't exist.
- **Tkinter GUI**: The user interface is built using the `Tkinter` module. It includes input fields for task details, buttons for various operations, and a listbox for task display.
- **Task Management**: Tasks are stored in a list and displayed in a listbox. The app allows CRUD (Create, Read, Update, Delete) operations on tasks.

#### Code Structure
- `__init__`: Initializes the app, creates the UI elements, loads tasks, and sets initial conditions.
- `create_widgets`: Defines all the buttons, labels, and input fields for the GUI.
- `add_task`: Adds a new task to the list if valid data is provided.
- `delete_task`: Deletes a selected task from the list.
- `edit_task`: Allows editing of a selected task and temporarily removes it from the list.
- `confirm_edit`: Confirms the edit of the task and re-adds it to the list with updated details.
- `mark_as_done`: Marks a selected task as "Done".
- `save_tasks`: Saves the current task list to `task.csv`.
- `load_tasks`: Loads tasks from `task.csv` if the file exists.


## Installation
### Requirements
Python 3.x installed on your system.\
The following Python libraries are needed:\
- Tkinter (comes pre-installed with Python).\
-  csv and os modules (standard Python modules).

## Steps:
- Clone or download this repository.
- Ensure you have Python 3.x installed on your system.
- Open a terminal/command prompt in the project directory.
- Run the application using the command:

```bash
python todo_app.py
```
## CSV File Structure

The tasks are saved to a file named `task.csv` in the following format:

| Title         | Description   | Category   | Status  |
|---------------|---------------|------------|---------|
| Task Title| Task Details | Task Category   | Pending/Done |

- **Title**: The name or title of the task.
- **Description**: A brief description of the task.
- **Category**: The category or group the task belongs to.
- **Status**: The status of the task, either "Pending" or "Done".
## Application Walkthrough

### 1. Adding a Task
- Enter the **task's title**, **description**, and **category** in the provided input fields.
- Click the **Add Task** button to add the task to the list.
- Tasks are displayed in a listbox below the form.

### 2. Deleting a Task
- Select a task from the listbox.
- Click the **Delete Task** button to remove the selected task.

### 3. Editing a Task
- Select a task from the listbox.
- Click the **Edit Task** button. The task details will populate the input fields.
- Modify the task details and click the **Confirm Edit** button to save changes.

### 4. Marking a Task as Done
- Select a task from the listbox.
- Click the **Mark as Done** button to update the task's status to "Done".

### 5. Saving Tasks
- Click the **Save Tasks** button to save all tasks in a CSV file (`task.csv`).
- Tasks will persist between sessions.

### 6. Loading Tasks
- Tasks are automatically loaded from the `task.csv` file when the application starts.
- If the file doesn't exist, it will be created automatically.

## Future Scope
- Add a filter feature to view tasks by category or status.
- Add the ability to set task due dates and prioritize tasks.
- Improve the UI with more modern styling.
## License

This project is licensed under the MIT License. See the LICENSE file for more details.
[MIT](https://choosealicense.com/licenses/mit/)

