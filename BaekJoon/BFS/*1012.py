# BFS
import sys
from collections import deque
T = int(sys.stdin.readline())

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * N for _ in range(M)]
    cnt = 0

    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                BFS(a,b)
                cnt += 1
    print(cnt)