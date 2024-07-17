# 그래프 - 빙빙 돌며 숫자 사각형 채우기
# 오른 -> 아래 -> 왼 -> 위

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0] * m for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
nd = 0

x, y = 0, 0
for i in range(1, n * m + 1):
    graph[x][y] = i
    nx, ny = x + dx[nd], y + dy[nd]
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
        x, y = nx, ny
    else:
        nd = (nd + 1) % 4
        x, y =  x + dx[nd], y + dy[nd]

for rows in graph:
    for node in rows:
        print(node, end=" ")
    print()