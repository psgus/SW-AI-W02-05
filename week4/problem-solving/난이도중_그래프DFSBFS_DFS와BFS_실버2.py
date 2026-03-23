# Graph - DFS and BFS (BOJ 1260)

import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for edges in graph:
    edges.sort()


def dfs(start):
    visited = [False] * (n + 1)
    order = []
    stack = [start]

    while stack:
        node = stack.pop()

        if visited[node]:
            continue

        visited[node] = True
        order.append(node)

        for next_node in reversed(graph[node]):
            if not visited[next_node]:
                stack.append(next_node)

    return order


def bfs(start):
    visited = [False] * (n + 1)
    order = []
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        order.append(node)

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    return order


print(*dfs(v))
print(*bfs(v))
