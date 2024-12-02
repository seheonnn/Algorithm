import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

t = int(input())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or m <= nx or ny < 0 or n <= ny:
            continue
        if visited[nx][ny] == 0 and graph[nx][ny] == 1:
            visited[nx][ny] = 1
            dfs(nx, ny)

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]

    cnt = 0
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                dfs(i, j) # 배추(1)가 모인 곳만 dfs로 방문 표시
                cnt += 1

    print(cnt)
