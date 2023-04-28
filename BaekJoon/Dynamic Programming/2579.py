import sys
N = int(sys.stdin.readline())
stair = [int(sys.stdin.readline())for _ in range(N)]
dp = [0] * (N)
if len(stair) <= 2:
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    for i in range(2, N):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i]) # 두 계단 연속 or 한 계단 건너 뜀. 둘 중 큰 값
    print(dp[-1])