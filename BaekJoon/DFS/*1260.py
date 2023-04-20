# DFS: 재귀함수, BFS: Queue, deque로 구현
import sys
from collections import deque

def dfs(V):
    visited1[V] = 1
    print(V, end=" ")
    for i in range(1, N + 1):
        if visited1[i] == 0 and graph[V][i] == 1: # 해당 vertex와 연결된 수들 중, 방문하지 않은 수에 대하여 dfs
            dfs(i)
def bfs(V):
    q = deque()
    q.append(V)
    visited2[V] = 1
    while q:
        V = q.popleft() # queue는 FIFO
        print(V, end=" ")
        for i in range(1, N + 1):
            if visited2[i] == 0 and graph[V][i] == 1: # 해당 vertex와 연결된 수들 중, 방문하지 않은 수에 대하여 dfs
                q.append(i)
                visited2[i] = 1

N, M, V = map(int, sys.stdin.readline().split())
graph = [[0] * (N+1) for _ in range(N + 1)]
visited1 = [0] * (N + 1)
visited2 = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1 # a가 b랑 연결되어 있음을 의미.

# print(graph)
# print(visited1)
# print(visited2)
dfs(V)
print()
bfs(V)
