import sys

input = sys.stdin.readline

n = int(input())
stair = [int(input()) for _ in range(n)]
dp = [0] * n

if len(stair) <= 2:
    print(sum(stair))
else:
    dp[0] = stair[0] # 0번째 칸과 1번째 칸의 경우의 수는 하나
    dp[1] = stair[0] + stair[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i]) # 연속으로 세 칸 밟을 수 없음
    print(dp[n - 1])