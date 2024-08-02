import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx, dy = [1, 0], [0, 1]
escape = False
def bfs(x, y):
    global escape
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if nx == (n-1) and ny == (m-1):
                escape = True
            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx ,ny))

visited[0][0] = 1
bfs(0,0)
if escape:
    print(1)
else:
    print(0)
