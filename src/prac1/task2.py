def task(a: float, b: float, operation: str):
    str_expr = str(a) + operation + str(b)

    try:
        x = eval(str_expr)

    except Exception:
        print("При вводе допущена ошибка. Попробуйте еще раз.")
    return x

if __name__ == '__main__':
    a = float(input())
    b = float(input())
    op = str(input())
    print(task(a, b, op))
