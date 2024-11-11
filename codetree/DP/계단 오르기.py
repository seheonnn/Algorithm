import sys
input = sys.stdin.readline

n = int(input())

dp = [-1] * (1000+1)
dp[0] = 1 # 시작점은 한 가지
dp[1] = 0 # 2칸 or 3칸이므로 1칸은 도달 불가
dp[2] = 1 # 2계단은 한 가지
dp[3] = 1 # 3계단은 한 가지

# 점화식
# dp[i] = dp[i - 2] + dp[i - 3]
for i in range(4, n + 1):
    # 2칸 or 3칸씩 오르므로 i-2 or i-3 번째 칸에서 진행
    # 두 가지 방식 합산이므로 +임
    dp[i] = (dp[i - 2] + dp[i - 3]) % 10007

print(dp[n])