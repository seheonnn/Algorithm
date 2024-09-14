import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

answer = 0

for i in range(1, 101):
    cnt = 0
    for j in range(n):
        for k in range(j + 1, n):
            if arr[j] + arr[k] == i * 2: # a1 - k = k - a2 즉, a1 - a2 = 2 * k 여야 등차수열임
                cnt += 1
    answer = max(answer, cnt)

print(answer)
