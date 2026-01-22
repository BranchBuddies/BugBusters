from dataclasses import dataclass

@dataclass
class Task:
    title: str
    priority: int = 1
    done: bool = False

    def mark_done(self):
        self.done = True
        print(f"Задача '{self.title}' выполнена!")

    def __str__(self):
        status = "✓" if self.done else "✗"
        return f"{self.title} (приоритет {self.priority}) [{status}]"

def add_task(tasks, title, priority=1):
    task = Task(title=title, priority=priority)
    tasks.append(task)

def list_tasks(tasks, only_open=False):
    for i, task in enumerate(tasks, start=1):
        if only_open and task.done:
            continue
        print(f"{i}. {task}")

def find_task(tasks, title):
    for task in tasks:
        if task.title.lower() == title.lower():
            return task
    return None

def main():
    tasks = []
    add_task(tasks, "Выучить Python", priority=2)
    add_task(tasks, "Сделать проект", priority=3)
    add_task(tasks, "Отдохнуть", priority=1)

    t = find_task(tasks, "Сделать проект")
    if t:
        t.mark_done()

    print("Все задачи:")
    list_tasks(tasks)
    print("\nТолько открытые задачи:")
    list_tasks(tasks, only_open=True)

if __name__ == "__main__":
    main()
