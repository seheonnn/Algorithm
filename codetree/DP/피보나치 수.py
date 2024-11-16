import sys
input = sys.stdin.readline

n = int(input())

# 재귀
# def func(n):
#     if n <= 2:
#         return 1
#     else:
#         return func(n - 1) + func(n - 2)

# print(func(n))

# DP
dp = [0] * 1000
dp[1] = 1
dp[2] = 1

for i in range(3, n + 1):
     dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])