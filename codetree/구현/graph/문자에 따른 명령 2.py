# 그래프

import sys

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
x, y = 0, 0

s = list(sys.stdin.readline().strip())
nd = 1

for i in s:
    if i == 'F':
        x, y = x + dx[nd], y + dy[nd]
    elif i == 'L':
        nd = (nd+1) % 4
    elif i == 'R':
        nd = (nd-1) % 4
print(x, y)
