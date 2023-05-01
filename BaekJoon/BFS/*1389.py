import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split()) # 유저 수, 친구 관계 수
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
def BFS(s):
    queue = deque()
    queue.append(s)
    check = [0] * (N+1)
    check[s] = 1
    bacon = [0] * (N+1)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if check[i] == 0:
                bacon[i] = bacon[x] + 1 # 현재 노드 x에서 다음 노드 i로 이동할 때, 노드 i까지의 최소 이동 횟수
                queue.append(i)
                check[i] = 1
    return sum(bacon)

result = []
for i in range(1, N+1):
    result.append(BFS(i))
print(result.index(min(result))+1) # index 0 에서 시작하므로

