# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562
numbers = []

for _ in range(9):
    numbers.append(int(input()))

max_value = numbers[0]
max_index = 0

for i in range(9):
    if numbers[i] > max_value:
        max_value = numbers[i]
        max_index = i

print(max_value)
print(max_index + 1)