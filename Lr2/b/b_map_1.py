import sys

NUM_BUCKETS = 100


def mapper():
    """
    Mapper 1-й фазы

    Вход: <число>
    Выход: <bucket_id>\t<число>

    Валидирует данные и распределяет их по корзинам для
    параллельного подсчета локальных сумм.
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