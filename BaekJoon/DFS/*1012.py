# DFS
# 재귀의 한도를 풀어줌. 어떤 문제든 재귀를 사용하는 경우 해주는 것이 좋다
import sys
sys.setrecursionlimit(10000)
T = int(sys.stdin.readline())

def DFS(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            DFS(nx, ny)

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * N for _ in range(M)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1

    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                DFS(a, b)
                cnt += 1
    print(cnt)