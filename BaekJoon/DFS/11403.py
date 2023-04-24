# DFS
import sys
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dfs(s):
    for i in range(N):
        if graph[s][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)
for i in range(N):
    visited = [0 for _ in range(N)]
    dfs(i)
    for j in range(N):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()