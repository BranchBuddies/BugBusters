def load_numbers():
    raw = input("Введите числа через пробел: ")
    parts = raw.split()
    numbers = []
    for p in parts:
        try:
            numbers.append(float(p))
        except ValueError:
            print(f"'{p}' пропущено (не число)")
    return numbers


def stats(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return total, count, avg


def main():
    nums = load_numbers()
    result = stats(nums)
    if result is None:
        print("Нет корректных чисел")
    else:
        total, count, avg = result
        print(f"Сумма: {total}")
        print(f"Количество: {count}")
        print(f"Среднее: {avg}")


if __name__ == "__main__":
    main()
