import sys
input = sys.stdin.readline

MOD = 1000000007
n = int(input())
dp = [0] * (n + 1)

dp[0] = 1
dp[1] = 2

for i in range(2, n + 1):
    # dp[i-1]*2 : 끝에 1 x 2 타일을 추가하는 경우 두 가지 1x2 두 개씩, 2 x 1 두 개씩
    dp[i] = (dp[i - 1] * 2 + dp[i - 2] * 3) % MOD
    for j in range(i - 3, -1, -1): # 남은 부분 2 x j 타일로 채우기
        dp[i] = (dp[i] + dp[j] * 2) % MOD
print(dp[n])