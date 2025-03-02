# Task Tracker

A simple command-line interface (CLI) tool to manage tasks. Tasks are stored in a JSON file and can be added, updated, deleted, marked with different statuses, listed, searched, sorted, and filtered by date.

## Features

- Add a new task
- Update an existing task
- Delete a task
- Mark a task as `todo`, `in-progress`, or `done`
- List all tasks or filter by status
- Search tasks by keyword
- Sort tasks by creation or update date
- Filter tasks by date range

## Usage

### Ensure the tasks file exists

The script will automatically create a `tasks.json` file if it does not exist.

### Commands

#### Add a new task

```sh
python task_tracker.py add "Task description"
```

#### Update an existing task

```sh
python task_tracker.py update <task_id> "New description"
```

#### Delete a task

```sh
python task_tracker.py delete <task_id>
```

#### Mark a task with a new status

```sh
python task_tracker.py mark <task_id> <status>
```

`<status>` can be `todo`, `in-progress`, or `done`.

#### List all tasks

```sh
python task_tracker.py list
```

#### List tasks by status

```sh
python task_tracker.py list-done
python task_tracker.py list-in-progress
```

#### Search tasks by keyword

```sh
python task_tracker.py search "keyword"
```

#### Sort tasks by date

```sh
python task_tracker.py sort <by>
```

`<by>` can be `createdAt` or `updatedAt`.

#### Filter tasks by date range

```sh
python task_tracker.py filter <start_date> <end_date> <by>
```

`<start_date>` and `<end_date>` should be in `YYYY-MM-DD` format. `<by>` can be `createdAt` or `updatedAt`.

## Example

```sh
python task_tracker.py add "Finish the project"
python task_tracker.py list
python task_tracker.py mark 1 done
python task_tracker.py list-done
python task_tracker.py search "project"
python task_tracker.py sort createdAt
python task_tracker.py filter 2023-01-01 2023-12-31 createdAt
```

## Project from Roadmap.sh Task Tracker
[https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)

## License

This project is licensed under the MIT License.https://roadmap.sh/projects/task-tracker