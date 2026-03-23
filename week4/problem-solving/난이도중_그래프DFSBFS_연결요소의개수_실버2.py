# Graph - Number of Connected Components (BOJ 11724)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
count = 0

for start in range(1, n + 1):
    if visited[start]:
        continue

    count += 1
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)

print(count)
