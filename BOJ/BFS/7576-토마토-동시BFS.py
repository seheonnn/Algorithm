import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

# 여러 좌표에 대하여 동시에 BFS 수행 *****
def bfs():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:  # 익은 토마토 좌표를 모두 한 번에 큐에 추가
                queue.append((i, j))
                visited[i][j] = 1  # 방문 표시

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = 1
                queue.append((nx, ny))

bfs() # 익은 토마토들에 대하여 동시에 BFS 작동해야함

r = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            sys.exit()
        else:
            r = max(r, graph[i][j])
print(r - 1) # 1에서 시작하므로 마지막에 1 빼야