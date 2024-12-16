import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    print(v, end=" ")
    for cur in sorted(graph[v]): # 작은 자식부터 탐색
        if visited[cur] == 0:
            visited[cur] = 1
            dfs(cur)

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for cur in sorted(graph[v]):
            if visited[cur] == 0:
                visited[cur] = 1
                queue.append(cur)

visited[v] = 1
dfs(v)

print()

visited = [0] * (n + 1)
visited[v] = 1
bfs(v)