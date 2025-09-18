from datetime import datetime

def validate_task_title(title):
     if not title.strip():
         print("You need to enter in atleast one character")
         return False
     else:
         return True
         
         
def validate_task_description(description):
    if not description.strip():
        print("You need to enter in atleast one character")
        return False
    else:
        return True
    
    
def validate_due_date(due_date):
    if len(due_date) != 10:
        print("Error: Due date must be in YYYY-MM-DD format and should be 10 characters")
        return False
    
    if due_date[4] !="-" or due_date[7] != "-": 
        print("Error: You're missing a dash (YYYY-MM-DD)")
        return False
    
    year, month, day = due_date.split("-")

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        print("Error: Needs to be a digit from 0-9")
        return False
    
    try:
        real_time = datetime(int(year), int(month), int(day))
        return True
    except:
        print("Error: That is not a valid date unless you are a time travler!")
        return False
    