# Import functions from task_manager.task_utils package
from task_utils.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress
from task_utils.validation import validate_task_title, validate_task_description, validate_due_date


# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            while True:
                title = input("Enter task title: ")
                if validate_task_title(title):
                    break

            while True:
                description = input("Enter a description: ")
                if validate_task_description(description):
                    break

            while True:
                due_date =input("Enter due date (YYYY-MM-DD format only): ")
                if validate_due_date(due_date):
                    add_task(title, description, due_date)
                    break

        elif choice == "2":
            view_pending_tasks()
            index = int(input("Enter the task number you would like to complete ")) -1
            mark_task_as_complete(index)
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            calculate_progress()
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
