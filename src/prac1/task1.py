from math import pi


def task() -> dict:
    res = {}

    num = input("""
    Введите номер фигуры:
    1. Треугольник
    2. Прямоугольник
    3. Круг
    """)
    shapes = {"1": "Треугольник", "2": "Прямоугольник", "3": "Круг"}

    match num:
        case "1":
            b = float(input("Введите сторону: "))
            h = float(input("Введите высоту: "))
            s = 0.5 * b * h
            res[shapes[num]] = s

        case "2":
            a = float(input("Введите сторону a: "))
            b = float(input("Введите сторону b: "))
            s = a * b
            res[shapes[num]] = s

        case "3":
            r = float(input("Введите радиус: "))
            s = pi * r**2
            res[shapes[num]] = s
        case _:
            return None
    return res


if __name__ == "main":
    res = task()
    if res is None:
        print("Ошибка ввода")
    else:
        print(res)

if __name__ == "builtins":
    import sys
    from io import StringIO

    test_input = "2\n2\n3"
    sys.stdin = StringIO(test_input)

    res = task()
    if res is None:
        print("Ошибка ввода")
    else:
        print(res)
