import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
s = []
cnt = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for _ in range(k):
    a, b = map(int, input().split())
    s.append((a - 1, b - 1))


def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y))
    cnt += 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or n <= nx or ny < 0 or n <= ny:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                cnt += 1
                visited[nx][ny] = 1
                queue.append((nx, ny))


for a, b in s:
    if visited[a][b] == 0:  # 입력받은 점들 중 방문하지 않은 곳에만 방문
        visited[a][b] = 1
        bfs(a, b)
print(cnt)
