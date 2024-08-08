import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def initialize():
    # DP 테이블 초기화
    dp[0][n-1] = a[0][n-1]

    # 첫 번째 행 초기화 (오른쪽에서 왼쪽으로)
    for j in range(n-2, -1, -1):
        dp[0][j] = dp[0][j+1] + a[0][j]

    # 첫 번째 열 초기화 (위에서 아래로)
    for i in range(1, n):
        dp[i][n-1] = dp[i-1][n-1] + a[i][n-1]

initialize()

for i in range(1, n):
    for j in range(n-2, -1, -1):
        dp[i][j] = min(dp[i-1][j], dp[i][j+1]) + a[i][j]

print(dp[n-1][0])

