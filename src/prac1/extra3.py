def task(n, file_data, m, queries):
    '''alskdjalskdjalskdj'''
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


if __name__ == "__main__":
    n = int(input())
    file_data = [input().strip() for _ in range(n)]
    m = int(input())
    queries = [input().strip() for _ in range(m)]

    task(n, file_data, m, queries)
