# DFS - Bipartite Graph (BOJ 1707)

import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
answer = []

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    color = [0] * (v + 1)
    possible = True

    for start in range(1, v + 1):
        if color[start] != 0:
            continue

        color[start] = 1
        queue = deque([start])

        while queue and possible:
            node = queue.popleft()

            for next_node in graph[node]:
                if color[next_node] == 0:
                    color[next_node] = -color[node]
                    queue.append(next_node)
                elif color[next_node] == color[node]:
                    possible = False
                    break

        if not possible:
            break

    answer.append("YES" if possible else "NO")

print("\n".join(answer))
