def validate_task_title(title):
    if not isinstance(title, str) or len(title.strip()) == 0:
        raise ValueError("Invalid title")
    return title


def validate_task_description(description):
    if not isinstance(description, str) or len(description.strip()) == 0:
        raise ValueError("Invalid description")
    return description


def validate_due_date(due_date):
    if not isinstance(due_date, str) or len(due_date.strip()) == 0:
        raise ValueError("Invalid due date")
    return due_date