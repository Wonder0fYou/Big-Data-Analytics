import sys


def mapper():
    """
    Mapper 2-й фазы

    Вход: <локальный_максимум>
    Выход: global_max\t<локальный_максимум>

    Направляет все локальные максимумы из первой фазы
    на один единственный Reducer для поиска глобального ответа
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        print(f"global_max\t{line}")


if __name__ == "__main__":
    mapper()