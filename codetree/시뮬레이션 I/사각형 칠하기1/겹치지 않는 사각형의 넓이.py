import sys
input = sys.stdin.readline

OFFSET = 1000
graph = [[0] * (2 * OFFSET + 1) for _ in range(2 * OFFSET + 1)]
for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
for i in range(x1, x2):
    for j in range(y1, y2):
        graph[i][j] = 2

for i in range(2 * OFFSET + 1):
    for j in range(2 * OFFSET + 1):
        if graph[i][j] == 2:
            graph[i][j] = 0

r = 0
for lst in graph:
    r += sum(lst)
print(r)

