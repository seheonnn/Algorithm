# 그래프

import sys

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def cnt_graph(x, y, cnt=0):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or n <= nx or ny < 0 or n <= ny:
            continue
        if graph[nx][ny] == 1:
            cnt += 1
    return cnt

cnt_ones = 0
for i in range(n):
    for j in range(n):
        if cnt_graph(i, j) >= 3:
            cnt_ones += 1

print(cnt_ones)