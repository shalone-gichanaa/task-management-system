from . import validation

tasks = []


def add_task(title, description, due_date):
    valid_title, msg1 = validation.validate_task_title(title)
    valid_desc, msg2 = validation.validate_task_description(description)
    valid_date, msg3 = validation.validate_due_date(due_date)

    if not (valid_title and valid_desc and valid_date):
        return f"Error: {msg1 or msg2 or msg3}"

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    return "Task added successfully"


def mark_task_as_complete(title):
    for task in tasks:
        if task["title"] == title:
            task["completed"] = True
            return "Task marked as complete"
    return "Task not found"


def view_pending_tasks():
    return [task for task in tasks if not task["completed"]]


def calculate_progress():
    if len(tasks) == 0:
        return 0

    completed = len([t for t in tasks if t["completed"]])
    return (completed / len(tasks)) * 100