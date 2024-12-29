import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx, ny))

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1 # x, y -> 2차원 배열상 y, x임

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                bfs(i, j)
                cnt += 1

    print(cnt)