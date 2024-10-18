import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input().strip())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    visited[v] = 1
    dp[v][0] = 1
    for cur in graph[v]:
        if not visited[cur]:
            dfs(cur)
            dp[v][0] += min(dp[cur][0], dp[cur][1])
            dp[v][1] += dp[cur][0]
dfs(1)
print(min(dp[1][0], dp[1][1]))

