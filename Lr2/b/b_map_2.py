import sys


def mapper():
    """
    Mapper 2-й фазы

    Вход: <локальная_сумма>\t<локальное_количество>
    Выход: total_avg\t<локальная_сумма>\t<локальное_количество>

    Собирает промежуточные результаты на один Reducer.
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        print(f"total_avg\t{line}")


if __name__ == "__main__":
    mapper()