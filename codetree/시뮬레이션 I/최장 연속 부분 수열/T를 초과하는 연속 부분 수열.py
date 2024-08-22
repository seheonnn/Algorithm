import sys
input = sys.stdin.readline

n, t = map(int, input().split())
a = list(map(int, input().split()))

m, cnt = 0, 0
for i in range(n):
    if a[i] > t:
        cnt += 1
    else:
        cnt = 0
    m = max(m, cnt)
print(m)