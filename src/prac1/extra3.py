def task(n, file_data, m, queries):
    permissions = {}

    for i in range(n):
        data = file_data[i].split()
        file_name = data[0]
        rights = data[1:]
        permissions[file_name] = rights

    operations = {"write": "w", "read": "r", "execute": "x"}

    for query in queries:
        operation, file_name = query.split()
        if operations[operation] in permissions.get(file_name, set()):
            print("OK")
        else:
            print("Access denied")


if __name__ == "main":
    n = int(input())
    file_data = [input().strip() for _ in range(n)]
    m = int(input())
    queries = [input().strip() for _ in range(m)]

    task(n, file_data, m, queries)

if __name__ == "builtins":
    import sys
    from io import StringIO

    sys.stdin = StringIO(
        "3\n"
        "python.exe x\n"
        "book.txt r w\n"
        "notebook.exe r w x\n"
        "5\n"
        "read python.exe\n"
        "read book.txt\n"
        "write notebook.exe\n"
        "execute notebook.exe\n"
        "write book.txt"
    )

    n = int(input())
    file_data = [input().strip() for _ in range(n)]
    m = int(input())
    queries = [input().strip() for _ in range(m)]

    task(n, file_data, m, queries)
