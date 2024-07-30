import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

r1, c1 = map(int, input().split())

for i in range(0, r1):
    for j in range(0, c1):
        if graph[i][j] < graph[r1-1][c1-1]:
            graph[i][j] = 0

for rows in graph:
    for c in rows:
        print(c, end=" ")
    print()