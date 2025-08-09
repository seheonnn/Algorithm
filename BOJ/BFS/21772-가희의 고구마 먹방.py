import sys
from collections import deque

input = sys.stdin.readline

r, c, time = map(int, input().split())
visited = [[[-1] * (time + 1) for _ in range(c)] for _ in range(r)]
graph = []
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(x, y, time):
    queue = deque()
    queue.append((0, 0, x, y, set()))  # cnt, t, x, y, eaten. 한 번 먹은 고구마는 다음에 먹을 수 없음
    visited[x][y][0] = 0

    while queue:
        cnt, t, x, y, eaten = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or r <= nx or ny < 0 or c <= ny: continue
            if graph[nx][ny] == '#': continue

            new_cnt = cnt
            new_eaten = set(eaten)

            if graph[nx][ny] == 'S' and (nx, ny) not in eaten:
                new_cnt += 1
                new_eaten.add((nx, ny))
            if t + 1 <= time and visited[nx][ny][t + 1] <= new_cnt:
                visited[nx][ny][t + 1] = new_cnt
                queue.append((new_cnt, t + 1, nx, ny, new_eaten))


for _ in range(r):
    s = input().strip()
    graph.append(s)

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'G':
            bfs(i, j, time)
result = 0
for i in range(r):
    for j in range(c):
        result = max(result, visited[i][j][time])
print(result)

