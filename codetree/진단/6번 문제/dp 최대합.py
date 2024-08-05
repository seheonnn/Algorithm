import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] for _ in range(n)]

# DP 테이블 초기화
dp = [[0] * n for _ in range(n)]
dp[n-1][0] = a[n-1][0]

def initialize():

    for i in range(n - 2, -1, -1):
        dp[i][0] = dp[i + 1][0] + a[i][0]

    for j in range(1, n):
        dp[n - 1][j] = dp[n - 1][j - 1] + a[n - 1][j]

initialize()

for i in range(n-2, -1, -1):
    for j in range(1, n):
        dp[i][j] = max(dp[i+1][j], dp[i][j-1]) + a[i][j]

print(dp[0][n-1])
