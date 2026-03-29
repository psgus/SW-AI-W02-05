# DP - Ordinary Knapsack (BOJ 12865)

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k + 1)

for _ in range(n):
    weight, value = map(int, input().split())

    for capacity in range(k, weight - 1, -1):
        dp[capacity] = max(dp[capacity], dp[capacity - weight] + value)

print(dp[k])
