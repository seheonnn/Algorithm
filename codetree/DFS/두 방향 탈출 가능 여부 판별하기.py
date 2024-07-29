# DFS - 두 방향 탈출 가능 여부 판별하기
# 0 : 뱀 있음, 1 : 뱀 없음

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)] #
escape = False

dx, dy = [1, 0], [0, 1] # 우측 하단으로만 움직일 수 있음

def inRange(x, y):
    return x < 0 or n <= x  or y < 0 or m <= y

def canGo(x, y):
    return visited[x][y] != 1 and graph[x][y] == 1

def dfs(x, y):
    global escape
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if nx == (n-1) and ny == (m-1):
            escape = True
        if inRange(nx, ny):
            continue
        if canGo(nx, ny):
            visited[nx][ny] = 1
            dfs(nx, ny)

visited[0][0] = 1
dfs(0, 0)
if escape:
    print(1)
else:
    print(0)