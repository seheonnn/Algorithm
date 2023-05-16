import sys
N = int(sys.stdin.readline())
dp = []
for _ in range(N):
    dp.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, N):
    for j in range(i+1):
        if j==0:
            dp[i][0] += dp[i-1][0]
        elif j==i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[N-1]))