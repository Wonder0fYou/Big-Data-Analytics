import sys


def reducer():
    """
    Reducer 1-й фазы

    Вход: <число>\t1
    Выход: 1

    На каждое уникальное число выдает ровно одну единицу.
    """
    prev_key = None

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        key = line.split('\t', 1)[0]

        if key != prev_key:
            print("1")
            prev_key = key


if __name__ == "__main__":
    reducer()