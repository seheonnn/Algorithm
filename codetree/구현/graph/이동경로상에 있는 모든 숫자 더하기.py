import sys
input = sys.stdin.readline

n, t = map(int, input().split())
cmd = input()
graph = [list(map(int, input().split())) for _ in range(n)]

# 처음 북쪽을 바라봄
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

x, y = n // 2, n // 2
nd = 0

r = graph[x][y]
for c in cmd:
    if c == "L":
        nd = (nd - 1) % 4
    elif c == "R":
        nd = (nd + 1) % 4
    elif c == "F":
        nx, ny = x + dx[nd], y + dy[nd]
        if 0 <= nx < n and 0 <= ny < n:
            r += graph[nx][ny]
            x, y = nx, ny

print(r)
