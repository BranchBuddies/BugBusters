# Второй коммит: Добавлена поддержка пользовательского имени

def greet(name=None):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, World!"

# Запрос имени у пользователя
name_input = input("Enter your name (optional): ").strip()

# Вывод приветствия
print(greet(name_input if name_input else None))
