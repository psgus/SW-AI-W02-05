# DP - Coin (BOJ 9084)

import sys

input = sys.stdin.readline

t = int(input())
answer = []

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]

    answer.append(str(dp[target]))

print("\n".join(answer))
