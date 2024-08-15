import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

# 중복된 경로에 대한 계산이 필요함 -> DFS/BFS가 아닌 Memozation
def memozation(x, y):
    if dp[x][y] != -1: # 이미 계산된 값이 있으면 그 값을 반환
        return dp[x][y]

    dp[x][y] = 1  # 현재 위치도 포함해서 길이 1부터 시작
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > graph[x][y]:
            dp[x][y] = max(dp[x][y], memozation(nx, ny) + 1)

    return dp[x][y]

m = -sys.maxsize
for i in range(n):
    for j in range(n):
        m = max(m, memozation(i, j))

print(m)
