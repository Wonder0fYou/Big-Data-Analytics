import sys


def reducer():
    """
    Универсальный Reducer для уникальных значений.

    Вход (Фаза 1): <число>\t1
    Вход (Фаза 2): distinct\t<число>
    Выход: <число>

    Выводит ключ только один раз при его смене.
    """
    prev_key = None

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split('\t', 1)

        # Если это фаза 1, берем parts[0]. Если фаза 2 (ключ 'distinct') - берем parts[1]
        target_val = parts[1] if parts[0] == 'distinct' else parts[0]

        if target_val != prev_key:
            print(target_val)
            prev_key = target_val


if __name__ == "__main__":
    reducer()