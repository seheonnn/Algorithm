# BFS
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

check = [0] * (N+1)
def BFS(s):
    queue = deque()
    queue.append(s)
    check[s] = 1
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if check[i] == 0:
                queue.append(i)
                check[i] = 1
# 시작점이 고정되어 있지 않으므로, 모든 노드에 대하여 BFS 반복 수행
cnt = 0
for i in range(1, N+1):
    if not check[i]:
        BFS(i)
        cnt += 1
print(cnt)