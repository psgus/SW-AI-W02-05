# BFS - Maze Search (BOJ 2178)

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maze = [input().strip() for _ in range(n)]
distance = [[0] * m for _ in range(n)]
queue = deque([(0, 0)])
distance[0][0] = 1

while queue:
    row, col = queue.popleft()

    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        next_row = row + dr
        next_col = col + dc

        if 0 <= next_row < n and 0 <= next_col < m:
            if maze[next_row][next_col] == "1" and distance[next_row][next_col] == 0:
                distance[next_row][next_col] = distance[row][col] + 1
                queue.append((next_row, next_col))

print(distance[n - 1][m - 1])
