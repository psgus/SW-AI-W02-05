# Tree - Sanggeun's Travel (BOJ 9372)

import sys

input = sys.stdin.readline

t = int(input())
answer = []

for _ in range(t):
    n, m = map(int, input().split())

    for _ in range(m):
        input()

    answer.append(str(n - 1))

print("\n".join(answer))
