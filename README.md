# To Do List Manager 📝

A simple command-line To Do List Manager built with Python.
This project helps you manage daily tasks using a JSON file for permanent storage.

## Features

* View all tasks
* Add new tasks
* Mark tasks as complete
* Mark tasks as incomplete
* Remove tasks
* Saves tasks automatically using JSON
* Simple and beginner-friendly project

## Technologies Used

* Python
* JSON File Storage

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Run the project:

```bash
python todo_list.py
```

## Menu Options

```text
1. View Tasks
2. Add Tasks
3. Complete Tasks
4. Incomplete Tasks
5. Remove Tasks
6. Exit
```

## Example Output

```text
To Do List Manager

1. View Tasks
2. Add Tasks
3. Complete Tasks
4. Incomplete Tasks
5. Remove Tasks
6. Exit

Enter your choice: 2
Enter the tasks description: Learn Python
Tasks added.
```

## How It Works

* Tasks are stored inside `todo_list.json`
* Each task has:

  * Description
  * Status (Complete / Pending)
* Data is saved automatically after every change

## Project Structure

```text
todo_list.py
todo_list.json
README.md
```

## Future Improvements

* Add due dates
* Add task priority levels
* Search tasks
* Sort tasks
* GUI version with Tkinter
* Better error handling

## Author

Made with Python for practice and learning.

## License

Free to use and modify.
