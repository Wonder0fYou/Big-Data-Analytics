import sys


def mapper():
    """
    Mapper 1-й фазы

    Вход: <число>
    Выход: <число>\t1

    Использует само число в качестве ключа
    Гарантирует, что все пары с одинаковым ключом попадут
    к одному reducerу
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