import tasks

while True:
    print("\n--- TaskMate ---")
    print("1. Add  2. View  3. Complete  4. Delete  5. Exit")
    choice = input("Choose: ")
    if choice == "1":
        tasks.add_task(input("Title: "), input("Due date: "))
    elif choice == "2":
        tasks.view_tasks()
    elif choice == "3":
        tasks.mark_complete(int(input("Task id: ")))
    elif choice == "4":
        tasks.delete_task(int(input("Task id: ")))
    elif choice == "5":
        break