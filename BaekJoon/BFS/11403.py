# BFS 경로 탐색 -> floyd washall
# graph[i][j] = 1 i, j 사이에 "간선"이 있다는 뜻.
import sys
from collections import deque

def BFS(s):
    queue = deque()
    queue.append(s)
    check = [0] * N

    while queue:
        x = queue.popleft()
        for i in range(N):
            if check[i] == 0 and graph[x][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[s][i] = 1


N = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
for i in range(N):
    BFS(i)
for i in visited:
    print(*i) # 공백으로 구분하여 출력

