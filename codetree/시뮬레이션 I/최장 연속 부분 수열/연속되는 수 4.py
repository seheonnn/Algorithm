import sys
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

cnt, m = 1, 1

for i in range(1, n):
    if a[i-1] < a[i]:
        cnt += 1
    else:
        cnt = 1
    m = max(m, cnt)

print(m)