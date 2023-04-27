import sys
sys.setrecursionlimit(10000)
def DFS(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            DFS(i)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

DFS(1) # 시작점이 1로 고정
print(sum(visited)-1) # 시작지점 빼주기