import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1) # 부모 정보를 저장할 리스트

def BFS(node):
    queue = deque()
    queue.append(node)
    while queue:
        cur = queue.popleft()
        for child in graph[cur]:
            if visited[child] == 0:
                visited[child] = cur
                queue.append(child)

visited[1] = 1
BFS(1)

for i in range(2, n + 1):
    print(visited[i])
