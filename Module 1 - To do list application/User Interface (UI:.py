user_input = input("Welcome to the To-Do List App!")
add_task = input("Add a task!")
view_task = input("View tasks")
complete_task = input("Task completed")
delete_task = input("Delete task")
quit_task = input("Quit")


def todo_list():
    user_input = input("Welcome to the To-Do List App")
    add_task = input("Add a task?")
    view_task = input("View tasks")
    complete_task = input("Task completed")
    delete_task = input("Delete task")
    quit_task = input("Quit")
    
    task = []
    for task in add_task:
        if task == add_task:
            print("Nice going!")
        # elif 



todo_list()