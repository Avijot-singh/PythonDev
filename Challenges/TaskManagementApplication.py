
def main_menu():
    print("This is main menu")
    print("1.   Add a Task")
    print("2.   Status Checker")
    print("3.   Mark Tasks")
    print("4.   Quit Application")
    user = int(input("please select the options above: "))
    if(user == 1):
        add_task()
    elif(user == 2):
        status_checker()
    elif(user == 3):
        mark_tasks()





tasks = []

def add_task():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    number = int(input("Enter your number: "))

    con_dict = {
        'name' : name, 
        'email' : email,
        'number' : number,
        'completed' : False
    }

    tasks.append(con_dict)
    print(f"Task successfully added {tasks}")

def status_checker():
    status = input("Please type the name of the user to check their status: ")
    found = False
    for task in tasks:
        if(task['name'] == status):
            print(f"Task status for {status}: {'Completed' if task['completed '] else 'Not Completed'}")
            found = True
            break
        if not found:
            print("User not found please try again")
        

def mark_tasks():
    mark = input("Please type the name of the task to be marked off: ")
    found = False
    for task in tasks:
          if(task['name'] == mark):
            task['completed'] = True
            print(f"Task '{mark}' marked as completed.")
            found = True
            break
    if not found:
        print("User not found. Please try again.")