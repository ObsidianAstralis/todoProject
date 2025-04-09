from flask import Flask
from app.models import init_db
from app.repository import add_task, list_tasks, complete_task, delete_task

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return "<h1>Obsidian's flask</h1>"

if __name__ == "__main__":
    app.run()

init_db()

print("Simple To-Do List")
print("1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")

while True:
    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter task title: ")
        add_task(title)
    elif choice == '2':
        for task in list_tasks():
            status = 'Done' if task.completed else 'Pending'
            print(f"[{task.id}] {task.title} - {status}")
    elif choice == '3':
        task_id = int(input("Enter task ID to complete: "))
        complete_task(task_id)
    elif choice == '4':
        task_id = int(input("Enter task ID to delete: "))
        delete_task(task_id)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Try again.")

