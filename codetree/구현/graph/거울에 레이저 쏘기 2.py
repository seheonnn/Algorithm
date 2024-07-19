# 그래프 - 거울에 레이저 쏘기 2

import sys
input = sys.stdin.readline

n = int(input())
graph = [input() for _ in range(n)]

start = int(input())

x, y, d = n - (start - 3 * n), 0, 3
if start <= n:
    x, y, d = 0, start - 1, 0
elif start <= 2 * n:
    x, y, d = start - n - 1, n - 1,1
elif start <= 3 * n:
    x, y, d = n - 1, n - (start - 2 * n), 2


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def move(x, y, nd):
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    nx, ny = x + dx[nd], y + dy[nd]
    return nx, ny, nd
move_num = 0
while in_range(x, y):
    if graph[x][y] == '/':
        x, y, d = move(x, y, d ^ 1)
    else:
        x, y, d = move(x, y, 3 - d)

    move_num += 1
