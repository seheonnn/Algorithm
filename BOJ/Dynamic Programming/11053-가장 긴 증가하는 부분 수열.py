import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n # 수열의 길이 배열

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]: # i 까지 읽었을 때 arr[i]보다 작은 수의 개수 계산
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))