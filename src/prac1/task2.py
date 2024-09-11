def task(a: float, b: float, operation: str):
    str_expr = str(a) + operation + str(b)

    try:
        x = eval(str_expr)

    except Exception:
        print("При вводе допущена ошибка. Попробуйте еще раз.")
    return x


if __name__ == "__main__":
    print(task("5", "2", "*"))

if __name__ == "builtins":
    import sys
    from io import StringIO

    sys.stdin = StringIO()
    print(task("5", "2", "*"))
