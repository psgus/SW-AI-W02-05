# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
import sys
input = sys.stdin.readline

n = int(input())

def tile(n):
    dp=[0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    if n == 1:
        return 1
    for i in range(3,n+1):
        dp[i]=(dp[i-1]+dp[i-2]) % 15746
    return dp[n]
result = tile(n)
print(result)