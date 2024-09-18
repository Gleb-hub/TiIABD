def task(n, requests):
    database = {}

    for name in requests:
        if name not in database:
            database[name] = 0
            print("OK")
        else:
            database[name] += 1
            new_name = f"{name}{database[name]}"
            while new_name in database:
                database[name] += 1
                new_name = f"{name}{database[name]}"
            database[new_name] = 0
            print(new_name)


if __name__ == "__main__":
    n = int(input())
    requests = [input().strip() for _ in range(n)]

    task(n, requests)
