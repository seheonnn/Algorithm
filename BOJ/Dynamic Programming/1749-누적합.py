# 부분 누적합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m + 1) for _ in range(n + 1)]

# 누적 합 계산
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = graph[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

r = -sys.maxsize

# (x1, y1)부터 (x2, y2)까지의 부분합 계산
for x1 in range(1, n + 1):
    for y1 in range(1, m + 1):
        for x2 in range(x1, n + 1):
            for y2 in range(y1, m + 1):
                # 부분 행렬의 합 계산
                tmp = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
                r = max(r, tmp)

print(r)