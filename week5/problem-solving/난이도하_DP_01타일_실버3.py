# DP - 01 Tile (BOJ 1904)

n = int(input())

if n == 1:
    print(1)
else:
    prev2 = 1
    prev1 = 2

    for _ in range(3, n + 1):
        prev2, prev1 = prev1, (prev1 + prev2) % 15746

    print(prev1)
