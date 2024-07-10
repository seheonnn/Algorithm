# BFS(인접행렬) - 경로 찾기

import sys
from collections import deque

n = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        cur = queue.popleft()
        for i in range(n):
            if graph[cur][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

for i in range(n):
    visited = [0] * n
    bfs(i)
    for j in range(n):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
