# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
n = int(input())
s = set()

for _ in range(n):
    s.add(int(input()))

arr = list(s)
arr.sort()

sum_set = set()

for a in range(n):
    for b in range(n):
        sum_set.add(arr[a] + arr[b])

for d in range(len(arr)-1,-1,-1):
    for c in range(len(arr)):
        if (arr[d] - arr[c]) in sum_set:
            print(arr[d])
            exit()

