
import sys
import collections

input = sys.stdin.readline
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
queue = collections.deque()

# push all the ripe tomatoes into queue.
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

# ripen the other tomatoes.
while queue:  # bfs
    i, j = queue.popleft()
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 0:
            graph[ni][nj] = graph[i][j] + 1
            queue.append((ni, nj))

# calculate the answer.
answer = max(map(max, graph)) - 1
print(graph)
for row in graph:
    if 0 in row:
        answer = -1
print(answer)