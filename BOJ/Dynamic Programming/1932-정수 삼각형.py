import sys
input = sys.stdin.readline

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1): # i층의 인덱스 0층이면 idx 0, 1층 이면 0, 1
        if j == 0:
            # 첫 번째 열은 대각선 왼쪽 값만 더할 수 있음
            dp[i][0] += dp[i - 1][0]
        elif j == i:
            # 마지막 열은 대각선 오른쪽 값만 더할 수 있음
            dp[i][j] += dp[i - 1][j - 1]
        else:
            # 그 외의 경우, 대각선 왼쪽(dp[i-1][j-1])과 오른쪽(dp[i-1][j]) 중 최대 값을 선택
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[n - 1])) # 최종적으로 마지막 층에서의 최대값 출력
