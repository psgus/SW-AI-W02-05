from collections import deque


def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)

    return order


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2],
    }

    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print("시작 정점: 0")
    print(f"방문 순서: {result}")
