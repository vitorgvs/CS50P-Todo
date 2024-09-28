def main():
    # Initialize an empty to-do list
    todo_list = []

    while True:
        # Display menu options
        print("To-Do List App")
        print("1. Add task")
        print("2. Remove task")
        print("3. Mark task as completed")
        print("4. Display to-do list")
        print("5. Quit")

        # Get user input
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            remove_task(todo_list)
        elif choice == "3":
            mark_task_as_completed(todo_list)
        elif choice == "4":
            display_todo_list(todo_list)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def add_task(todo_list):
    task = input("Enter a task: ")
    todo_list.append({"task": task, "completed": False})

def remove_task(todo_list):
    task_number = int(input("Enter the task number to remove: "))
    try:
        del todo_list[task_number - 1]
    except IndexError:
        print("Task number out of range.")

def mark_task_as_completed(todo_list):
    task_number = int(input("Enter the task number to mark as completed: "))
    try:
        todo_list[task_number - 1]["completed"] = True
    except IndexError:
        print("Task number out of range.")

def display_todo_list(todo_list):
    for i, task in enumerate(todo_list, start=1):
        status = "Completed" if task["completed"] else "Not completed"
        print(f"{i}. {task['task']} - {status}")

if __name__ == "__main__":
    main()
