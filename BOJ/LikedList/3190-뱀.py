import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1
l = int(input())
turn = []
for _ in range(l):
    x, c = input().split()
    turn.append((int(x), c))

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
nd = 0
x, y = 1, 1 # 뱀의 머리 위치
queue = deque()
queue.append((x, y))
time = 0
i = 0 # 방향 전환 정보 인덱스
while True:
    x, y = x + dx[nd], y + dy[nd]
    time += 1
    if x < 1 or n < x or y < 1 or n < y or (x, y) in queue:
        break

    # x, y가 범위 안이라면 큐에 추가
    queue.append((x, y))

    if graph[x][y] == 1:
        graph[x][y] = 0
    elif graph[x][y] == 0:
        queue.popleft()

    if time == turn[i][0]:
        if turn[i][1] == "L":
            nd = (nd - 1) % 4
        elif turn[i][1] == "D":
            nd = (nd + 1) % 4

        if i + 1 < len(turn):
            i += 1

print(time)
