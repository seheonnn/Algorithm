import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp  = [0] * (n + 1)
dp[1] = 1
dp[2] = 3
for i in range(3, n + 1):
    # i - 1까지 채워진 경우 이후는 2 x 1 하나만 올 수 있음
    # i - 2까지 채워진 경우 이후는 2 x 2 하나 or 1 x 2 두 개 올 수 있음 (2 x 1 두 개 오는 경우는 앞에서 고려)
    dp[i] = (dp[i - 1] + (2 * dp[i - 2])) % 796796

print(dp[n])
