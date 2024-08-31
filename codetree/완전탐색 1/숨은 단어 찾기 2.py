import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx, dy = [0, 1, 0, -1, -1, -1, 1, 1], [1, 0, -1, 0, -1, 1, -1, 1]
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] != "L":
            continue
        for x, y in zip(dx, dy):
            nx, ny = i + x, j + y
            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                continue
            if graph[nx][ny] == "E":
                nx, ny = nx + x, ny+y
                if nx < 0 or n <= nx or ny < 0 or m <= ny:
                    continue
                if graph[nx][ny] == "E":
                    cnt += 1
print(cnt)