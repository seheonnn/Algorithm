import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
x, y = map(int, input().split())
x, y = x-1, y-1
dx, dy = [-1,1,-1,1], [-1,-1,1,1]

def dfs(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or n <= nx or ny < 0 or n <= ny:
            continue
        if graph[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny)

visited[x][y] = 1
dfs(x, y)

for rows in visited:
    for c in rows:
        print(c, end=" ")
    print()
