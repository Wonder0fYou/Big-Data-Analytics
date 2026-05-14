import sys


def reducer():
    """
    Reducer 2-й фазы

    Вход: count\t1
    Выход: <количество_различных_целых_чисел>

    Суммирует все единицы
    """
    total_unique = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split('\t', 1)
        if len(parts) != 2:
            continue

        try:
            total_unique += int(parts[1])
        except ValueError:
            continue

    print(total_unique)


if __name__ == "__main__":
    reducer()