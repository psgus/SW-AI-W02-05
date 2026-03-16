# Queue - Snake (BOJ 3190)

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
apples = set()

for _ in range(k):
    row, col = map(int, input().split())
    apples.add((row - 1, col - 1))

l = int(input())
turns = {}

for _ in range(l):
    time, direction = input().split()
    turns[int(time)] = direction

snake = deque([(0, 0)])
occupied = {(0, 0)}
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_index = 0
time = 0

while True:
    time += 1
    head_row, head_col = snake[-1]
    dr, dc = directions[direction_index]
    next_row = head_row + dr
    next_col = head_col + dc

    if not (0 <= next_row < n and 0 <= next_col < n) or (next_row, next_col) in occupied:
        break

    snake.append((next_row, next_col))
    occupied.add((next_row, next_col))

    if (next_row, next_col) in apples:
        apples.remove((next_row, next_col))
    else:
        tail = snake.popleft()
        occupied.remove(tail)

    if time in turns:
        if turns[time] == "D":
            direction_index = (direction_index + 1) % 4
        else:
            direction_index = (direction_index - 1) % 4

print(time)
