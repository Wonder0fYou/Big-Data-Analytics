import sys


def mapper():
    """
    Mapper 2-й фазы

    Вход: <уникальное_число>
    Выход: distinct\t<уникальное_число>

    Присваивает всем уникальным числам единый ключ "distinct"
    объединяя результаты всех reducer'ов фазы 1
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            int(line)
        except ValueError:
            continue

        print(f"distinct\t{line}")


if __name__ == "__main__":
    mapper()