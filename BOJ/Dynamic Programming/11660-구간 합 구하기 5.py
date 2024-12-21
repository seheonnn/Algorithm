import sys
input = sys.stdin.readline

# 1. 입력 받기
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 2. DP 배열을 (n+1) x (n+1)로 설정 (1-indexed 접근을 위해)
dp = [[0] * (n + 1) for _ in range(n + 1)]

# 3. 누적합 DP 배열 계산 (1-indexed 접근)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # dp[i][j] : 1 부터 i, j까지의 합
        # 왼쪽(현재 위치의 왼쪽 부분) + 위쪽(현재 위치의 위쪽 부분) - 중복된 부분(왼쪽과 위쪽에 중복된 부분) + 현재 위치의 값(i-1, j-1)
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + matrix[i - 1][j - 1]

# 4. M개의 쿼리 처리
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 누적합으로 구간 합 구하기
    # (x1, y1)부터 (x2, y2)까지의 구간 합
    # 전체 합(dp[x2][y2])에서 위쪽 부분(dp[x1-1][y2])을 빼고 왼쪽 부분(dp[x2][y1-1])을 뺀 후 중복으로 뺀 부분(dp[x1-1][y1-1])을 다시 더해줌
    result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(result)
