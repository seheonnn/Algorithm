import sys
input = sys.stdin.readline

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

def initialize():
    dp[0][0] = a[0][0]

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], a[i][0])
    for j in range(1, n):
        dp[0][j] = min(dp[0][j-1], a[0][j])

initialize()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), a[i][j])
대
print(dp[n-1][n-1])
