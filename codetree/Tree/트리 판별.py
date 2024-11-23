import sys
from collections import deque
input = sys.stdin.readline

MAX_N = 10000
m = int(input().strip())
graph = [[] for _ in range(MAX_N + 1)]
visited = [0] * (MAX_N + 1)
used = [False] * (MAX_N + 1) # 각 노드가 그래프에 쓰이는 노드인지 표시
deg = [0] * (MAX_N + 1) # 각 노드에 들어오는 간선의 개수

root = 0 # 노드는 1부터 시작
is_tree = True # 트리인지

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # a에서 b로 가는 간선이 존재함
    used[a] = True
    used[b] = True

    deg[b] += 1 # b에 들어오는 간선의 개수

# dfs
# def dfs(node):
#     for cur in graph[node]:
#         if visited[cur] == 0:
#             visited[cur] = 1
#             dfs(cur)
# bfs
def bfs(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        for cur in graph[node]:
            if visited[cur] == 0:
                visited[cur] = 1
                queue.append(cur)

# 루트 노드 찾기 **
for i in range(MAX_N + 1):
    if used[i] and deg[i] == 0: # root에는 들어오는 간선이 없음
        if root != 0: # 루트 노드가 초기값이 아니라면 이미 루트가 존재한다는 것 -> root 가 여러개 = 트리 아님
            is_tree = False
        root = i

# # 루트가 없다면 트리 아님
if root == 0:
    is_tree = False

for i in range(1, MAX_N): # 루트 노드를 제외한 모든 노드에는 들어오는 간선이 1개씩 있음 (들어오는 간선은 무조건 하나!!)
    if used[i] and i != root and deg[i] != 1:
        is_tree = False

# root 노드를 구하였으면 root로부터 모든 정점에 도달할 수 있는지 확인
if is_tree and root != 0:
    visited[root] = True
    bfs(root)

for i in range(1, MAX_N + 1):
    if used[i] and visited[i] == 0: # root부터 dfs한 후 현재 사용중인 노드들 중에서 방문하지 않은 곳이 있으면 트리가 아님
        is_tree = False

if is_tree:
    print(1)
else:
    print(0)