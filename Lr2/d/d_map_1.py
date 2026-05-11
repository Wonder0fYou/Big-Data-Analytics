import sys


def mapper():
    """
    Mapper 1-й фазы

    Вход: <число>
    Выход: <число>\t1

    Группируем по самому числу.
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            number = int(line)
        except ValueError:
            continue

        print(f"{number}\t1")


if __name__ == "__main__":
    mapper()