import sys
from collections import deque
N = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
def BFS():
    queue = deque()
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                queue.append((i, j))
                visited[i][j] = 1
                cnt += 1
                dx = [1, 0, -1, 0]
                dy = [0, 1, 0, -1]
                while queue:
                    x, y = queue.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if -1 < nx < N and -1 < ny < N:
                            if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                                visited[nx][ny] = 1
                                queue.append((nx, ny))
    return cnt
print(BFS(), end=" ")
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
visited = [[0] * N for _ in range(N)]
print(BFS())