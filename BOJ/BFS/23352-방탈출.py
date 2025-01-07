import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
r = []

def bfs(sx, sy):
    queue = deque()
    distance = 0 # 거리
    queue.append((sx, sy, distance))
    while queue:
        x, y, distance = queue.popleft() # 여기에서 x, y가 덮어씌워지므로 시작점은 sx, sy로 선언
        poss = False # 더 이동이 가능한지 체크
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                continue
            if graph[nx][ny] != 0 and visited[nx][ny] == 0:
                poss = True
                queue.append((nx, ny, distance + 1))
                visited[nx][ny] = 1

        if not poss:
            r.append((distance, graph[sx][sy] + graph[x][y])) # r 배열에 총 거리와 시작점 값 + 끝점 값 저장

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            visited = [[0] * m for _ in range(n)] # 새로 시작할 때마다 visited 초기화
            visited[i][j] = 1
            bfs(i, j)

r.sort(key=lambda x:(x[0], x[1]), reverse=True)
print(r[0][1])
