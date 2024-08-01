# DFS - 뿌요뿌요

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

result = []
cnt = 0

dx, dy = [1,0,-1,0], [0,1,0,-1]
def dfs(x, y):
    global cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or n <= nx or ny < 0 or n <= ny:
            continue
        if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            cnt += 1
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt = 1
            visited[i][j] = 1
            dfs(i, j)
            result.append(cnt)
m = max(result)
r = [i for i in result if i >= 4] # 4 개 이상이어야 터짐
print(len(r), m)