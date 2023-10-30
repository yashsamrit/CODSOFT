tasks = []
while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")
    elif choice == "2":
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(f"Task '{task}' removed from the to-do list.")
        else:
            print(f"Task '{task}' not found in the to-do list.")
    elif choice == "3":
        if tasks:
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Your to-do list is empty.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
