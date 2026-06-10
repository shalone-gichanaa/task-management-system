from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []


def add_task(title, description, due_date):
    title = validate_task_title(title)
    description = validate_task_description(description)
    due_date = validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")  # MUST match exact output


def mark_task_as_complete(title):
    for task in tasks:
        if task["title"] == title:
            task["completed"] = True
            print("Task marked as complete!")  # MUST match exactly
            return

    print("Task not found")


def view_pending_tasks():
    pending = [t for t in tasks if not t["completed"]]
    return pending


def calculate_progress(task_list):
    if len(task_list) == 0:
        return 0.0

    completed = len([t for t in task_list if t["completed"]])
    return (completed / len(task_list)) * 100