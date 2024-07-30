# DFS - 안전지대

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int , input().split())

dx, dy = [1,0,-1,0], [0,1,0,-1]
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

result = {}

def dfs(x,y, k):
    global cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or n <= nx or ny < 0 or m <= ny:
            continue
        if graph[nx][ny] > k and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx,ny, k)
def fn(k):
    for i in range(n):
        for j in range(m):
            if graph[i][j] <= k:
                graph[i][j] = 0
                visited[i][j] = 1

k = 4
for k in range(1, 101):
    fn(k)
    cnt = 0
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] != 1:
                visited[i][j] = 1
                dfs(i, j, k)
                cnt += 1
    result[k] = cnt

m = max(result.values())
r = [key for key, value in result.items() if value == m ]
print(r[0], m)