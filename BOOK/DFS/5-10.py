# DFS - 음료수 얼려 먹기

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    graph[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            dfs(nx, ny)

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result += 1
            dfs(i, j)

print(result)
