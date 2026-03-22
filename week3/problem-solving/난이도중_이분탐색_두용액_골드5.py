# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470
n = int(input())
arr = list(map(int, input().split()))

arr.sort()

left = 0
right = n - 1

best = float('inf')
a = 0
b = 0

while left < right:
    s = arr[left] + arr[right]

    if abs(s) < best:
        best = abs(s)
        a = arr[left]
        b = arr[right]

    if s < 0:
        left += 1
    else:
        right -= 1

print(a, b)