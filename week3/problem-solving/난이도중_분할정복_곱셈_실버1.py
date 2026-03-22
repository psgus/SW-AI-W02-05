# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629
A, B, C = map(int, input().split())

def func(a, b, c):
    if b == 1:
        return a % c

    small = func(a, b // 2, c)

    if b % 2 == 0:
        return (small * small) % c
    else:
        return (small * small * a) % c

print(func(A, B, C))
