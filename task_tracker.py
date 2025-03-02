import argparse
import json
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Ensure tasks file exists
def ensure_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            json.dump([], f)

# Load tasks from file
def load_tasks():
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Generate unique ID
def generate_id(tasks):
    return max([task["id"] for task in tasks], default=0) + 1

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task = {
        "id": generate_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": str(datetime.now()),
        "updatedAt": str(datetime.now())
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")

# Update task
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = str(datetime.now())
            save_tasks(tasks)
            print("Task updated successfully.")
            return
    print("Task ID not found.")

# Delete task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully.")

# Mark task as in-progress or done
def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = str(datetime.now())
            save_tasks(tasks)
            print(f"Task marked as {status}.")
            return
    print("Task ID not found.")

# List tasks, optionally filtering by status
def list_tasks(status=None):
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    for task in tasks:
        print(f"[ID: {task['id']}] {task['description']} - {task['status']} (Created: {task['createdAt']})")

# CLI setup
def main():
    ensure_file()
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    subparsers.add_parser("list")
    subparsers.add_parser("list-done")
    subparsers.add_parser("list-todo")
    subparsers.add_parser("list-in-progress")
    
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("description", type=str, help="Task description")
    
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("task_id", type=int, help="Task ID")
    update_parser.add_argument("description", type=str, help="New description")
    
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("task_id", type=int, help="Task ID")
    
    mark_parser = subparsers.add_parser("mark")
    mark_parser.add_argument("task_id", type=int, help="Task ID")
    mark_parser.add_argument("status", type=str, choices=["todo", "in-progress", "done"], help="New status")
    
    args = parser.parse_args()
    
    if args.command == "add":
        add_task(args.description)
    elif args.command == "update":
        update_task(args.task_id, args.description)
    elif args.command == "delete":
        delete_task(args.task_id)
    elif args.command == "mark":
        mark_task(args.task_id, args.status)
    elif args.command == "list":
        list_tasks()
    elif args.command == "list-done":
        list_tasks("done")
    elif args.command == "list-todo":
        list_tasks("todo")
    elif args.command == "list-in-progress":
        list_tasks("in-progress")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
