# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541
import sys
input = sys.stdin.readline

s = input().strip().split('-')

result = sum(map(int, s[0].split('+')))

for i in s[1:]:
    result -= sum(map(int, i.split('+')))

print(result)