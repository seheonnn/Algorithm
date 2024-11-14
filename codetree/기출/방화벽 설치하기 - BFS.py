import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


# BFS 함수 정의 (불이 퍼지게 하는 함수)
def bfs(graph_copy):
    queue = deque()

    # 초기 불 위치 큐에 추가
    for i in range(n):
        for j in range(m):
            if graph_copy[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph_copy[nx][ny] == 0 and visited[nx][ny] == 0:
                graph_copy[nx][ny] = 2  # 불 퍼뜨리기
                visited[nx][ny] = 1
                queue.append((nx, ny))


empty = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]  # 빈 공간 저장

r = 0

# 모든 빈 칸 중 3개의 위치에 방화벽 설치
for i in range(len(empty)):
    for j in range(i + 1, len(empty)):
        for k in range(j + 1, len(empty)):
            # 방화벽을 설치했다가 복구해야 하므로 그래프 복사본 생성
            graph_copy = [list(row) for row in graph]  # 깊은 복사 주의!!

            # 빈공간 (0인 곳)에 방화벽 설치
            x1, y1 = empty[i]
            x2, y2 = empty[j]
            x3, y3 = empty[k]
            graph_copy[x1][y1] = 1
            graph_copy[x2][y2] = 1
            graph_copy[x3][y3] = 1

            # BFS로 불 퍼뜨리기 후 안전 영역 계산
            visited = [[0] * m for _ in range(n)]  # 방문 여부 초기화
            bfs(graph_copy)

            # 안전 영역 계산
            safe = 0
            for row in graph_copy:
                safe += row.count(0)

            # 최대 안전 영역 갱신
            r = max(r, safe)

print(r)
