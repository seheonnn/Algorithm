import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
who = 0
def bfs(x, y):
    global cnt, who
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or n <= nx or ny < 0 or n <= ny:
                continue
            if graph[nx][ny] != 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1
result = [0, 0]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2 and visited[i][j] == 0:
            visited[i][j] = 1
            cnt = 1
            bfs(i, j)
            result[0] = cnt
        elif graph[i][j] == 3 and visited[i][j] == 0:
            visited[i][j] = 1
            cnt = 1
            bfs(i, j)
            result[1] = cnt

print(result[0], result[1])