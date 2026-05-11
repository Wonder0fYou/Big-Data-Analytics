import sys


def reducer():
    """
    Reducer 2-й фазы

    Вход: total_avg\t<локальная_сумма>\t<локальное_количество>
    Выход: <итоговое_среднее>

    Агрегирует все локальные суммы и количества, вычисляет итог
    """
    global_sum = 0
    global_count = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split('\t')
        if len(parts) == 3:
            global_sum += int(parts[1])
            global_count += int(parts[2])

    if global_count > 0:
        print(global_sum / global_count)


if __name__ == "__main__":
    reducer()