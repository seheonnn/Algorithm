import sys
from collections import deque

input = sys.stdin.readline


def bfs(n, graph, inDegree, dp, times, w):
    queue = deque()
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            queue.append(i)
            dp[i] = times[i]

    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            dp[next] = max(dp[next], dp[cur] + times[next])
            inDegree[next] -= 1
            if inDegree[next] == 0:
                queue.append(next)


tc = int(input())
for t in range(tc):
    n, k = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    inDegree = [0] * (n + 1)
    dp = [0] * (n + 1)
    times = [0] + list(map(int, input().split()))

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        inDegree[y] += 1

    w = int(input())
    bfs(n, graph, inDegree, dp, times, w)
    print(dp[w])
