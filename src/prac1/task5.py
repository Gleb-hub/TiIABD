def task():
    A = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
    B = ["a", "b", "c", "c", "c", "b", "a", "c", "a", "a", "b", "c", "b", "a"]

    result = {}

    for a, b in zip(A, B):
        if b in result:
            result[b] += a
        else:
            result[b] = a

    return result


if __name__ == "__main__":
    print(task())

if __name__ == "builtins":
    import sys
    from io import StringIO

    sys.stdin = StringIO()
    print(task())
