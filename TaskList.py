tasklist = []

def add_task(taskName):
    tasklist.append({"task_name": taskName, "done": False})

def mark_done(index):
    if 0 <= index < len(tasklist):
        tasklist[index]["done"] = True
    else:
        print("Invalid index")

def delete_task(index):
    if 0 <= index < len(tasklist):
        tasklist.pop(index)
    else:
        print("Invalid index")

def show_tasks():
    print("\nYour task list\n")
    for i, task in enumerate(tasklist):
        status = "\u2714" if task["done"] else "\u2718"
        print(f"{i}: {task['task_name']} [{status}]")

def user():
    while True:
        print("\n1. Add task")
        print("2. Mark task done")
        print("3. Delete task")
        print("4. Show tasks")
        print("5. Exit")

        operation = input("What do you want to do: ")

        match operation:
            case "1":
                add_task(input("Enter task: "))
            case "2":
                mark_done(int(input("Enter task number: ")))
            case "3":
                delete_task(int(input("Enter task to delete: ")))
            case "4":
                show_tasks()
            case "5":
                break
            case _:
                print("Invalid choice")

user()