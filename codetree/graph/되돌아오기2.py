# 그래프 - 되돌아오기2

import  sys
input = sys.stdin.readline

dx, dy = [0,1,0,-1], [1,0,-1,0]
x, y = 0, 0
nd = 0
time = 0
s = input().strip()
for d in s:
    time += 1
    if d == 'F':
        x, y = x + dx[nd], y + dy[nd]
    elif d == 'R':
        nd = (nd + 1) % 4
    elif d == 'L':
        nd = (nd - 1) % 4
    if x == 0 and y == 0:
        print(time)
        break

if x != 0 and y != 0:
    print(-1)