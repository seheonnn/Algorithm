# DFS - 마을 구분하기
# 0 : 벽, 1 : 사람

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]  # 0 : 벽, 1 : 사람
visited = [[0] * n for _ in range(n)]
result = []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def inRange(x, y):
    return x < 0 or n <= x or y < 0 or n <= y


def canGo(x, y):
    return graph[x][y] == 1 and visited[x][y] == 0


def dfs(x, y):
    global cnt
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if inRange(nx, ny):
            continue
        if canGo(nx, ny):  # 시작점에 대한 visited는 dfs 밖에서 설정하고
            visited[nx][ny] = 1  # nx에 대하여 visited를 수정하는 것이 좋음
            cnt += 1
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if canGo(i, j):
            cnt = 1  # 시작점
            visited[i][j] = 1
            dfs(i, j)
            result.append(cnt)

print(len(result))
result.sort()
for i in result:
    print(i)
