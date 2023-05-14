# 동적계획법
import sys

N = int(sys.stdin.readline())
dp = []
for _ in range(N):
    dp.append(list(map(int, sys.stdin.readline().split())))

# print(dp)
for i in range(1, N):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2]) # 빨강 -> i 번째 집이 빨강이라면 이전 집은 초록이나 파랑 중 작은 값이어야 함.
    dp[i][1] += min(dp[i-1][2], dp[i-1][0]) # 초록
    dp[i][2] += min(dp[i-1][0], dp[i-1][1]) # 파랑

# print(dp)
result = min(dp[N-1])
print(result)