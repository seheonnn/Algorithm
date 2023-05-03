import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
dp = [0] * N
for i in range(N):
    for j in range(N):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))