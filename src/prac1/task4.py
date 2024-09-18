from functools import reduce

def task():
    N = int(input())
    return reduce(lambda x, y: x + y, [[i] * i for i in range(N)])[:N]


if __name__ == "__main__":
    print(*task())
