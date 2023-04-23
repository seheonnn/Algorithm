# BFS
import sys
from collections import deque

def BFS():
    queue = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1:
                    queue.append((i, j, k))
    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M:
                continue
            if graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.append((nx, ny, nz))

M, N, H = map(int, sys.stdin.readline().split())
graph = []
for _ in range(H):
    tmp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    graph.append(tmp)

BFS()
result = -1
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 0:
                print(-1)
                exit()
            result = max(result, graph[i][j][k])
print(result - 1)