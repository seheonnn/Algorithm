# 동시에 익게 되는 조건이 있으므로 DFS 사용 불가.
# BFS
# N, M 헷갈리지 않도록 주의
import sys
from collections import deque

def BFS():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i, j))
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


M, N = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
BFS()
# print(graph)
result = max(map(max, graph)) - 1
for row in graph:
    if 0 in row:
        result = -1
print(result)