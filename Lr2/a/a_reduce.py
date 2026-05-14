import sys


def reducer():
    """
    Reducer для поиска максимума

    Вход: <ключ>\t<число>
    Выход: <максимальное_число>

    Линейный проход по всем значениям с поддержанием текущего
    максимума. Завершается за O(n) шагов, где n — число входных пар.
    """
    max_val = None

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split('\t', 1)
        if len(parts) != 2:
            continue

        try:
            value = int(parts[1])
        except ValueError:
            continue

        if max_val is None or value > max_val:
            max_val = value

    if max_val is not None:
        print(max_val)


if __name__ == "__main__":
    reducer()