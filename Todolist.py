def main():
    Tasks=[]

    while True:
        print("\nTo-Do List\n")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How may tasks you want to add: "))
            
            for i in range(n_tasks):
                Task = input("Enter the task: ")
                Tasks.append({"task": Task, "done": False})
                print("Task added!")

        
        elif choice == '2':
            if Tasks:
                print("\nTasks:")
                for i, t in enumerate(Tasks, 1):
                    status = "Done" if t["done"] else "Not Done"
                    print(f"{i}. {t['task']} - {status}")
            else:
                print("No tasks available.")


        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(Tasks):
                Tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        
        elif choice == '4':
            task_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_index < len(Tasks):
                deleted_task = Tasks.pop(task_index)
                print(f"Deleted task: {deleted_task['task']}")
            else:
                    print("Invalid task number.")
        

        elif choice == '5':
            print("Exiting the To-Do List.")
            break
main()
