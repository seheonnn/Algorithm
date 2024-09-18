import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

r = 0
for i in range(1, 1001):  # 각 높이 완전탐색
    cnt = 0

    if arr[0] > i:
        cnt += 1

    for j in range(1, n):
        if arr[j] > i and arr[j - 1] <= i:
            cnt += 1

    r = max(r, cnt)

print(r)