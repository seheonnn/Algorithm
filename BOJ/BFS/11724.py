# BFS(인접리스트) - 트리의 부모 찾기

import sys
from collections import deque

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1
print(cnt)