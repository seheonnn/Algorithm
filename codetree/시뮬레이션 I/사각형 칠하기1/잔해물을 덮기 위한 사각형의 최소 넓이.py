import sys
input = sys.stdin.readline

OFFSET = 1000
MAX_R = sys.maxsize

graph = [[0] * (2*OFFSET+1) for _ in range(2*OFFSET+1)]
a = 1

for k in range(1, 3):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = k

min_x, max_x, min_y, max_y = MAX_R, 0, MAX_R, 0
fir = False
for x in range(2*OFFSET+1):
    for y in range(2*OFFSET+1):
        if graph[x][y] == 1:
            fi = True
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

if not fi:
    area = 0
else:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)
print(area)