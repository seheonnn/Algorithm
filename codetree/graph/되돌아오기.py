# 그래프

import sys
input = sys.stdin.readline
n = int(input())

x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

nd = 0
time = 0

for i in range(n):
    d, w = input().split()
    if d == 'E':
        nd = 1
    elif d == 'W':
        nd = 3
    elif d == 'N':
        nd = 0
    elif d == 'S':
        nd = 2

    w = int(w)
    for j in range(w):
        x, y = x + dx[nd], y + dy[nd]
        time += 1
        if x == 0 and y == 0:
            print(time)
            sys.exit()
print(-1)
