from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(v):
    global cnt
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

cnt = 0
for i in range(1, n+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1
print(cnt)