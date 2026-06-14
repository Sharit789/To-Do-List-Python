# Daily To-Do List App

A simple Python console application to manage a daily schedule for a CSE student — balancing study (AI, DSA, ML/AI frameworks), entertainment (guitar, gaming), and self-improvement reading.

## Features

- Pre-loaded daily task list with realistic time durations
- Each task has a scheduled time slot (e.g., `6:00 AM - 8:00 AM`)
- Mark tasks as done and record the actual completion time
- Get feedback if a task was completed after its scheduled time

## Requirements

- Python 3.6 or higher
- No external libraries needed (uses only built-in `random` and `datetime` modules)

## How to Run

```bash
python todo_list.py
```

## Usage

When you run the app, you'll see a menu:

```
1. Show tasks
2. Mark task as done
3. Exit
Choose an option (1-3):
```

- **Option 1** — Displays all tasks with their scheduled time, duration, and status (Done/Pending)
- **Option 2** — Lets you select a task by number and mark it as done
- **Option 3** — Exits the program

## Example Output

```
--- Today's To-Do List ---
1. Study AI (concepts/theory)
   Scheduled: 6:00 AM - 8:00 AM (2 hours)
   Status: Pending
2. Practice DSA (for job prep)
   Scheduled: 8:00 AM - 10:00 AM (2 hours)
   Status: Pending
...

Enter task number to mark as done: 1
Marked 'Study AI (concepts/theory)' as done at 07:45 AM!
Good job! You completed this task on time or early.
```

## Default Daily Schedule

| Task | Duration | Scheduled Time |
|------|----------|-----------------|
| Study AI (concepts/theory) | 2 hours | 6:00 AM - 8:00 AM |
| Practice DSA (for job prep) | 2 hours | 8:00 AM - 10:00 AM |
| Learn ML/AI framework (PyTorch) | 1.5 hours | 5:00 PM - 6:30 PM |
| Play Guitar | 45 minutes | 6:30 PM - 7:15 PM |
| Play GTA 5 / Games | 1 hour | 7:15 PM - 8:15 PM |
| Read self-improvement book | 30 minutes | 9:00 PM - 9:30 PM |

You can edit the `tasks` list inside `todo_list.py` to customize names, durations, and scheduled times.

## Future Improvements

- Save task progress to a file so it persists between runs
- Allow adding/removing tasks dynamically
- Add a daily summary report

## License

Free to use and modify for personal or educational purposes.
