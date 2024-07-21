import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y):
    global cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or n <= nx or ny < 0 or n <= ny:
            continue
        if graph[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            cnt += 1
            dfs(nx, ny)

result = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt = 1
            visited[i][j] = 1
            dfs(i, j)
            if cnt == 3:
                result += 1

print(result)