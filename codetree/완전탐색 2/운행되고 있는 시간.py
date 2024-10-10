import sys
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

r = 0
for i in range(n):

    s = 0
    cnt = [0] * 1000
    for j, (x, y) in enumerate(arr):
        if i == j:
            continue
        for k in range(x, y):
            cnt[k] = 1
    s = sum(cnt)
    r = max(r, s)
print(r)
