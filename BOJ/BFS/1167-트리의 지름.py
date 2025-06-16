import sys
from collections import deque

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)


def bfs(start):
    queue = deque()
    visited[start] = 0
    queue.append((visited[start], start))

    while queue:
        d, cur = queue.popleft()
        for next, w in graph[cur]:
            if visited[next] == -1:
                visited[next] = d + w
                queue.append((visited[next], next))


for _ in range(n):
    arr = list(map(int, input().split()))
    u = arr[0]
    i = 1
    while arr[i] != -1:
        v = arr[i]
        w = arr[i + 1]
        graph[u].append((v, w))
        i += 2

bfs(1)
farthest_node = visited.index(max(visited));

visited = [-1] * (n + 1)
bfs(farthest_node)
r = max(visited)
print(r)