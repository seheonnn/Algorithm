# 그래프

import sys

n = int(sys.stdin.readline())

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
x, y = 0, 0

for _ in range(n):
    d, w = sys.stdin.readline().split()

    w = int(w)

    if d == 'E':
        di = 0
    elif d == 'W':
        di = 2
    elif d == 'S':
        di = 3
    elif d == 'N':
        di = 1

    x, y = x + dx[di] * w, y + dy[di] * w

print(x, y)