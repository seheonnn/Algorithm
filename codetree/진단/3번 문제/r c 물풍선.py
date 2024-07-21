import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

r, c = map(int, input().split())
r, c = r - 1, c - 1
sum = 0
for i in range(n):
    for j in range(n):
        if i == r or j == c:
            if graph[i][j] < graph[r][c]:
                graph[i][j] = 0

for rows in graph:
    for n in rows:
        print(n, end=" ")
    print()