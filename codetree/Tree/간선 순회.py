import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(50000)

n, d = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)  # 누적 거리
edges = [-1] * (n + 1)  # 간선의 수
max_dist = (0, 0)  # 가장 먼거리의 노드의 지나는 간선 수, 가중치 합

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# def dfs(v, dist):
#     global max_dist, last_node
#     for cur, w in graph[v]:
#         if visited[cur] == -1 and edges[cur] == -1:
#             visited[cur] = dist + w
#             edges[cur] = edges[v] + 1

#             cur_dist = (edges[cur], -visited[cur]) # 지나는 간선 수, -거리

#             if cur_dist > max_dist: # 지나는 간선 수가 동일하면 -거리가 큰 경우 즉, 거리가 짧은 경우
#                 max_dist = cur_dist # 갱신
#                 last_node = cur # 갱신되었을 때의 노드

#             dfs(cur, visited[cur])

def bfs(v, dist):
    global max_dist, last_node
    queue = deque()
    queue.append((v, dist))
    while queue:
        v, dist = queue.popleft()
        for cur, w in graph[v]:
            if visited[cur] == -1 and edges[cur] == -1:
                visited[cur] = dist + w
                edges[cur] = edges[v] + 1

                cur_dist = (edges[cur], -visited[cur])

                if cur_dist > max_dist:
                    max_dist = cur_dist
                    last_node = cur

                queue.append((cur, visited[cur]))

edges = [-1] * (n + 1)
visited[1] = 0
edges[1] = 0
# dfs(1, visited[1])
bfs(1, visited[1])

visited = [-1] * (n + 1)
edges = [-1] * (n + 1)
visited[last_node] = 0
edges[last_node] = 0
# dfs(last_node, visited[last_node])
bfs(last_node, visited[last_node])

print(1 + (-max_dist[1] - 1) // d)  # 나머지가 있을 경우 올림이 됨