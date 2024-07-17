# 그래프 - 격자 위의 편안한 상태

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
for _ in range(m):
    r, c = map(int, input().split())
    graph[r][c] = 1

    cnt = 0
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if nr < 1 or n < nr or nc < 1 or n < nc:
            continue
        if graph[nr][nc] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)
