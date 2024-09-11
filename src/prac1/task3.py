def task():
    lst1 = []

    while sum(lst1) != 0 or len(lst1) == 0:
        lst1.append(int(input()))

    lst1 = [x**2 for x in lst1]
    return sum(lst1)


if __name__ == "__main__":
    print(task())


if __name__ == "builtins":
    import sys
    from io import StringIO

    sys.stdin = StringIO("1\n2\n-3\n")
    print(task())
