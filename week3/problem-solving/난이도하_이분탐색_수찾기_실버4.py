# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

arr1.sort()

for arr in arr2:
    left = 0
    right = len(arr1)-1
    found = False

    while left <= right:
        mid = (left+right)//2

        if arr1[mid] == arr:
            found = True
            break
        elif arr1[mid] < arr:
            left = mid + 1
        else:
            right = mid - 1

    if found:
        print(1)
    else:
        print(0)
