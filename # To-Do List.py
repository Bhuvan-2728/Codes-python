# To-Do List
import os

FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE): return []
    with open(FILE) as f:
        return [line.strip() for line in f if line.strip()]

def save_tasks(tasks):
    with open(FILE, 'w') as f:
        f.write('\n'.join(tasks))

def show_tasks(tasks):
    if not tasks:
        print("  No tasks yet!"); return
    for i, t in enumerate(tasks, 1):
        print(f"  {i}. {t}")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List ---")
        print("1. View  2. Add  3. Delete  4. Quit")
        choice = input("Choice: ").strip()
        if   choice == '1': show_tasks(tasks)
        elif choice == '2':
            task = input("New task: ").strip()
            if task: tasks.append(task); save_tasks(tasks)
        elif choice == '3':
            show_tasks(tasks)
            idx = int(input("Delete task #: ")) - 1
            if 0 <= idx < len(tasks):
                removed = tasks.pop(idx); save_tasks(tasks)
                print(f"Removed: {removed}")
        elif choice == '4': break

if __name__ == "__main__": main()