import random
from datetime import datetime, timedelta

# Daily To-Do List App

# List of today's tasks with realistic time estimates and scheduled time slots
tasks = [
    {"name": "Study AI (concepts/theory)", "duration": "2 hours", "scheduled_time": "6:00 AM - 8:00 AM", "done": False, "completed_at": None},
    {"name": "Practice DSA (for job prep)", "duration": "2 hours", "scheduled_time": "8:00 AM - 10:00 AM", "done": False, "completed_at": None},
    {"name": "Learn ML/AI framework (PyTorch)", "duration": "1.5 hours", "scheduled_time": "5:00 PM - 6:30 PM", "done": False, "completed_at": None},
    {"name": "Play Guitar", "duration": "45 minutes", "scheduled_time": "6:30 PM - 7:15 PM", "done": False, "completed_at": None},
    {"name": "Play GTA 5 / Games", "duration": "1 hour", "scheduled_time": "7:15 PM - 8:15 PM", "done": False, "completed_at": None},
    {"name": "Read self-improvement book", "duration": "30 minutes", "scheduled_time": "9:00 PM - 9:30 PM", "done": False, "completed_at": None},
]


def show_tasks():
    print("\n--- Today's To-Do List ---")
    for i, task in enumerate(tasks, start=1):
        if task["done"]:
            status = f"Done at {task['completed_at']}"
        else:
            status = "Pending"
        print(f"{i}. {task['name']}")
        print(f"   Scheduled: {task['scheduled_time']} ({task['duration']})")
        print(f"   Status: {status}")


def mark_done():
    show_tasks()
    choice = int(input("\nEnter task number to mark as done: "))
    if 1 <= choice <= len(tasks):
        # Take the scheduled end time of this task (e.g. "8:00 AM" from "6:00 AM - 8:00 AM")
        end_time_str = tasks[choice - 1]["scheduled_time"].split(" - ")[1]
        end_time = datetime.strptime(end_time_str, "%I:%M %p")

        # Random variation: can finish earlier (-30 min) or later (+20 min) than scheduled end
        variation_minutes = random.randint(-30, 20)
        completed_time = end_time + timedelta(minutes=variation_minutes)

        tasks[choice - 1]["done"] = True
        tasks[choice - 1]["completed_at"] = completed_time.strftime("%I:%M %p")
        print(f"Marked '{tasks[choice - 1]['name']}' as done at {tasks[choice - 1]['completed_at']}!")

        # Compare with scheduled end time and show a message
        if completed_time > end_time:
            print("You completed this task AFTER the scheduled time. Try to manage time better next time!")
        else:
            print("Good job! You completed this task on time or early.")
    else:
        print("Invalid task number.")


# Main program loop
while True:
    print("\n1. Show tasks")
    print("2. Mark task as done")
    print("3. Exit")
    option = input("Choose an option (1-3): ")

    if option == "1":
        show_tasks()
    elif option == "2":
        mark_done()
    elif option == "3":
        print("Goodbye! Keep up the good work.")
        break
    else:
        print("Invalid choice, try again.")