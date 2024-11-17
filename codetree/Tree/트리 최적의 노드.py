import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
graph = [[]for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# def dfs(v, dist):
#     for cur in graph[v]:
#         if visited[cur] == -1:
#             visited[cur] = dist + 1 # 모든 간선의 길이는 1
#             dfs(cur, visited[cur])

def bfs(v, dist):
    queue = deque()
    queue.append((v, dist))
    while queue:
        v, dist = queue.popleft()
        for cur in graph[v]:
            if visited[cur] == -1:
                visited[cur] = dist + 1
                queue.append((cur, visited[cur]))

visited = [-1] * (n + 1)
visited[1] = 0
# dfs(1, 0)
bfs(1, 0)
farthest_nodeA = visited.index(max(visited))

visited = [-1] * (n + 1)
visited[farthest_nodeA] = 0
# dfs(farthest_nodeA, 0)
bfs(farthest_nodeA, 0)
farthest_nodeB = visited.index(max(visited))

# 리스트 복사, 노드 A 기준 모든 정점에 대한 거리 저장 리스트
distsA = visited[:] # or visited.copy())

visited = [-1] * (n + 1)
visited[farthest_nodeB] = 0
# dfs(farthest_nodeB, 0)
bfs(farthest_nodeB, 0)
distsB = visited[:] # 노드 B 기준 모든 정점에 대한 거리 저장 리스트

r = sys.maxsize
for i in range(1, n + 1):
    tmp = max(distsA[i], distsB[i])
    r = min(r, tmp)

print(r)