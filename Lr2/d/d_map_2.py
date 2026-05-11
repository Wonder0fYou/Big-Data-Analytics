import sys


def mapper():
    """
    Mapper 2-й фазы

    Вход: 1 (от Reducer 1)
    Выход: count\t1

    Отправляет единички на финальный счетчик.
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        print(f"count\t{line}")


if __name__ == "__main__":
    mapper()