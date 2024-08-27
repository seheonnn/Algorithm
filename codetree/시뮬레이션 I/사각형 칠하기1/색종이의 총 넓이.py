import sys
input = sys.stdin.readline

OFFSET = 100
graph = [[0] * (2*OFFSET + 1) for _ in range(2*OFFSET+1)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+8):
        for j in range(y, y+8):
            graph[i][j] = 1
r = 0
for lst in graph:
    r += sum(lst)
print(r)