import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# def dfs(node, dist):
    # for cur, w in graph[node]:
        # if visited[cur] == -1:
            # visited[cur] = dist + w
            # dfs(cur, visited[cur])

def bfs(node, dist):
    queue = deque()
    queue.append((node, dist))
    while queue:
        node, dist = queue.popleft()
        for cur, w in graph[node]:
            if visited[cur] == -1:
                visited[cur] = dist + w
                queue.append((cur, visited[cur]))

for _ in range(m):
    s, e = map(int, input().split())
    visited = [-1] * (n + 1)
    visited[s] = 0
    bfs(s, 0)
    print(visited[e])
