import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

result = []
visited = [[0] * n for _ in range(n)]


def dfs(x, y):
    visited[x][y] = 1
    cnt = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or n <= nx or ny < 0 or n <= ny:
            continue
        if visited[nx][ny] == 0 and graph[nx][ny] == 1:
            cnt += dfs(nx, ny)
    return cnt


c = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            if dfs(i, j) == 3:
                c += 1

print(c)
