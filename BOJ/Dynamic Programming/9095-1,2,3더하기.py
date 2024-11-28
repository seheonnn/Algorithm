import sys

input = sys.stdin.readline

t = int(input())
tests = [int(input()) for _ in range(t)]

dp = [0] * 12

# 초기값 설정
dp[1] = 1 # 1을 만드는 경우의 수는 1개
dp[2] = 2 # 2를 만드는 경우의 수는 2, 1 + 1
dp[3] = 4 # 3을 만드는 경우의 수는 1+1+1, 2+1, 1+2, 3

# DP 테이블 채우기
for i in range(4, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for n in tests:
    print(dp[n])
