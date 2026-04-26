import time

def loading():
    text = "\nLoading..."

    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.2)
    print()

def add_task(tasks, name_task):
    
    task = {"task": name_task, "done": False}
    tasks.append(task)

    print(f"Task '{name_task}' was successfully added")

    loading()
    return

def see_task(tasks):
    print("\nList of Tasks")

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        name_task = task['task']
        print(f"{i}. [{status}] {name_task}")

def update_task(tasks, index_task, new_name_task):
    index_adjusted = int(index_task) - 1

    if index_adjusted >= 0 and index_adjusted < len(tasks):
        tasks[index_adjusted]["task"] = new_name_task
        print(f"Task {index_task} updated to {new_name_task}")
        loading()
    else: 
        print("Index out of range. Try again.")
    return

tasks = []
while True:
    print("\n"+"="*35)
    print("Menu do Gerenciador de Tarefas:")
    print("1. Add task")
    print("2. See tasks")
    print("3. Update task")
    print("4. Complete task")
    print("5. Remove completed tasks")
    print("6. Exit")
    print("="*35)

    esc = input("[option] >> ")

    if esc == "1":
        print('\n'+'='*35, "\nType a name for your task\n")
        name_task = input("[+] ")
        add_task(tasks, name_task)

    elif esc == "2":
        see_task(tasks)

    elif esc == "3":
        see_task(tasks)
        
        index_task = input("\nType the number of the task you want to update\n[number] ")
        new_name_task = input("-"*35 +"\nType the new name for this task\n[new name] ")
        update_task(tasks, index_task, new_name_task)

    elif esc == "6":
        break

    else: 
        print("Choose a valid option")