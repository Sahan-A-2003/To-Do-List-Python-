import json

file_name = "todo_list.json"

def lode_tasks():
  try:
    with open(file_name, "r") as file:
      return json.load(file)
  except:
    return { "tasks": []}

def save_tasks(tasks):
  try:
    with open(file_name, "w") as file:
      json.dump(tasks, file)
  except:
    print("faile to save")

def view_tasks(tasks):
  print()
  tasks_list = tasks["tasks"]
  if len(tasks_list) == 0:
    print("No tasks to display.")
  else:
    print("You To_Do List: ")
    for idx, task in enumerate(tasks_list):
      status = "[Complete]" if task["complete"] else "[Pending]"
      print(f"{idx + 1}. {task['description']} | {status}")

def create_tasks(tasks):
  description = input("Enter the tasks description: ").strip()

  if description:
    tasks["tasks"].append({"description":description, "complete": False})
    save_tasks(tasks)
    print("Tasks added.")
  else:
    print("desription can not be empty..")

def mark_tasks_complete():
  pass

def main():
  tasks = lode_tasks()

  while True:
    print("\nTo Do List Manager")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Complete Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
      view_tasks(tasks)
    elif choice == "2":
      create_tasks(tasks)
    elif choice == "3":
      mark_tasks_complete()
    elif choice == "4":
      print("Goodbye!!")
      break
    else:
      print("Invalide choice. please try againe.")

main()
