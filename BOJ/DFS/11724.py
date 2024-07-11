# DFS(인접리스트) - 트리의 부모 찾기

import sys
sys.setrecursionlimit(10000) # 재귀 제한 풀기

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
