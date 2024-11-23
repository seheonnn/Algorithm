import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# def dfs(node, depth):
#     global cnt
#     is_leaf = True
#     for cur in graph[node]:
#         if visited[cur] == 0:
#             visited[cur] = 1
#             dfs(cur, depth + 1)
#             is_leaf = False

#     if is_leaf:
#         cnt += depth

def bfs(node, depth):
    global cnt
    queue = deque()
    queue.append((node, depth))
    while queue:
        node, depth = queue.popleft()
        is_leaf = True  # 리프 노드 판별, 위치 주의 !!

        for cur in graph[node]:
            if visited[cur] == 0:
                visited[cur] = 1
                queue.append((cur, depth + 1))
                is_leaf = False
        if is_leaf:
            cnt += depth


cnt = 0  # 리프 노드의 깊이 전체합
visited[1] = 1
bfs(1, 0)
if cnt % 2 == 1:  # 리프 노드 깊이의 전체합이 홀수여야 a가 이길 수 있음
    print(1)
else:
    print(0)