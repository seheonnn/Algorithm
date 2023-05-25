# 삼각형 양 끝은 바로 위 수, 중간 수들은 위에 있는 두 개의 수 중 최댓값 +
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