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

def mark_complete(task_id):
    """Find the task by id and mark it as done."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print(f"Task {task_id} marked as complete.")
            return
    print(f"Task with id {task_id} does not exist.")

# def delete_task(task_id):
#     pass #Member 3