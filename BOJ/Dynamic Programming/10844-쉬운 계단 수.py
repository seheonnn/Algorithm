import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * 10 for _ in range(n + 1)] # i : 계단 수의 길이, j : 마지막 숫자가 j인 계단 수의 개수
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            # 마지막 숫자가 0이면, 이전 숫자는 반드시 1이어야 함
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            # 마지막 숫자가 9이면, 이전 숫자는 반드시 8이어야 함
            dp[i][j] = dp[i - 1][8]
        else:
            # 마지막 숫자가 1~8이면, 이전 숫자 j-1, j+1인 경우들의 합
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % (10 ** 9))