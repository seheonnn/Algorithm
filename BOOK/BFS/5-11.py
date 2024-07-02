# BFS 구현 - 미로 탈출

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


bfs(0, 0)

print(graph[n-1][m-1])
