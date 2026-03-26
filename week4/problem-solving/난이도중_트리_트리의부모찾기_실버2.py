# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(graph, start=1):
    queue = deque([start])
    visited = set([start])
    parent = [0]*(n+1)

    while queue:
        a = queue.popleft()

        for node in graph[a]:
            if node not in visited:
                visited.add(node)
                parent[node] = a
                queue.append(node)

    return parent

p = bfs(graph, start=1)

for i in range(2, n+1):
    print(p[i])