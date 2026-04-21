tasks = []

def addTask():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added to the list.")

def listTasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def deleteTask():
    listTasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except:
        print("Invalid input.")

if __name__ == "__main__":
    print("WELCOME TO THE TO-DO LIST APP")

    while True:
        print("\nPlease select one of the following options:")
        print("------------------------------------------")
        print("1. Add new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid input... please try again.")