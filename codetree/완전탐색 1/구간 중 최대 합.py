import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
max_sum = 0
for i in range(0, n - k + 1):  # 구간 주의
    max_sum = max(max_sum, sum(arr[i:i + k]))
print(max_sum)
