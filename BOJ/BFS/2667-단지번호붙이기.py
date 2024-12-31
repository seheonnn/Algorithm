import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or n <= nx or ny < 0 or n <= ny:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                queue.append((nx, ny))

r = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt = 1
            visited[i][j] = 1
            bfs(i, j)
            r.append(cnt)

r.sort()
print(len(r))
for el in r:
    print(el)
