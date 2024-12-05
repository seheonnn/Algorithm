import sys
input = sys.stdin.readline

n = int(input().strip())
num = int(input().strip())

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
graph = [[0] * n for _ in range(n)]
x, y = 0, 0
d = 0

for i in range(n * n, 0, -1):
    if i == num: # num의 위치 저장
        a, b = x + 1, y + 1
    graph[x][y] = i
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
        x, y = nx, ny
    else:
        d = (d + 1) % 4
        x, y = x + dx[d], y + dy[d]

for rows in graph:
    for el in rows:
        print(el, end=" ")
    print()
print(a, b)