import json

class ToDoList:
    def __init__(self):
        self.tasks = []  # List to store tasks

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)  # Load tasks from the JSON file
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)  # Save tasks to the JSON file

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def add_task(self, new_task):
        self.tasks.append(new_task)  # Add a new task to the list
        print("Task added successfully.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)  # Remove a task from the list
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()
    todo_list.load_tasks()  # Load tasks when the program starts

    while True:
        print("\n--- To-Do List ---")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            todo_list.display_tasks()
        elif choice == "2":
            new_task = input("Enter the new task: ")
            todo_list.add_task(new_task)
        elif choice == "3":
            todo_list.display_tasks()
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == "4":
            todo_list.save_tasks()  # Save tasks before exiting
            print("Exiting the To-Do List. Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
