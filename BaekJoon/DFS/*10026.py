import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
def DFS(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < N and -1 < ny < N:
            if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                DFS(nx, ny)

# 색약 없는 경우
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            DFS(i, j)
            cnt += 1
print(cnt, end=" ")

# 색약 있는 경우
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
visited = [[0] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            DFS(i, j)
            cnt += 1
print(cnt)

