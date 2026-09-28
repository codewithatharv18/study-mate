import json
from datetime import datetime

FILE_NAME = "study_data.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task():
    print("\n--- ADD STUDY TASK ---")

    subject = input("Enter subject: ")
    topic = input("Enter topic: ")
    task_date = input("Enter date (DD-MM-YYYY): ")
    priority = input("Enter priority (High/Medium/Low): ")

    task = {
        "subject": subject,
        "topic": topic,
        "date": task_date,
        "priority": priority,
        "completed": False
    }

    tasks.append(task)
    save_tasks()

    print("\nTask added successfully!")


def view_tasks():
    print("\n--- ALL STUDY TASKS ---")

    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"\n{i}. {task['subject']}")
        print(f"   Topic    : {task['topic']}")
        print(f"   Date     : {task['date']}")
        print(f"   Priority : {task['priority']}")
        print(f"   Status   : {status}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("\nEnter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks()
            print(f"Deleted: {removed['topic']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def show_progress():
    print("\n--- STUDY PROGRESS ---")

    if not tasks:
        print("No tasks available.")
        return

    completed = sum(task["completed"] for task in tasks)
    total = len(tasks)

    progress = (completed / total) * 100

    print(f"Completed Tasks : {completed}")
    print(f"Total Tasks     : {total}")
    print(f"Overall Progress: {progress:.1f}%")

    bar_length = 20
    filled = int(progress / 100 * bar_length)

    print("[" + "#" * filled + "-" * (bar_length - filled) + "]")


def search_subject():
    keyword = input("\nEnter subject to search: ").lower()

    found = False

    for i, task in enumerate(tasks, start=1):
        if keyword in task["subject"].lower():
            print(f"\n{i}. {task['subject']}")
            print(f"   Topic: {task['topic']}")
            print(f"   Date: {task['date']}")
            print(f"   Priority: {task['priority']}")
            found = True

    if not found:
        print("No matching subject found.")


def main():
    while True:
        print("\n================================")
        print("          STUDYMATE")
        print("     Study Planner & Tracker")
        print("================================")
        print("1. Add Study Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Show Progress")
        print("5. Search Subject")
        print("6. Delete Task")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            show_progress()

        elif choice == "5":
            search_subject()

        elif choice == "6":
            delete_task()

        elif choice == "7":
            print("\nThank you for using StudyMate!")
            break

        else:
            print("\nInvalid choice. Please try again.")


tasks = load_tasks()
main()