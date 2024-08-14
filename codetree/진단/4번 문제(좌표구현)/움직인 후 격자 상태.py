import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
nd = 0
x, y = 0, 0
graph = [[0] * n for _ in range(n)]

for _ in range(n):
    d, w = input().split()
    w = int(w)

    if d == "E":
        nd = 0
    elif d == "W":
        nd = 2
    elif d == "N":
        nd = 3
    elif d == "S":
        nd = 1

    for i in range(w):
        x, y =  x + dx[nd], y + dy[nd]
        graph[x][y] += 1

for rows in graph:
    for i in rows:
        print(i, end=" ")
    print()
