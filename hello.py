def greet(name):
    """Возвращает персонализированное приветствие."""
    return f"Hello, {name}!"

def ask_name():
    """Запрашивает имя пользователя и возвращает его."""
    return input("What's your name? ").strip()

def main():
    """Основная логика программы."""
    print("👋 Welcome to the Greeter Program!")
    
    name = ask_name()
    if not name:
        name = "Anonymous"
        print("Hmm, you didn't tell me your name. I'll call you Anonymous.")
    
    print(greet(name))
    print("Nice to meet you! 😊")

# Запуск программы
if __name__ == "__main__":
    main()
