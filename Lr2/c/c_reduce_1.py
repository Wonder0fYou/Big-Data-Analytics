import sys


def reducer():
    """
    Reducer фазы 1

    Вход: <число>\t1
    Выход: <уникальное_число>

    Выводит ключ только один раз при его смене
    """
    prev_key = None

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split('\t', 1)
        if len(parts) < 1:
            continue

        key = parts[0]

        if key != prev_key:
            print(key)
            prev_key = key


if __name__ == "__main__":
    reducer()