# Topological Sort - Work (BOJ 2056)

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
time = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
completion = [0] * (n + 1)

for job in range(1, n + 1):
    data = list(map(int, input().split()))
    time[job] = data[0]
    indegree[job] = data[1]
    completion[job] = time[job]

    for prerequisite in data[2:]:
        graph[prerequisite].append(job)

queue = deque(job for job in range(1, n + 1) if indegree[job] == 0)

while queue:
    job = queue.popleft()

    for next_job in graph[job]:
        completion[next_job] = max(completion[next_job], completion[job] + time[next_job])
        indegree[next_job] -= 1

        if indegree[next_job] == 0:
            queue.append(next_job)

print(max(completion))
