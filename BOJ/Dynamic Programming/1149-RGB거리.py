import sys
input = sys.stdin.readline

n = int(input())

# dp[i][0]: i번째 집을 빨강으로 칠했을 때의 누적 최소 비용
# dp[i][1]: i번째 집을 초록으로 칠했을 때의 누적 최소 비용
# dp[i][2]: i번째 집을 파랑으로 칠했을 때의 누적 최소 비용
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    # 빨강
    # 이전 집(i-1)이 초록(1) 또는 파랑(2)으로 칠한 경우 중 최소 비용
    dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
    # 초록
    dp[i][1] += min(dp[i - 1][2], dp[i - 1][0])
    # 파랑
    dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[n - 1]))