# Brute Force - Maximum Difference (BOJ 10819)

from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
answer = 0

for order in permutations(numbers):
    total = 0

    for i in range(n - 1):
        total += abs(order[i] - order[i + 1])

    answer = max(answer, total)

print(answer)
