# DFS - 인접 리스트
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
def dfs(v):
    global cnt
    visited[v] = True
    for cur in graph[v]:
        if not visited[cur]:
            dfs(cur)
            cnt += 1
dfs(1)
print(cnt)
