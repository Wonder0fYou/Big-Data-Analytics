import sys


def reducer():
    """
    Reducer 1-й фазы

    Вход: <bucket_id>\t<число>
    Выход: <локальная_сумма>\t<локальное_количество>

    Считает сумму и количество элементов внутри своей партиции.
    """
    local_sum = 0
    local_count = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        _, value_str = line.split('\t', 1)
        local_sum += int(value_str)
        local_count += 1

    if local_count > 0:
        print(f"{local_sum}\t{local_count}")


if __name__ == "__main__":
    reducer()