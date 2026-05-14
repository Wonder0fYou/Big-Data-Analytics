import sys


def reducer():
    """
    Reducer 1-й фазы

    Вход: <bucket_id>\t<целое_число>
    Выход: <local_sum>\t<local_count>

    Накапливает частичную сумму (local_sum) и счётчик
    (local_count) за один линейный проход.
    """
    local_sum = 0
    local_count = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split('\t', 1)
        if len(parts) != 2:
            continue

        try:
            local_sum += int(parts[1])
            local_count += 1
        except ValueError:
            continue

    if local_count > 0:
        print(f"{local_sum}\t{local_count}")


if __name__ == "__main__":
    reducer()