import sys


def mapper():
    """
    Mapper 2-й фазы

    Вход: <уникальное_число>
    Выход: distinct\t<уникальное_число>

    Собирает все уникальные числа в один поток
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        print(f"distinct\t{line}")


if __name__ == "__main__":
    mapper()