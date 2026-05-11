import sys


def reducer():
    """
    Reducer для поиска максимума

    Вход: <ключ>\t<число>
    Выход: <максимальное_число>

    Находит самое большое число
    среди всех поступивших к нему значений.
    """
    max_val = None

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        _, value_str = line.split('\t', 1)
        value = int(value_str)

        if max_val is None or value > max_val:
            max_val = value

    if max_val is not None:
        print(max_val)


if __name__ == "__main__":
    reducer()