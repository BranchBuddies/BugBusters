def load_numbers(prompt="Введите числа через пробел: "):
    raw = input(prompt)
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
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    avg = total / count
    return {
        "total": total,
        "min": minimum,
        "max": maximum,
        "count": count,
        "avg": avg,
    }


def print_stats(stats_dict):
    if stats_dict is None:
        print("Нет корректных чисел")
        return
    print(f"Сумма: {stats_dict['total']}")
    print(f"Минимум: {stats_dict['min']}")
    print(f"Максимум: {stats_dict['max']}")
    print(f"Количество: {stats_dict['count']}")
    print(f"Среднее: {stats_dict['avg']}")


def main():
    nums = load_numbers()
    result = stats(nums)
    print_stats(result)


if __name__ == "__main__":
    main()
