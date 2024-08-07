import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

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
            if graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                cnt += 1
                visited[nx][ny] = 1
                queue.append((nx, ny))

result = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt = 1
            visited[i][j] = 1
            bfs(i, j)
            result.append(cnt)

r = [i for i in result if i >= 4]
print(len(r), max(result)) # r 이 빈 리스트인 경우, 즉 모든 값이 4보다 작은 경우 max 호출 시 런타임 에러 발생