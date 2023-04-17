# y 좌표 기준 정렬

import sys
n = int(sys.stdin.readline())
points = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((y,x))
points.sort()
for p in points:
    print(p[1], p[0])