import sys
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

def DFS(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = s
            DFS(i)
DFS(1)
for i in range(2, N+1):
    print(visited[i])
# print(graph)
# print(visited)