# 그래프

import sys
input = sys.stdin.readline

n, t = map(int, input().split())
r, c, d = input().split()

x, y = int(r) - 1, int(c) - 1

if d == 'U':
    nd = 2
elif d == 'D':
    nd = 1
elif d == 'R':
    nd = 0
elif d == 'L':
    nd = 3

dx = [0, 1, -1,  0]
dy = [1, 0,  0, -1]

for _ in range(t):
    nx, ny = x + dx[nd], y + dy[nd]
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
        x, y = nx, ny
    else:
        nd = 3 - nd

print(x + 1, y + 1)