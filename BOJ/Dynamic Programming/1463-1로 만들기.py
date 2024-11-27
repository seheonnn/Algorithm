import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1) # i를 만드는 데 필요한 최소 연산 횟수

for i in range(2, n + 1): # dp[1] = 0임

    dp[i] = dp[i - 1] + 1 # 1 빼는 경우

    if i % 2 == 0: # 2로 나누는 경우
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0: # 3으로 나누는 경우
        dp[i] = min(dp[i], dp[i // 3] + 1)

    # i == 10인 경우
    # 10 // 2 = 5니까 dp[10] 은 dp[5] 의 값에서 1 증가한 값. 연산 하나 더 증가

print(dp[n])
