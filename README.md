# TaskTracker

A Python script for a command-line interface (CLI) task tracker application. It allows users to manage tasks by adding, updating, deleting, marking, and listing them. The tasks are stored in a JSON file named `tasks.json`.

The `ensure_file` function checks if the `tasks.json` file exists. If it does not, the function creates the file and initializes it with an empty list. This ensures that the file is always present when the application runs.

The `load_tasks` function reads the tasks from the `tasks.json` file and returns them as a list. This function is used to load the current state of tasks whenever an operation needs to be performed on them.

The `save_tasks` function takes a list of tasks as an argument and writes it to the `tasks.json` file in a formatted JSON structure. This function is used to save the updated state of tasks after any modification.

The `generate_id` function generates a unique ID for a new task by finding the maximum ID in the current list of tasks and adding one to it. If there are no tasks, it defaults to zero and returns one.

The `add_task` function adds a new task to the list. It takes a description as an argument, loads the current tasks, generates a unique ID, and creates a new task dictionary with the provided description, a default status of "todo", and timestamps for creation and update. The new task is appended to the list, and the updated list is saved back to the file.

The `update_task` function updates the description of an existing task. It takes a task ID and a new description as arguments, loads the current tasks, and searches for the task with the given ID. If found, it updates the task's description and timestamp, saves the updated list, and prints a success message. If the task ID is not found, it prints an error message.

The `delete_task` function deletes a task by its ID. It takes a task ID as an argument, loads the current tasks, filters out the task with the given ID, saves the updated list, and prints a success message.

The `mark_task` function changes the status of a task. It takes a task ID and a new status as arguments, loads the current tasks, and searches for the task with the given ID. If found, it updates the task's status and timestamp, saves the updated list, and prints a success message. If the task ID is not found, it prints an error message.

The `list_tasks` function lists all tasks or filters them by status if a status is provided. It loads the current tasks, optionally filters them by the given status, and prints each task's ID, description, status, and creation timestamp.

The `main` function sets up the CLI using the `argparse` module. It defines subcommands for listing tasks (with optional status filters), adding tasks, updating tasks, deleting tasks, and marking tasks with a new status. It parses the command-line arguments and calls the appropriate function based on the provided command. If no command is provided, it prints the help message. The script ensures the tasks file exists before performing any operations by calling `ensure_file` at the beginning of the `main` function.

[https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)
