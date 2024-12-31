import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(x, y):
    global cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or n <= nx or ny < 0 or n <= ny:
            continue
        if visited[nx][ny] == 0 and graph[nx][ny] == 1:
            cnt += 1
            visited[nx][ny] = 1
            dfs(nx, ny)

r = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt = 1
            visited[i][j] = 1
            dfs(i, j)
            r.append(cnt)

r.sort()
print(len(r))
for el in r:
    print(el)
