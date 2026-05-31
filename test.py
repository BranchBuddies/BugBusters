from dataclasses import dataclass

@dataclass
class Task:
    title: str
    done: bool = False

    def mark_done(self):
        self.done = True

def add_task(tasks, title):
    task = Task(title=title)
    tasks.append(task)

def list_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task.done else "✗"
        print(f"{i}. {task.title} [{status}]")

def main():
    tasks = []
    add_task(tasks, "Выучить Python")
    add_task(tasks, "Сделать проект")
    tasks[0].mark_done()
    list_tasks(tasks)

if __name__ == "__main__":
    main()
