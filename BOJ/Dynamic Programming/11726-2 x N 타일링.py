import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

# dp[i] = 2 x i 크기의 사각형을 의미
# 2 x n 크기의 사각형을 1 x 2 or 2 x 1 타일로 채우기
dp[0] = 1 # 2 x 0 사각형에는 아무것도 놓지 않는 경우 하나
dp[1] = 1 # 2 x 1 사각형에는 2 x 1 놓는 경우 하나

# 점화식
# dp[i] = dp[i - 1] + dp[i - 2]
for i in range(2, n+1):
    # 두 타일 합산이므로 +임
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
print(dp[n])