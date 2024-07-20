# 그래프 - 빙빙 돌며 사각형 채우기
# 오 -> 아래 -> 왼 -> 위
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
nd = 0

for i in range(0, n * m):
    graph[x][y] = (i % 26) + 65  # 대문자 A : 65

    nx, ny = x + dx[nd], y + dy[nd]
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
        x, y = nx, ny
    else:
        nd = (nd + 1) % 4
        x, y = x + dx[nd], y + dy[nd]

for rows in graph:
    for c in rows:
        print(chr(c), end=" ")
    print()