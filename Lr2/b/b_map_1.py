import sys

NUM_BUCKETS = 100


def mapper():
    """
    Mapper 1-й фазы

    Вход: <число>
    Выход: <bucket_id>\t<число>

    Распределяет числа по корзинам так, чтобы каждый
    reducer получил непересекающееся подмножество чисел
    и мог независимо посчитать частичную сумму и счётчик.
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            number = int(line)
        except ValueError:
            continue

        bucket_id = abs(number) % NUM_BUCKETS
        print(f"{bucket_id}\t{number}")


if __name__ == "__main__":
    mapper()