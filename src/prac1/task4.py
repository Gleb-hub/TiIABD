from functools import reduce


def task():
    N = int(input())
    return reduce(lambda x, y: x + y, [[i] * i for i in range(N)])[:N]


if __name__ == "__main__":
    print(*task())


if __name__ == "builtins":
    import sys
    from io import StringIO

    sys.stdin = StringIO("10\n")
    print(*task())
