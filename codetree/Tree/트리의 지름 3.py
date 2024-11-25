import sys
from collections import deque

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

max_dist, last_node = 0, 0


# def dfs(v, ignore_num):
#     global max_dist, last_node

#     for cur, w in graph[v]:
#         if visited[cur] == -1:
#             visited[cur] = visited[v] + w

#             if visited[cur] > max_dist and cur != ignore_num:
#                 max_dist = visited[cur]
#                 last_node = cur

#             dfs(cur, ignore_num)

def bfs(v, ignore_num):
    global max_dist, last_node
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        for cur, w in graph[v]:
            if visited[cur] == -1:
                visited[cur] = visited[v] + w

                if visited[cur] > max_dist and cur != ignore_num:
                    max_dist = visited[cur]
                    last_node = cur

                queue.append(cur)


# 첫 번째 DFS/BFS : 1번 노드에서 가장 먼 노드를 찾음
visited = [-1] * (n + 1)
visited[1] = 0
# dfs(1, -1)
bfs(1, -1)
a = last_node

# 두 번째 DFS/BFS : 노드 a에서 가장 먼 노드를 찾음 (트리의 지름)
visited = [-1] * (n + 1)
max_dist = -1
visited[a] = 0
# dfs(a, -1)
bfs(a, -1)
b = last_node

# 세 번째 DFS/BFS : a에서 가장 먼 노드까지의 거리 (b 제외)
r = 0
visited = [-1] * (n + 1)
max_dist = -1
visited[a] = 0
# dfs(a, b)
bfs(a, b)
r = max(r, max_dist)

# 네 번째 DFS/BFS : b에서 가장 먼 노드까지의 거리 (a 제외)
visited = [-1] * (n + 1)
max_dist = -1
visited[b] = 0
# dfs(b, a)
bfs(b, a)
r = max(r, max_dist)
print(r)