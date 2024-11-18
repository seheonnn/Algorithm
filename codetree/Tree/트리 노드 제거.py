import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tar = int(input())
graph = [[] for _ in range(n)]
root = -1

for i, num in enumerate(arr):
    if num == -1:
        root = i # root 노드 저장
    else:
        graph[num].append(i)

visited = [0] * n # 방문 여부가 아닌 삭제 여부를 나타내는 배열

cnt = 0
# def dfs(node):
#     global cnt

#     if visited[node] == 1:
#         return

#     is_leaf = True
#     for cur in graph[node]:
#         if visited[cur] == 1:
#             continue
#         dfs(cur)
#         is_leaf = False
#     if is_leaf:
#         cnt += 1

def bfs(node):
    global cnt
    queue = deque()
    if visited[node] == 1:
        return
    queue.append(node)
    while queue:
        node = queue.popleft()
        is_leaf = True
        for cur in graph[node]:
            if visited[cur] == 1:
                continue
            queue.append(cur)
            is_leaf = False
        if is_leaf:
            cnt += 1


if tar == root:
    print(0)
else:
    # 노드 삭제
    visited[tar] = 1
    # dfs(root)
    bfs(root)
    print(cnt)