import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1,0,-1,0], [0,1,0,-1]
visited = [[0] * m for _ in range(n)]

def bfs(x, y):
    global k
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                continue
            if graph[nx][ny] > k and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

result = {}
for k in range(1, 101):
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > k and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j)
                cnt += 1
    result[k] = cnt

m = max(result.values())
r = [key for key, value in result.items() if value == m]
print(r[0], m)