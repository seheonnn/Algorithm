# BFS
import sys
from collections import deque
N = int(sys.stdin.readline())
count = []
def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0 # 2. 방문한 집은 0으로 바꿈
    cnt = 1 # 3. 따라서 cnt=1 부터 시작임

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1

    return cnt
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1: # 1. BFS가 호출될 때 이미 집 하나 방문한 상태
            count.append(BFS(i, j))
count.sort()
print(len(count))
for s in count:
    print(s)