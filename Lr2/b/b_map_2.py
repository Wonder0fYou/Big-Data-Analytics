import sys


def mapper():
    """
    Mapper 2-й фазы

    Вход: <локальная_сумма>\t<локальное_количество>
    Выход: total_avg\t<local_sum>\t<local_count>

    Присваивает всем частичным результатам единый ключ
    "total_avg", направляя их на один финальный reducer.
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split('\t')
        if len(parts) != 2:
            continue

        try:
            int(parts[0])
            int(parts[1])
        except ValueError:
            continue

        print(f"total_avg\t{line}")


if __name__ == "__main__":
    mapper()