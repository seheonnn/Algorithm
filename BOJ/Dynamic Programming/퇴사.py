import sys
input = sys.stdin.readline

n = int(input().strip())
t = []
p = []
dp = [0] * (n+1)
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n):
    # 상담하는 경우, i번째 날의 상담이 퇴사일(n) 이전에 끝나면
    if i + t[i] <= n:
        # dp[i+t[i]] i번째 날 상담을 마치는 날
        dp[i+t[i]] = max(dp[i+t[i]], dp[i] + p[i])

    # 상담을 진행하지 않는 경우: i번째 날의 최대 수익을 다음 날로 그대로 넘김
    dp[i + 1] = max(dp[i+1], dp[i])

print(dp[n])