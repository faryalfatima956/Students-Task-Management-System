tasks = []
def add_task(title, due_date):
    """Add a new task to the task list."""
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "due": due_date,
        "done": False,
    }
    tasks.append(task)
    print(f'Task "{title}" added successfully.')


def view_tasks():
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        status = "Done" if t["done"] else "Pending"
        print(f'{t["id"]}. [{status}] {t["title"]} (Due: {t["due"]})')

# def mark_complete(task_id):
#     pass #Member 2

# def delete_task(task_id):
#     pass #Member 3
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f"Task {task_id} deleted successfully.")
            return

    print(f"Task with ID {task_id} does not exist.")