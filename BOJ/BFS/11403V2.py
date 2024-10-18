from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        cur = queue.popleft()
        for i in range(n):
            if graph[cur][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)

for i in range(n):
    visited = [0] * n
    bfs(i)

    for j in range(n):
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
