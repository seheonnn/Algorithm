import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# def dfs(v, dist):
#     for cur, w in graph[v]:
#         if visited[cur] == -1:
#             visited[cur] = dist + w
#             dfs(cur, visited[cur])

def bfs(v, dist):
    queue = deque()
    queue.append((v, dist))
    while queue:
        v, dist = queue.popleft()
        for cur, w in graph[v]:
            if visited[cur] == -1:
                visited[cur] = dist + w
                queue.append((cur, visited[cur]))


visited = [-1] * (n + 1)
visited[1] = 0
bfs(1, 0)
farthest_node = visited.index(max(visited)) # 1에서 가장 먼 노드 찾기

visited = [-1] * (n + 1)
visited[farthest_node] = 0
bfs(farthest_node, 0)
r = max(visited)
print(r)