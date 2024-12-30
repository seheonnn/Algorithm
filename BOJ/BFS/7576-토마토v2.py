import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                visited[i][j] = 1
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy [i]
            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs()
r = 0
poss = True

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            poss = False
        else:
            r = max(r, graph[i][j])

if poss:
    print(r - 1)
else:
    print(-1)