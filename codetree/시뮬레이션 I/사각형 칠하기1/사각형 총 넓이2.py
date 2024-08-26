import sys
input = sys.stdin.readline

n = int(input())
OFFSET = 100

graph = [[0] * (2 * OFFSET) for _ in range(2 * OFFSET)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

r = 0
for lst in graph:
    r += sum(lst)
print(r)