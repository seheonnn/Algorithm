import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
def bfs(v):
    global cnt
    queue = deque()
    queue.append(v)
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                cnt += 1

visited[1] = 1
bfs(1)
print(cnt)