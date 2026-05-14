import sys


def reducer():
    """
    Reducer фазы 2

    Вход: distinct\t<число>
    Выход: <число>

    Извлекает и выводит число из каждой входной строки
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split('\t', 1)
        if len(parts) != 2 or parts[0] != 'distinct':
            continue

        print(parts[1])


if __name__ == "__main__":
    reducer()