import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(v):
    for i in range(n):
        if graph[v][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)

for i in range(n):
    visited = [0] * n
    dfs(i)

    for j in range(n):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

