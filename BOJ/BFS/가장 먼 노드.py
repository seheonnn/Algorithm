from collections import deque


def BFS(graph, visited, n, start):
    queue = deque()
    queue.append(start)

    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if visited[next] == 0:
                visited[next] = visited[cur] + 1
                queue.append(next)


def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n + 1)]
    visited = [0] * (n + 1)

    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)

    visited[1] = 1
    BFS(graph, visited, n, 1)

    max_dist = max(visited)
    answer = visited.count(max_dist)

    return answer