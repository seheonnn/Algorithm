# import sys
# sys.setrecursionlimit(10**6)

# input = sys.stdin.readline

# n = int(input())
# graph = [[] for _ in range(n+1)]
# visited = [-1] * (n+1)
# for _ in range(n-1):
#     u, v, w = map(int, input().split())
#     graph[u].append((v, w))
#     graph[v].append((u, w))

# def dfs(node, dist):
#     for cur, w in graph[node]:
#         if visited[cur] == -1: # -1은 아직 방문하지 않음
#             visited[cur] = dist + w
#             dfs(cur, visited[cur])

# visited[1] = 0 # 거리가 0임
# dfs(1, 0)
# farthest_node = visited.index(max(visited)) # 1에서 가장 먼 거리에 있는 정점 선택

# # 다시 dfs하여 1에서 가장 먼 거리의 정점을 기준으로 거리 계산
# visited = [-1] * (n+1)
# visited[farthest_node] = 0
# dfs(farthest_node, 0)
# r = max(visited)
# print(r)


import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def BFS(node, dist):
    queue = deque()
    queue.append((node, dist))
    while queue:
        node, dist = queue.popleft()
        for cur, w in graph[node]:
            if visited[cur] == -1:
                visited[cur] = dist + w
                queue.append((cur, visited[cur]))

visited[1] = 0
BFS(1, 0)
farthest_node = visited.index(max(visited))

visited = [-1] * (n + 1)
visited[farthest_node] = 0
BFS(farthest_node, 0)
r = max(visited)
print(r)