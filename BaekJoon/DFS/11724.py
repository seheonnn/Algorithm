# DFS
import sys
sys.setrecursionlimit(10000)
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
check = [0] * (N + 1)
def DFS(s):
    check[s] = 1
    for i in graph[s]:
        if check[i] == 0:
            DFS(i)
# 시작점이 고정되어 있지 않으므로, 모든 노드에 대하여 DFS 반복 수행
cnt = 0
for i in range(1, N+1):
    if not check[i]:
        DFS(i)
        cnt += 1
print(cnt)