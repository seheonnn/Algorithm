# Linked List - 뱀

import sys
from collections import deque

queue = deque()
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    x, y = map(int, sys.stdin.readline().split()) #####
    graph[x][y] = 2

l = int(sys.stdin.readline())
turn = []
for _ in range(l):
    t, d = sys.stdin.readline().split()
    turn.append((int(t), d))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
nd = 0
nx = 1
ny = 1
time = 0
i = 0
queue.append((nx, ny))

while True:
    nx = nx + dx[nd]
    ny = ny + dy[nd]
    time += 1
    if nx < 1 or nx > n or ny < 1 or ny > n or (nx, ny) in queue:
        break
    queue.append((nx, ny))
    if graph[nx][ny] == 0:
        queue.popleft()
    else:
        graph[nx][ny] = 0
    if time == turn[i][0]:
        if turn[i][1] == 'L':
            nd = (nd - 1) % 4
        elif turn[i][1] == 'D':
            nd = (nd + 1) % 4

        if i + 1 < len(turn):
            i += 1
print(time)
