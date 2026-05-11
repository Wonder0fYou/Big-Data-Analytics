import sys


def reducer():
    """
    Reducer 2-й фазы

    Вход: count\t1
    Выход: <итоговое_количество>

    Просто суммирует все поступившие единицы.
    """
    total_unique = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        _, val = line.split('\t', 1)
        total_unique += int(val)

    print(total_unique)


if __name__ == "__main__":
    reducer()