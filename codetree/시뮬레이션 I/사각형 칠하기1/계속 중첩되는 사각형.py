import sys

input = sys.stdin.readline

OFFSET = 100
graph = [[0] * (2 * OFFSET + 1) for _ in range(2 * OFFSET + 1)]
n = int(input())

col = 1  # 빨간색 : 0, 파란색 : 1
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
    if col == 1:
        col = 0
    elif col == 0:
        col = 1
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = col

r = 0
for lst in graph:
    r += sum(lst)
print(r)
