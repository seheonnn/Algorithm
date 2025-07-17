import sys

input = sys.stdin.readline

n = int(input())
arr = []
INF = float('inf')
r = INF

for _ in range(n):
    arr.append(list(map(int, input().split())))

for rgb in range(3):  # 1번집 색 고정

    dp = [[INF, INF, INF] for _ in range(n)]
    dp[0][rgb] = arr[0][rgb]

    for i in range(1, n):
        dp[i][0] = arr[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = arr[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = arr[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    for i in range(3):
        if i != rgb:
            r = min(r, dp[n - 1][i])

print(r)