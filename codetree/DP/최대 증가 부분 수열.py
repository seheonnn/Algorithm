import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n + 1)]
# dp[i] 는 arr[i]를 마지막으로 하는 가장 긴 증가 부분 수열의 길이
for i in range(n):
    for j in range(i): # j : 이전의 모든 i 값
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1) # 갱신

print(max(dp)+1) # 최소 한 번은 점프하므로 1에서 시작