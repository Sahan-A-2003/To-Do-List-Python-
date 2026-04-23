import json

file_name = "todo_list.json"

def lode_tasks():
  try:
    with open(file_name, "r") as file:
      return json.load(file)
  except:
    return { "tasks": []}

def save_tasks():
  pass

def view_tasks():
  pass

def create_tasks():
  pass

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
      view_tasks()
    elif choice == "2":
      create_tasks()
    elif choice == "3":
      mark_tasks_complete()
    elif choice == "4":
      print("Goodbye!!")
      break
    else:
      print("Invalide choice. please try againe.")

main()
