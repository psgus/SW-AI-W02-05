# Recursion - Tower of Hanoi (BOJ 1914)

n = int(input())
print(2 ** n - 1)


def move(count, start, end, via):
    if count == 0:
        return

    move(count - 1, start, via, end)
    print(start, end)
    move(count - 1, via, end, start)


if n <= 20:
    move(n, 1, 3, 2)
