import sys


def mapper():
    """
    Mapper 2-й фазы

    Вход: 1
    Выход: count\t1

    Присваивает единый ключ "count" всем единицам
    направляя их на один финальный reducer
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        if line != "1":
            continue

        print(f"count\t1")


if __name__ == "__main__":
    mapper()