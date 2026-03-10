# Backtracking - Traveling Salesman 2 (BOJ 10971)

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
answer = 10 ** 9


def dfs(start, current, depth, total):
    global answer

    if total >= answer:
        return

    if depth == n:
        if cost[current][start] != 0:
            answer = min(answer, total + cost[current][start])
        return

    for next_city in range(n):
        if not visited[next_city] and cost[current][next_city] != 0:
            visited[next_city] = True
            dfs(start, next_city, depth + 1, total + cost[current][next_city])
            visited[next_city] = False


visited[0] = True
dfs(0, 0, 1, 0)
print(answer)
