import sys

input = sys.stdin.readline

n = int(input())
graph = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

nd = 0
x, y = n - 1, n - 1
for i in range(n * n, 0, -1):
    graph[x][y] = i
    visited[x][y] = 1

    nx, ny = x + dx[nd], y + dy[nd]
    if nx < 0 or n <= nx or ny < 0 or n <= ny or graph[nx][ny] != 0: # 범위에서 벗어나거나 이미 숫자가 있다면
        nd = (nd + 1) % 4 # 방향 전환
        x, y = x + dx[nd], y + dy[nd]
    else:
        x, y = nx, ny

for lst in graph:
    for num in lst:
        print(num, end=" ")
    print()