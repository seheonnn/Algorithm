# DFS
import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
count = []

def DFS(x, y):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    graph[x][y] = 0 # 2. 방문한 집은 0으로 바꿈
    cnt = 1 # 3. 따라서 cnt=1 부터 시작임

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            cnt += DFS(nx, ny)
    return cnt

graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1: # 1. BFS가 호출될 때 이미 집 하나 방문한 상태
            count.append(DFS(i, j))
count.sort()
print(len(count))
for s in count:
    print(s)