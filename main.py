from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)

def menu():
    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due Date: ")
            print(add_task(title, desc, due))

        elif choice == "2":
            title = input("Task title to complete: ")
            print(mark_task_as_complete(title))

        elif choice == "3":
            print(view_pending_tasks())

        elif choice == "4":
            print(f"Progress: {calculate_progress()}%")

        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()