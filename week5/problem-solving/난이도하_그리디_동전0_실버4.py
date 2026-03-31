# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coin = len(coins)
total_coins = 0
coins.sort(reverse=True)
for i in range(coin):
    if m >= coins[i]:
        cnt = m // coins[i]
        total_coins += cnt
        m -= coins[i]*cnt
        if m == 0:
            break
print(total_coins)
