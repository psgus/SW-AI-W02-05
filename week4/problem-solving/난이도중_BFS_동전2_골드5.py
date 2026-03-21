# DP - Coin 2 (BOJ 2294)

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted({int(input()) for _ in range(n)})
inf = 10 ** 9
dp = [inf] * (k + 1)
dp[0] = 0

for coin in coins:
    for amount in range(coin, k + 1):
        dp[amount] = min(dp[amount], dp[amount - coin] + 1)

print(dp[k] if dp[k] != inf else -1)
