import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                visited[nx][ny] = 1
                # graph[nx][ny] = 2 # 하나의 배열만을 사용하므로 감염 여부는 visited배열을 이용
                queue.append((nx, ny))

# 최대 안전 영역을 저장할 변수
r = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            continue
        graph[i][j] = 1  # 첫 번째 벽

        for x in range(i, n):
            for y in range(m):
                if graph[x][y] != 0 or (x == i and y <= j):
                    continue
                graph[x][y] = 1  # 두 번째 벽

                for p in range(x, n):
                    for q in range(m):
                        if graph[p][q] != 0 or (p == x and q <= y):
                            continue
                        graph[p][q] = 1  # 세 번째 벽

                        # BFS 수행 후 안전 영역 계산
                        visited = [[0] * m for _ in range(n)]
                        for a in range(n):
                            for b in range(m):
                                if graph[a][b] == 2 and visited[a][b] == 0:
                                    visited[a][b] = 1
                                    bfs(a, b)

                        # 안전 영역 크기 계산
                        tmp = 0
                        for k in range(n):
                            for l in range(m):
                                # graph 따로 복사하거나 하지 않고 하나만 사용하므로 graph & visited 배열 모두를 이용하여 감염여부 확인
                                if graph[k][l] == 0 and visited[k][l] == 0:
                                    tmp += 1
                        r = max(r, tmp)

                        # 세 번째 벽 제거
                        graph[p][q] = 0

                # 두 번째 벽 제거
                graph[x][y] = 0

        # 첫 번째 벽 제거
        graph[i][j] = 0

print(r)
