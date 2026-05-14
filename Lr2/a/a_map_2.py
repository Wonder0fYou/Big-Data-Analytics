import sys


def mapper():
    """
    Mapper 2-й фазы

    Вход: <локальный_максимум>
    Выход: global_max\t<локальный_максимум>

    Присваивает всем локальным максимумам единый ключ
    "global_max", направляя их на один единственный reducer.
    Это гарантирует, что финальный reducer увидит все
    локальные максимумы и сможет выбрать глобальный.
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            int(line)
        except ValueError:
            continue

        print(f"global_max\t{line}")


if __name__ == "__main__":
    mapper()