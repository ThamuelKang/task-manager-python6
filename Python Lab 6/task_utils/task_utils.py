from datetime import datetime

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
   if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
   else:
       print("Not a valid index")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    for task in tasks: 
        if not (task["completed"]==True):
            print(task["title"])
       

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    num_tasks = len(tasks)
    completed_task = 0
    for task in tasks:
        if(task["completed"] == True):
            completed_task += 1

    progress = round((completed_task/num_tasks) *100,2)
    print(f"You are {progress}% way done. {completed_task} done out of {num_tasks} tasks")
    return progress
    
